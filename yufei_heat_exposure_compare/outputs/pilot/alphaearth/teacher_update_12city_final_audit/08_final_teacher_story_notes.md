# Final 12-city story audit

## Core finding
At the city level, coastal / water-influenced cities show a stronger shift toward Heat-Index-only hotspots. The equal-city coastal-minus-noncoastal difference is 15.7 percentage points.
However, when cities are weighted by the number of analysis-ready tracts, the difference is 0.7 percentage points. This means the result should be framed as a city-level typology pattern, not as a pooled tract-level effect.

## Strongest apparent-heat shift cases
- San Francisco: gap = 53.2 pp, HI-only = 53.2%, LST-only = 0.0%, context = Coastal / compact / bay-influenced, ready = 72.3%.
- Miami: gap = 49.6 pp, HI-only = 52.0%, LST-only = 2.4%, context = Coastal / humid, ready = 96.9%.
- Boston: gap = 36.1 pp, HI-only = 47.6%, LST-only = 11.5%, context = Coastal / temperate, ready = 92.3%.
- Atlanta: gap = 13.9 pp, HI-only = 32.3%, LST-only = 18.4%, context = Inland / humid / sprawling Sun Belt, ready = 100.0%.
- Seattle: gap = 11.2 pp, HI-only = 33.0%, LST-only = 21.8%, context = Coastal / Pacific Northwest / water-constrained, ready = 94.5%.

## Coupled or transitional cases
- Las Vegas: gap = 0.0 pp, LST-HI corr = 0.75, context = Inland / desert.
- New York: gap = 0.3 pp, LST-HI corr = 0.05, context = Coastal / megacity / dense core.
- Houston: gap = 0.4 pp, LST-HI corr = 0.34, context = Coastal / humid.
- Phoenix: gap = 4.2 pp, LST-HI corr = 0.29, context = Inland / desert.

## Robustness
The leave-one-out city-level pattern remains positive after removing each city. The coastal-minus-noncoastal difference ranges from 10.6 to 19.4 pp.

## Main caution
San Francisco is one of the strongest apparent-heat shift cases but has lower data readiness than most other cities. Therefore, it should be used as an important case, but the result should not depend only on San Francisco.

## Spatial morphology direction
- San Francisco: radial pattern = Cannot compare, HI-LST centroid distance = nan km, HI-only largest patch = 51.4%.
- Miami: radial pattern = HI-only more peripheral, HI-LST centroid distance = 5.4 km, HI-only largest patch = 100.0%.
- Boston: radial pattern = HI-only more peripheral, HI-LST centroid distance = 8.3 km, HI-only largest patch = 95.0%.
- Atlanta: radial pattern = HI-only more peripheral, HI-LST centroid distance = 9.8 km, HI-only largest patch = 100.0%.
- Seattle: radial pattern = HI-only more central, HI-LST centroid distance = 9.2 km, HI-only largest patch = 100.0%.

## Suggested paper framing
The paper should frame the result as a multi-city comparison of how LST and Heat Index identify different hotspot geographies. The strongest story is not simply that coastal cities are hotter, but that some coastal or water-influenced cities show a stronger apparent-heat hotspot signature that LST alone may miss.

## Suggested next action before writing
Before expanding to many more cities, use this 12-city audit to discuss the unit-of-analysis issue with the advisor: city-level pattern is strong, while tract-weighted pooled pattern is weaker. If the advisor agrees, the next expansion should be targeted by typology rather than random city addition.