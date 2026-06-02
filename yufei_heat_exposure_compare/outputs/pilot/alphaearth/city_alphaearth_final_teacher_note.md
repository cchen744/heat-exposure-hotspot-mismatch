# AlphaEarth summary update

This note summarizes the current AlphaEarth results for Houston and Phoenix.

## Houston
- Model performance: baseline=0.403, baseline+PC1-PC7=0.783, baseline+stable raw dims=0.754, combined=0.777.
- Stable raw dims: selected=15, shared=3, city-specific=12.
- Shared stable dims: A04, A22, A59.
- Top raw-dimension pairs: A16 ↔ lst_c (|r|=0.697); A07 ↔ lst_c (|r|=0.684).
- PC1–PC4 themes: PC1: land/water structure + thermal pattern (33.2%) | PC2: thermal pattern + land/water structure (17.9%) | PC3: thermal pattern + land/water structure (9.1%) | PC4: thermal pattern + land/water structure (7.2%).
- Takeaway: Houston: PC-only and combined models are very close (combined - PC-only = -0.006); extra raw dims add limited gain.

## Phoenix
- Model performance: baseline=0.176, baseline+PC1-PC7=0.668, baseline+stable raw dims=0.721, combined=0.731.
- Stable raw dims: selected=16, shared=3, city-specific=13.
- Shared stable dims: A04, A22, A59.
- Top raw-dimension pairs: A59 ↔ hi_minus_lst (|r|=0.627); A58 ↔ median_household_income_clean (|r|=0.593).
- PC1–PC4 themes: PC1: socioeconomic gradient + land/water structure (32.8%) | PC2: thermal pattern + socioeconomic gradient (16.3%) | PC3: thermal pattern + socioeconomic gradient (13.7%) | PC4: thermal pattern + socioeconomic gradient (7.6%).
- Takeaway: Phoenix: stable raw dims add meaningful value beyond PC1–PC7 (combined - PC-only = 0.063).

## Cross-city interpretation
- Shared stable dims are limited in number, while most stable raw dimensions are city-specific.
- Houston appears to be captured mainly by PC structure; adding stable raw dims gives little extra gain beyond PC1–PC7.
- Phoenix retains additional value from city-specific stable raw dims beyond PC1–PC7.
- These results support using both PCA-level interpretation and selected raw-dimension follow-up analysis.
