# las_vegas heat extraction input package

## What this file is
This package combines:
- tract geometry
- GEOID join key
- ACS baseline variables
- reserved heat columns for future integration

## Current status
This means las_vegas is now ready for the next stage:
heat-data integration / heat extraction workflow.

## Included baseline fields
- total_population_clean
- median_household_income_clean
- below_poverty_count
- poverty_universe
- poverty_rate

## Reserved heat fields
- lst_c
- air_temp_c
- rh_pct
- hi_c
- hi_minus_lst

## Output files
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_heat_extraction_input.gpkg
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_heat_extraction_input.geojson
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_heat_extraction_input.csv
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_heat_extraction_input_summary.csv
