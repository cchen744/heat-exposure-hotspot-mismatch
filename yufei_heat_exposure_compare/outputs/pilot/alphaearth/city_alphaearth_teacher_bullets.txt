# AlphaEarth summary for teacher

This note combines three outputs:
1. PC1-PC4 interpretation
2. Stable raw-dimension vs observable-variable links
3. Predictive comparison of PCs vs stable raw dimensions

## Houston
- Model performance (CV R²): baseline=0.4030, PC-only=0.7833, rawdim-only=0.7544, combined=0.7773.
- Gains vs baseline: PC-only=0.3803, rawdim-only=0.3514, combined=0.3743.
- Best model: baseline + PC1-PC7.
- Top raw-dim / observable links: A16 ↔ lst_c (|r|=0.697); A07 ↔ lst_c (|r|=0.684).
- PC interpretation summary: PC1 explains 33.2% (cum 33.2%). Theme: land/water structure + thermal pattern. Top factors: land area (0.597); LST (0.535); HI-LST gap (0.500). | PC2 explains 17.9% (cum 51.1%). Theme: thermal pattern + land/water structure. Top factors: LST (0.380); HI-LST gap (0.370); land area (0.181). | PC3 explains 9.1% (cum 60.2%). Theme: thermal pattern + land/water structure. Top factors: LST (0.319); HI-LST gap (0.309); land area (0.249). | PC4 explains 7.2% (cum 67.3%). Theme: thermal pattern + land/water structure. Top factors: LST (0.365); HI-LST gap (0.332); land area (0.293).
- Working interpretation: Stable raw dims capture similar signal to PCs and help interpretation.

## Phoenix
- Model performance (CV R²): baseline=0.1759, PC-only=0.6685, rawdim-only=0.7212, combined=0.7311.
- Gains vs baseline: PC-only=0.4927, rawdim-only=0.5453, combined=0.5553.
- Best model: baseline + PC1-PC7 + stable raw dims.
- Top raw-dim / observable links: A59 ↔ hi_minus_lst (|r|=0.627); A58 ↔ median_household_income_clean (|r|=0.593).
- PC interpretation summary: PC1 explains 32.8% (cum 32.8%). Theme: socioeconomic gradient + land/water structure. Top factors: land area (0.459); median income (0.288); poverty rate (0.228). | PC2 explains 16.3% (cum 49.1%). Theme: thermal pattern + socioeconomic gradient. Top factors: median income (0.206); HI-LST gap (0.196); HI (0.191). | PC3 explains 13.7% (cum 62.8%). Theme: thermal pattern + socioeconomic gradient. Top factors: HI-LST gap (0.405); LST (0.397); median income (0.354). | PC4 explains 7.6% (cum 70.4%). Theme: thermal pattern + socioeconomic gradient. Top factors: HI-LST gap (0.267); LST (0.242); HI (0.206).
- Working interpretation: Stable raw dims add useful information beyond PCs.

## Cross-city takeaway
- Houston best model: baseline + PC1-PC7. This suggests stable raw dims capture similar signal to pcs and help interpretation.
- Phoenix best model: baseline + PC1-PC7 + stable raw dims. This suggests stable raw dims add useful information beyond pcs.
- Overall, the stable raw dimensions are now interpretable and can be compared directly against the PCA-based summaries.