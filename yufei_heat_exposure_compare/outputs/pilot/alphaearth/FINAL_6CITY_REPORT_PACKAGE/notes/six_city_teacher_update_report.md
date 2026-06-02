# Six-city LST vs Heat Index report package

## Core status
The six-city core dataset is ready for LST vs Heat Index mismatch analysis.

- Houston: 549/549 ready (100.0%)
- Phoenix: 332/332 ready (100.0%)
- Las Vegas: 458/458 ready (100.0%)
- Los Angeles: 1080/1108 ready (97.5%)
- Miami: 125/129 ready (96.9%)
- Boston: 191/207 ready (92.3%)

## Key findings
- The six-city dataset is now analysis-ready for the core LST vs Heat Index comparison. Houston: 549/549 ready (100.0%); Phoenix: 332/332 ready (100.0%); Las Vegas: 458/458 ready (100.0%); Los Angeles: 1080/1108 ready (97.5%); Miami: 125/129 ready (96.9%); Boston: 191/207 ready (92.3%).
- Miami and Boston show the strongest Heat-Index-dominant pattern: Miami has 52.0% HI-only hotspots and 50.4% priority tracts; Boston has 47.6% HI-only hotspots and 44.0% priority tracts.
- Las Vegas behaves differently: it has the highest LST-HI correlation (0.75) and is classified as Coupled LST-HI, suggesting a more coupled surface-heat and apparent-heat pattern.
- Los Angeles is classified as Moderate HI-dominant, with 25.9% HI-only hotspots and 17.8% LST-only hotspots. This makes it a useful coastal/dry comparison case.
- The next strongest paper framing is: LST and Heat Index identify different spatial mechanisms of urban heat risk across climate and coastal/inland contexts, rather than simply producing the same hotspot map.

## Best figures to use first
- `01_six_city_mismatch_class_maps.png`: Six-city spatial distribution of LST-HI hotspot mismatch. Purple shows tracts that are both LST and Heat Index hotspots; orange shows LST-only hotspots; green shows Heat-Index-only hotspots. This is the main map for showing that LST and Heat Index identify different risk areas across cities.
- `02_six_city_relative_dominance_maps.png`: Relative dominance map showing where Heat Index ranks higher than LST and where LST ranks higher than Heat Index. This helps move beyond hotspot counts by showing within-city spatial gradients.
- `03_six_city_priority_tract_maps.png`: Priority tracts based on HI-only hotspots and high apparent-vs-surface heat contrast. This figure identifies candidate areas where LST alone may underestimate apparent heat risk.
- `04_six_city_mechanism_typology_maps.png`: Mechanism typology maps linking spatial patterns to city-level interpretation. Miami and Boston are classified as strong HI-dominant; Las Vegas is more coupled; Los Angeles is moderate HI-dominant; Houston and Phoenix are mixed/transitional.
- `05_six_city_mechanism_space.png`: Mechanism space comparing LST-only and Heat-Index-only hotspot shares. Cities above the diagonal are more Heat-Index-dominant, while cities near the diagonal show stronger LST-HI coupling.
- `06_six_city_heat_risk_signature_matrix.png`: Heat-risk signature matrix summarizing each city across mean LST, mean Heat Index, LST-HI correlation, hotspot mismatch shares, and priority tract share.

## Suggested paper framing
A promising framing is that surface heat and apparent heat reveal different spatial mechanisms of urban heat exposure. Dry/inland cities such as Las Vegas show more coupled LST-HI patterns, while coastal/humid or temperate cities such as Miami and Boston show stronger Heat-Index-only hotspot patterns. This supports the argument that relying only on LST can miss important apparent-heat risk areas.
