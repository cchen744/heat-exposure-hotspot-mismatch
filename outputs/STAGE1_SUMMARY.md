# Stage-1 Results Summary — LST–HI Mismatch Explainability

*Prepared 2026-06-11. Scope: 12 U.S. cities, 6,743 census tracts. Method: AlphaEarth 64-dim embeddings → per-city PCA (7 PCs) → Random Forest → SHAP.*

---

## 1. Pipeline (what the notebooks produce)

`01_build_modeling_table` joins the AlphaEarth 64-dim embeddings (A00–A63) to per-tract LST and Heat Index (HI), 12 cities pooled. `02_random_forest_cv` runs per-city RF (baseline / embed-only / baseline+embed) plus leave-one-city-out (LOCO) CV. `03–04` compute SHAP on the raw 64 dims and map it. `05_pca_interpretation` does per-city PCA, correlates each PC with observables, and runs SHAP on the PC scores. `06_three_outcome_pc_shap` (new) repeats the PC→RF→SHAP pipeline for **three targets** — LST, HI, and the mismatch — so they are directly comparable. `07_summary_figure` (new) renders the compact 12×3 overview.

**Target.** Mismatch = `gap_z = z(HI) − z(LST)`, z-scored per city. (Per-city z-scoring does not change R² — R² is scale-invariant — but it makes SHAP magnitudes comparable across cities and across the three outcomes.)

---

## 2. RQ1 — Does an LST–HI mismatch exist?

Yes. Across all tracts the surface is on average 12 °C hotter than the heat index (mean HI−LST = −12.2 °C, per-tract range −28 to +3 °C), and the spatial *patterns* diverge: the `compare_group` field flags large numbers of **HI-only hotspots** (~1,360 tracts) and **LST-only hotspots** (~855 tracts) — places that are humid-hot but not surface-hot, and vice versa. These are not the same neighborhoods, which is the entire premise of the study.

*Data-quality flag:* the binary `lst_hotspot` / `hi_hotspot` columns are saturated (all = 1) for Boston, Las Vegas, Los Angeles, and Miami, so per-city hotspot-mismatch counts derived from those two columns are unreliable for those cities. Use `compare_group` for RQ1 claims, and consider regenerating the hotspot flags.

---

## 3. RQ2 — Is the mismatch different across cities / climate zones?

Yes, strongly. Two independent signals:

**Explanatory strength varies city to city** (5-fold CV R² for the mismatch): high in Atlanta (.70), San Francisco (.64), LA (.60), Miami/Phoenix (.54); low in Las Vegas (.14), Seattle (.22), Boston (.26). The mismatch is far more spatially structured (embedding-predictable) in humid/coastal cities than in arid ones.

**Drivers do not transfer across cities.** LOCO CV (train on 11 cities, predict the 12th) is near-zero or negative for most cities (e.g. Las Vegas −0.62, Chicago −0.34; best is Houston/Dallas ≈ +0.24). A model of "what makes the mismatch large" learned elsewhere does **not** generalize — the mismatch is governed by city-specific land-surface structure, consistent with distinct climate regimes.

---

## 4. RQ3 — What factors drive the mismatch? (PCA + SHAP — the core result)

**Embeddings carry the signal, not demographics.** Per-city RF: demographics alone give R² ≈ 0; embeddings alone give R² up to .78; adding demographics to embeddings changes nothing. The drivers of the mismatch are land-surface/land-cover factors captured by AlphaEarth, not the ACS poverty/income variables.

**PC1 ≈ a surface/land-cover axis that drives the mismatch.** In most cities PC1 is the top SHAP contributor to the mismatch and correlates strongly with LST and with the mismatch but **not** with HI — e.g. Atlanta PC1: r = −0.77 vs LST, +0.77 vs mismatch, ≈0 vs HI. The mismatch tracks the surface side.

### New three-outcome comparison (advisor's request)

Running the identical PC→RF→SHAP pipeline with LST, HI, and the mismatch as targets:

| Outcome | mean CV R² | interpretation |
|---|---|---|
| **LST** | **0.53** | embeddings explain surface temperature best |
| **Mismatch** | **0.44** | in between |
| **HI** | **0.39** | embeddings explain heat index worst |

This ordering is the key quantitative result: **AlphaEarth embeddings are a land-surface representation, so they explain LST strongly and HI weakly.** HI is humidity-driven — governed by regional atmospheric moisture rather than local land cover — so the embeddings are largely blind to it. That blindness is precisely *why* satellite/surface measures under-capture humidity-driven heat exposure.

**The mismatch is driven by the LST axis, not the HI axis.** The dominant SHAP PC for the mismatch equals the dominant PC for **LST in 11 of 12 cities** (PC1 for Atlanta, Boston, Dallas, Houston, Miami, New York, Seattle; PC3 for Las Vegas, Phoenix, San Francisco) and **never** equals HI's dominant PC (HI loads on PC2/4/5/6/7). So the spatial structure of the mismatch inherits the land-cover factors that drive surface heat. Cities also split into a "PC1-driven" group and a "PC3-driven" group, reinforcing RQ2's city heterogeneity.

See `outputs/figures/summary_12cities_3outcomes.png` for the 12×3 overview (★ marks cells where the mismatch's top PC = LST's top PC).

---

## 5. Headline for the paper

1. The LST–HI mismatch is real and spatially organized, but its structure is **city-specific** (drivers don't transfer).
2. It is explained by **land-surface factors, not demographics**.
3. **AlphaEarth embeddings explain LST ≫ HI**, and the mismatch is driven by the **same surface axis as LST** — a direct, quantified demonstration that surface/satellite features miss the humidity component of heat exposure.

## 6. Suggested next steps

Regenerate the saturated hotspot flags (§2). Attach climate-zone / Köppen labels to formalize the RQ2 city groupings. Interpret what the recurring PC1 (and PC3) land-cover axes physically represent via their top embedding-dimension loadings. Optionally test whether adding an explicit humidity/moisture covariate raises the HI R² — if it does, it confirms the "embeddings miss humidity" reading.

---
*Tables: `outputs/tables/three_outcome_model_summary.csv`, `three_outcome_pc_shap_importance.csv`, `model_comparison.csv`, `loco_cv_results.csv`, `all_cities_pc_obs_corr.csv`, `all_cities_pc_shap_importance.csv`.*
