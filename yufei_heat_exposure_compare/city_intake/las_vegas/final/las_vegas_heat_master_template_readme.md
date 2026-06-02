# las_vegas heat master template

## Current status
This file is a heat-ready master template for las_vegas.

It already includes:
- tract join key (GEOID)
- tract identifiers and geometry-related summary fields
- ACS baseline variables:
  - total_population_clean
  - median_household_income_clean
  - below_poverty_count
  - poverty_universe
  - poverty_rate

It does NOT yet include real heat variables.

## Heat columns reserved for next step
- lst_c
- air_temp_c
- rh_pct
- hi_c
- hi_minus_lst

## Interpretation
This means Las Vegas is now ready for the real heat-data integration step.
Once a tract-level heat table is prepared, it should merge into this template by GEOID.

## Files created
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_heat_master_template.csv
- /Users/yufeizhou/Desktop/heat-exposure-compare/city_intake/las_vegas/working/las_vegas_heat_master_template_summary.csv
