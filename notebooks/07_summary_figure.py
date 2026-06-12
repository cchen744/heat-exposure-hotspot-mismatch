"""
07_summary_figure.py
Compact summary figure: 12 cities x 3 outcomes (LST, HI, mismatch).
 - cell color = 5-fold CV R2 (explanatory strength of AlphaEarth embeddings)
 - cell text  = R2 value + dominant SHAP PC
 - a star marks cells where the mismatch's dominant PC == LST's dominant PC
   (i.e. the mismatch is driven by the surface/LST axis)
Outputs: outputs/figures/summary_12cities_3outcomes.png (+ .pdf)
"""
import pandas as pd, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAB  = ROOT / "outputs" / "tables"
FIG  = ROOT / "outputs" / "figures"; FIG.mkdir(parents=True, exist_ok=True)

d = pd.read_csv(TAB / "three_outcome_model_summary.csv")
OC = ["lst_z", "hi_z", "gap_z"]
LABELS = {"lst_z": "LST", "hi_z": "HI", "gap_z": "Mismatch\n(HI−LST)"}

r2  = d.pivot(index="city", columns="outcome", values="cv_r2")[OC]
top = d.pivot(index="city", columns="outcome", values="top_pc")[OC]

# order cities by mismatch explanatory strength (descending) for readability
r2 = r2.sort_values("gap_z", ascending=False)
top = top.loc[r2.index]
cities = [c.replace("_", " ").title() for c in r2.index]

vals = r2.values
mat_top = top.values

# colormap: clamp negatives to 0 for color; white->teal
cmap = LinearSegmentedColormap.from_list("r2", ["#f7fbff", "#9ecae1", "#3182bd", "#08519c"])
disp = np.clip(vals, 0, 0.8)

fig, ax = plt.subplots(figsize=(6.4, 7.6))
im = ax.imshow(disp, cmap=cmap, vmin=0, vmax=0.8, aspect="auto")

ax.set_xticks(range(3)); ax.set_xticklabels([LABELS[o] for o in OC], fontsize=11, fontweight="bold")
ax.set_yticks(range(len(cities))); ax.set_yticklabels(cities, fontsize=10)
ax.set_xticks(np.arange(-.5, 3, 1), minor=True)
ax.set_yticks(np.arange(-.5, len(cities), 1), minor=True)
ax.grid(which="minor", color="white", linewidth=1.5)
ax.tick_params(which="minor", length=0)
ax.tick_params(axis="x", top=True, labeltop=True, bottom=False, labelbottom=False)

lst_top = top["lst_z"].values
for i in range(len(cities)):
    for j, o in enumerate(OC):
        v = vals[i, j]; pc = mat_top[i, j]
        txt_color = "white" if disp[i, j] > 0.45 else "#222222"
        star = ""
        if o == "gap_z" and pc == lst_top[i]:
            star = "  ★"  # mismatch driven by LST axis
        ax.text(j, i - 0.13, f"{v:.2f}", ha="center", va="center",
                color=txt_color, fontsize=10.5, fontweight="bold")
        ax.text(j, i + 0.22, f"{pc}{star}", ha="center", va="center",
                color=txt_color, fontsize=8)

cbar = fig.colorbar(im, ax=ax, fraction=0.045, pad=0.03)
cbar.set_label("5-fold CV R²  (AlphaEarth → outcome)", fontsize=9)

ax.set_title("AlphaEarth embeddings explain LST best, HI worst,\n"
             "and the mismatch is driven by the LST axis (★)",
             fontsize=11, pad=34)
# column means footnote
means = r2.mean()
fig.text(0.13, 0.012,
         f"Column mean R²:  LST {means['lst_z']:.2f}   |   HI {means['hi_z']:.2f}   |   "
         f"Mismatch {means['gap_z']:.2f}        ★ = mismatch's top SHAP PC = LST's top PC",
         fontsize=8, color="#444444")
plt.tight_layout(rect=[0, 0.02, 1, 1])
for ext in ("png", "pdf"):
    plt.savefig(FIG / f"summary_12cities_3outcomes.{ext}", dpi=220, bbox_inches="tight")
plt.close()
print("saved outputs/figures/summary_12cities_3outcomes.png / .pdf")
