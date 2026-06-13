"""
08_permanova_city_embeddings.py

Advisor (Song) request: statistically justify city-specific vs universal PCA by
testing whether AlphaEarth (AE) 64-D embeddings differ across cities.

Workflow:
  1. Balanced random sample of AE 64-D embeddings per city.
  2. Pairwise distance matrices (Euclidean and Cosine).
  3. PERMANOVA  -> do city centroids differ? (pseudo-F, p, R2 = between-city share)
  4. PERMDISP   -> are within-city dispersions homogeneous? (so PERMANOVA isn't
                   just driven by unequal spread)
Interpretation:
  large R2 + significant PERMANOVA  => embeddings shift strongly across cities
                                       => city-specific (local) PCA is justified.

PERMANOVA implemented directly from the distance matrix (Anderson 2001) to avoid
heavy deps. PERMDISP via distance-to-centroid + Levene/Kruskal on those distances.
"""
import os, warnings; warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
from pathlib import Path
from scipy.spatial.distance import pdist, squareform
from scipy.stats import f_oneway, kruskal

rng = np.random.default_rng(42)
ROOT = Path(__file__).resolve().parents[1]
TAB  = ROOT / "outputs" / "tables"; TAB.mkdir(parents=True, exist_ok=True)

mt = pd.read_csv(ROOT / "data/processed/modeling_table.csv", dtype={"GEOID": str})
E  = [f"A{i:02d}" for i in range(64)]
PER_CITY = 100          # balanced sample size per city
N_PERM   = 999

# ---- balanced sample ----
parts = []
for c, g in mt.groupby("city"):
    g = g.dropna(subset=E)
    take = min(PER_CITY, len(g))
    parts.append(g.sample(take, random_state=42))
samp = pd.concat(parts).reset_index(drop=True)
X = samp[E].values.astype(float)
labels = samp["city"].values
cities = np.unique(labels)
a, N = len(cities), len(samp)
print(f"sample: {N} pts, {a} cities, {PER_CITY}/city")

def permanova(D2, labels, n_perm=999, seed=42):
    """PERMANOVA from a SQUARED-distance matrix (Anderson 2001)."""
    r = np.random.default_rng(seed)
    N = D2.shape[0]; cats = np.unique(labels); a = len(cats)
    onehot = {c: (labels == c) for c in cats}
    SS_T = D2[np.triu_indices(N, 1)].sum() / N
    def ss_within(lab):
        s = 0.0
        for c in cats:
            idx = np.where(lab == c)[0]
            n = len(idx)
            if n > 1:
                sub = D2[np.ix_(idx, idx)]
                s += sub[np.triu_indices(n, 1)].sum() / n
        return s
    SS_W = ss_within(labels)
    SS_A = SS_T - SS_W
    F = (SS_A / (a - 1)) / (SS_W / (N - a))
    R2 = SS_A / SS_T
    perm = labels.copy(); count = 0
    for _ in range(n_perm):
        r.shuffle(perm)
        sw = ss_within(perm)
        Fp = ((SS_T - sw) / (a - 1)) / (sw / (N - a))
        if Fp >= F: count += 1
    p = (count + 1) / (n_perm + 1)
    return F, p, R2

def permdisp(X, labels):
    """Distance of each point to its (Euclidean) city centroid; test homogeneity."""
    d2c = np.zeros(len(X))
    for c in np.unique(labels):
        m = labels == c
        d2c[m] = np.linalg.norm(X[m] - X[m].mean(0), axis=1)
    groups = [d2c[labels == c] for c in np.unique(labels)]
    Fl, pl = f_oneway(*groups)        # Levene-style on distances-to-centroid
    Hk, pk = kruskal(*groups)
    disp = {c: round(d2c[labels == c].mean(), 3) for c in np.unique(labels)}
    return Fl, pl, Hk, pk, disp

rows = []
for metric in ["euclidean", "cosine"]:
    D = squareform(pdist(X, metric=metric))
    F, p, R2 = permanova(D**2, labels, n_perm=N_PERM)
    print(f"\n[{metric}] PERMANOVA: pseudo-F={F:.1f}  p={p:.4f}  R2(between-city)={R2:.3f}")
    rows.append({"metric": metric, "test": "PERMANOVA", "stat_F": round(F, 2),
                 "p_value": p, "R2_between_city": round(R2, 4), "n": N, "n_perm": N_PERM})

Fl, pl, Hk, pk, disp = permdisp(X, labels)
print(f"\nPERMDISP (Euclidean dist-to-centroid): ANOVA F={Fl:.1f} p={pl:.2e} | Kruskal H={Hk:.1f} p={pk:.2e}")
print("per-city mean dispersion:", disp)
rows.append({"metric": "euclidean", "test": "PERMDISP_ANOVA", "stat_F": round(Fl, 2),
             "p_value": pl, "R2_between_city": "", "n": N, "n_perm": ""})
rows.append({"metric": "euclidean", "test": "PERMDISP_Kruskal", "stat_F": round(Hk, 2),
             "p_value": pk, "R2_between_city": "", "n": N, "n_perm": ""})

pd.DataFrame(rows).to_csv(TAB / "permanova_city_embeddings.csv", index=False)
pd.DataFrame([{"city": c, "mean_dispersion": v} for c, v in disp.items()]).to_csv(
    TAB / "permdisp_city_dispersion.csv", index=False)
print("\nsaved outputs/tables/permanova_city_embeddings.csv")
print("saved outputs/tables/permdisp_city_dispersion.csv")
