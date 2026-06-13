"""
09_permanova_ordination.py
Visual companion to the PERMANOVA test: 2-D ordination of the AE embedding
sample colored by city (shows centroid + dispersion separation), plus a
per-city dispersion bar. Illustrates why a city-specific PCA is warranted.
Outputs: outputs/figures/permanova_ordination.png / .pdf
"""
import warnings; warnings.filterwarnings("ignore")
import numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

ROOT = Path(__file__).resolve().parents[1]
FIG  = ROOT / "outputs" / "figures"; FIG.mkdir(parents=True, exist_ok=True)
mt = pd.read_csv(ROOT / "data/processed/modeling_table.csv", dtype={"GEOID": str})
E  = [f"A{i:02d}" for i in range(64)]

parts = []
for c, g in mt.groupby("city"):
    g = g.dropna(subset=E); parts.append(g.sample(min(100, len(g)), random_state=42))
samp = pd.concat(parts).reset_index(drop=True)
X = StandardScaler().fit_transform(samp[E].values)
labels = samp["city"].values
cities = sorted(np.unique(labels))

pca = PCA(2, random_state=42).fit(X); S = pca.transform(X)
evr = pca.explained_variance_ratio_ * 100

disp = pd.read_csv(ROOT / "outputs/tables/permdisp_city_dispersion.csv")
disp = disp.set_index("city").loc[cities]

cmap = plt.get_cmap("tab20")
colors = {c: cmap(i) for i, c in enumerate(cities)}

fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.6), gridspec_kw={"width_ratios": [1.6, 1]})

# ---- Panel A: ordination ----
for c in cities:
    m = labels == c
    ax.scatter(S[m, 0], S[m, 1], s=14, alpha=0.55, color=colors[c],
               label=c.replace("_", " ").title(), edgecolors="none")
    # centroid marker
    ax.scatter(S[m, 0].mean(), S[m, 1].mean(), s=160, color=colors[c],
               edgecolors="black", linewidths=1.2, marker="o", zorder=5)
ax.set_xlabel(f"PC1 ({evr[0]:.0f}% var)"); ax.set_ylabel(f"PC2 ({evr[1]:.0f}% var)")
ax.set_title("AlphaEarth embeddings cluster by city\n(dots = tracts, ringed = city centroids)", fontsize=11)
ax.legend(fontsize=7, ncol=2, loc="upper right", framealpha=0.9, markerscale=1.2)
ax.text(0.02, 0.02,
        "PERMANOVA (Euclidean): pseudo-F=218.5, R²=0.67, p=0.001\n"
        "PERMANOVA (Cosine):    pseudo-F=450.5, R²=0.81, p=0.001\n"
        "PERMDISP: p<10⁻³⁰  (dispersion also differs)",
        transform=ax.transAxes, fontsize=8.5, va="bottom",
        bbox=dict(boxstyle="round", fc="white", ec="#888", alpha=0.9))

# ---- Panel B: per-city dispersion ----
d = disp["mean_dispersion"].sort_values()
ax2.barh([c.replace("_", " ").title() for c in d.index], d.values,
         color=[colors[c] for c in d.index], edgecolor="black", linewidth=0.5)
ax2.set_xlabel("Mean distance to city centroid")
ax2.set_title("Within-city dispersion\n(heterogeneous → PERMDISP sig.)", fontsize=11)
ax2.grid(axis="x", alpha=0.3)

plt.tight_layout()
for ext in ("png", "pdf"):
    plt.savefig(FIG / f"permanova_ordination.{ext}", dpi=200, bbox_inches="tight")
plt.close()
print("saved outputs/figures/permanova_ordination.png / .pdf")
