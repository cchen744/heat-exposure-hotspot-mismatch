# RQ1 methods draft

## Study design
This pilot analysis focuses on two cities, Houston and Phoenix, and compares tract-level Land Surface Temperature (LST) with tract-level Heat Index (HI).

## Core inputs
- Tract-level LST values were derived from the processed summer LST workflow.
- Tract-level HI values were derived from the processed heat-index workflow.
- The analysis was conducted on census tracts with valid geometry and available LST/HI values.

## Hotspot definition
Hotspots were defined separately within each city and separately for each measure as the top 20% of tracts.

## Comparison framework
Each tract was assigned to one of five categories:
- Overlap hotspot
- LST-only hotspot
- HI-only hotspot
- Neither
- Missing

## Quantitative metrics
The comparison was summarized using:
- hotspot counts
- overlap share
- LST-only share
- HI-only share
- Jaccard index

The Jaccard index is defined as:
Jaccard = overlap / (overlap + LST-only + HI-only)

## Continuous interpretation layer
To interpret relative humidity-sensitive heat exposure, we also computed a standardized gap:
HI_z − LST_z

Positive values indicate tracts where HI is relatively stronger than LST, while negative values indicate tracts where LST is relatively stronger than HI.

## Current city-level data coverage
- Houston valid tracts with both measures: 549
- Houston missing HI tracts: 105
- Phoenix valid tracts with both measures: 332
- Phoenix missing HI tracts: 41
