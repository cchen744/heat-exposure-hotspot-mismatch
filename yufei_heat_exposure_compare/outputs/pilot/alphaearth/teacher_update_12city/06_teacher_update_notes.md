# 12-city LST vs Heat Index teacher update

## Current status
I expanded the comparison to 12 cities and organized the results into a city-level story table, context-level summaries, and robustness checks.

## Main finding
The strongest pattern is that coastal / water-influenced cities show a larger shift toward Heat-Index-only hotspots. The equal-city mean HI-only minus LST-only hotspot gap is 22.7 percentage points for coastal / water-influenced cities, compared with 7.0 percentage points for the other cities.

## Strongest apparent-heat shift cases
- San Francisco: HI-only 53.2%, LST-only 0.0%, gap 53.2 pp, context = Coastal / compact / bay-influenced.
- Miami: HI-only 52.0%, LST-only 2.4%, gap 49.6 pp, context = Coastal / humid.
- Boston: HI-only 47.6%, LST-only 11.5%, gap 36.1 pp, context = Coastal / temperate.

## Robustness
The leave-one-out check stays positive for every removed city. The coastal-minus-noncoastal difference ranges from 10.6 to 19.4 pp.
This suggests the context-gradient pattern is not caused by a single outlier city.

## Important caution
This is still a 12-city descriptive comparison, so I should frame the result as a robust pilot pattern, not as causal proof or a final statistically significant conclusion.

## Possible paper story
A strong paper direction is: LST-based urban heat mapping may under-detect apparent-heat risk in humid, coastal, or water-influenced cities. The mismatch between LST and Heat Index appears to be structured by urban-climate context, rather than being random across cities.

## Suggested next step
The next analytical step is to expand the city sample using a structured typology: coastal humid, coastal dry, Great Lakes, inland desert, and inland humid / Sun Belt cities. This would test whether the 12-city pattern remains stable at a larger scale.