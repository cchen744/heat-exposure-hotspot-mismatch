# Twelve-city paper robustness notes

## Main finding
Across the 12-city comparison, Heat Index and LST do not identify the same hotspot geographies. The strongest apparent-heat shifts occur in several coastal or water-influenced cities, while inland desert cities are more coupled or transitional.

## Evidence 1: strongest HI-shift cities
- San Francisco: HI-only = 53.2%, LST-only = 0.0%, HI-LST hotspot gap = 53.2 pp, context = Coastal / compact / bay-influenced.
- Miami: HI-only = 52.0%, LST-only = 2.4%, HI-LST hotspot gap = 49.6 pp, context = Coastal / humid.
- Boston: HI-only = 47.6%, LST-only = 11.5%, HI-LST hotspot gap = 36.1 pp, context = Coastal / temperate.
- Atlanta: HI-only = 32.3%, LST-only = 18.4%, HI-LST hotspot gap = 13.9 pp, context = Inland / humid / sprawling Sun Belt.
- Seattle: HI-only = 33.0%, LST-only = 21.8%, HI-LST hotspot gap = 11.2 pp, context = Coastal / Pacific Northwest / water-constrained.

## Evidence 2: context gradient
- Coastal / water-influenced: mean HI-LST hotspot gap = 22.7 pp across 7 cities: Houston, Los Angeles, Miami, Boston, New York, Seattle, San Francisco.
- Great Lakes: mean HI-LST hotspot gap = 11.0 pp across 1 cities: Chicago.
- Inland Sun Belt: mean HI-LST hotspot gap = 10.0 pp across 2 cities: Atlanta, Dallas.
- Inland desert: mean HI-LST hotspot gap = 2.1 pp across 2 cities: Phoenix, Las Vegas.

## Evidence 3: robustness
Leave-one-out test: after removing each city one at a time, the coastal/water-influenced minus non-coastal HI-shift difference ranges from 10.6 to 19.4 percentage points.
This means the context-gradient pattern is not driven by a single city.

## Evidence 4: most useful paper contrasts
- San Francisco vs Las Vegas: HI-shift difference = 53.2 pp. San Francisco = Strong HI-shift; Las Vegas = Coupled LST-HI.
- Miami vs Houston: HI-shift difference = 49.2 pp. Miami = Strong HI-shift; Houston = Mixed / transitional.
- San Francisco vs Phoenix: HI-shift difference = 49.0 pp. San Francisco = Strong HI-shift; Phoenix = Mixed / transitional.
- Miami vs Phoenix: HI-shift difference = 45.4 pp. Miami = Strong HI-shift; Phoenix = Mixed / transitional.
- Boston vs New York: HI-shift difference = 35.8 pp. Boston = Strong HI-shift; New York = Mixed / transitional.
- Chicago vs Las Vegas: HI-shift difference = 11.0 pp. Chicago = Moderate HI-shift; Las Vegas = Coupled LST-HI.

## Suggested paper framing
A strong framing is that LST-based urban heat mapping may under-detect apparent-heat risk in humid, coastal, or water-influenced cities. The paper can argue that multi-city comparison reveals city-type-specific mismatch mechanisms between surface heat and human-experienced heat.

## Caution
Because this is currently a 12-city analysis, claims should be framed as comparative/descriptive evidence rather than causal proof. The next step should expand the city sample and test whether the coastal/water-influenced gradient remains stable.