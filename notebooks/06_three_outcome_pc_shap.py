"""
06_three_outcome_pc_shap.py  (resumable, chunked)

Advisor request: run the SAME per-city PCA + RF + SHAP pipeline used for the
mismatch (gap_z) on LST and HI separately, so the three outcomes are comparable.

Reuses per-city PC scores from 05 (outputs/tables/<city>_pc_scores.csv).
Targets (per-city z-scored -> SHAP magnitudes comparable):
  lst_z = z(LST) ; hi_z = z(HI) ; gap_z = z(HI)-z(LST)

Per city x outcome: RF(PC1..PC7) 5-fold CV R2, train R2, mean|SHAP| per PC, top PC.
SHAP averaged over a <=600-row sample (mean is stable) for speed.

Resumable: skips cities already in the summary CSV. Pass MAX_CITIES env to cap per run.

Outputs:
  outputs/tables/three_outcome_model_summary.csv
  outputs/tables/three_outcome_pc_shap_importance.csv
"""
import os, warnings; warnings.filterwarnings("ignore")
import numpy as np, pandas as pd, shap
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score

ROOT = Path(__file__).resolve().parents[1]
TAB  = ROOT / "outputs" / "tables"
SUM_P = TAB / "three_outcome_model_summary.csv"
IMP_P = TAB / "three_outcome_pc_shap_importance.csv"
MAX_CITIES = int(os.environ.get("MAX_CITIES", "99"))
N_TREES = 150
SHAP_N  = 600

mt = pd.read_csv(ROOT / "data/processed/modeling_table.csv", dtype={"GEOID": str})
mt["GEOID"] = mt["GEOID"].str.zfill(11)
CITIES = sorted(mt["city"].unique().tolist())

def zs(s): return (s - s.mean()) / s.std() if s.std() > 0 else s * 0
def build_targets(g):
    return pd.DataFrame({"lst_z": zs(g["lst_c"]), "hi_z": zs(g["hi_c"]),
                         "gap_z": zs(g["hi_c"]) - zs(g["lst_c"])}, index=g.index)
mt = pd.concat([mt, mt.groupby("city", group_keys=False).apply(build_targets)], axis=1)

OUTCOMES = ["lst_z", "hi_z", "gap_z"]
cv = KFold(n_splits=5, shuffle=True, random_state=42)

done_pairs = set()
if SUM_P.exists():
    d = pd.read_csv(SUM_P)
    done_pairs = set(zip(d["city"], d["outcome"]))
done_cities = {c for c in CITIES if all((c, o) in done_pairs for o in ["lst_z", "hi_z", "gap_z"])}
todo = [c for c in CITIES if c not in done_cities][:MAX_CITIES]
print("done cities:", sorted(done_cities), "| this run:", todo)

for city in todo:
    sum_rows, imp_rows = [], []
    pc_path = TAB / f"{city}_pc_scores.csv"
    if not pc_path.exists():
        print(f"{city}: no PC scores, skip"); continue
    pc_df = pd.read_csv(pc_path, dtype={"GEOID": str}); pc_df["GEOID"] = pc_df["GEOID"].str.zfill(11)
    PC = [c for c in pc_df.columns if c.startswith("PC")]
    merged = pc_df.merge(mt[mt.city == city][["GEOID"] + OUTCOMES], on="GEOID", how="inner")
    if len(merged) < 20:
        print(f"{city}: too few rows"); continue
    X = merged[PC]
    print(f"{city.upper():15s} n={len(merged)}", flush=True)
    for oc in OUTCOMES:
        if (city, oc) in done_pairs:
            print(f"   {oc:6s} already done, skip", flush=True); continue
        y = merged[oc]; m = y.notna(); Xc, yc = X[m], y[m]
        rf = RandomForestRegressor(n_estimators=N_TREES, random_state=42, n_jobs=-1)
        cvs = cross_val_score(rf, Xc, yc, cv=cv, scoring="r2")
        rf.fit(Xc, yc)
        tr = rf.score(Xc, yc)
        Xs = Xc.sample(min(SHAP_N, len(Xc)), random_state=0)
        sv = shap.TreeExplainer(rf).shap_values(Xs)
        imp = pd.Series(np.abs(sv).mean(axis=0), index=PC).sort_values(ascending=False)
        print(f"   {oc:6s} CV={cvs.mean():+.3f}±{cvs.std():.3f} train={tr:.3f} top={imp.index[0]}({imp.iloc[0]:.3f})", flush=True)
        sum_rows.append({"city": city, "outcome": oc, "cv_r2": round(cvs.mean(), 4),
                         "cv_std": round(cvs.std(), 4), "train_r2": round(tr, 4),
                         "top_pc": imp.index[0], "top_pc_shap": round(imp.iloc[0], 4), "n": int(m.sum())})
        for pc, v in imp.items():
            imp_rows.append({"city": city, "outcome": oc, "pc": pc, "mean_abs_shap": round(v, 4)})
        # write per outcome (resumable on timeout)
        pd.DataFrame(sum_rows[-1:]).to_csv(SUM_P, mode="a", header=not SUM_P.exists(), index=False)
        pd.DataFrame([r for r in imp_rows if r["outcome"] == oc and r["city"] == city]).to_csv(
            IMP_P, mode="a", header=not IMP_P.exists(), index=False)
        print(f"   saved {city}/{oc}", flush=True)

print("run complete")
