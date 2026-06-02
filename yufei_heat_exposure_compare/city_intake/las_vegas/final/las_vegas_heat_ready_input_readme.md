# Las Vegas heat-ready input

## What this step did
Added tract-level summer 2024 ERA5-Land climate variables to Las Vegas.

Added columns:
- air_temp_c
- rh_pct
- hi_c
- hi_minus_lst = hi_c - lst_c

## Inputs
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_heat_extraction_input.geojson
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_heat_master_template.csv

## Outputs
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_era5_heat_tracts_summer2024.csv
- /Users/yufeizhou/Desktop/heat-exposure-compare/outputs/pilot/alphaearth/las_vegas_era5_heat_tracts_summer2024_summary.csv
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_heat_ready_input.gpkg
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_heat_ready_input.geojson
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_heat_ready_input.csv
- /Users/yufeizhou/Desktop/heat-exposure-compare/outputs/pilot/alphaearth/las_vegas_heat_master_template_after_era5_summary.csv

## Notes
- Summer window: 2024-06-01 to 2024-09-01
- Dataset: ECMWF/ERA5_LAND/HOURLY
- Scale: 11132
