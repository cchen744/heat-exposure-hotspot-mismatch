# RQ1 paper-ready results notes

## Core result
This analysis compares Land Surface Temperature (LST) and Heat Index (HI) at the tract level in Houston and Phoenix.

## Main findings
- In Houston, the hotspot overlap between LST and HI is limited rather than complete. The Jaccard index is 0.199, and overlap hotspots account for 6.9% of tracts with both measures.
- In Houston, LST-only hotspots account for 8.2% of valid tracts, while HI-only hotspots account for 19.7%. This suggests that the two measures capture partly different heat-risk areas.
- In Phoenix, the hotspot overlap is also incomplete. The Jaccard index is 0.264, and overlap hotspots account for 8.7% of tracts with both measures.
- In Phoenix, LST-only hotspots account for 11.1% of valid tracts, while HI-only hotspots account for 13.3% of valid tracts.
- The median standardized HI−LST gap is 0.06 in Houston and 0.01 in Phoenix. Positive values indicate places where humidity-sensitive heat exposure is stronger relative to surface heat.

## Interpretation
- LST alone does not fully reproduce the spatial pattern of HI-defined heat exposure.
- The mismatch between LST-only and HI-only hotspots supports the main RQ1 argument that humidity matters for identifying heat-risk areas.
- The original-value choropleth maps show the broad spatial distribution of each variable, while the hotspot mismatch map directly identifies where the two measures agree and differ.
- The standardized HI−LST gap map provides an additional interpretation layer by showing where humidity-sensitive heat is relatively stronger or weaker.

## Method note
- Hotspots are defined separately within each city and each measure as the top 20% of tracts.
- The hotspot overlap metric is summarized using the Jaccard index:
  Jaccard = overlap / (overlap + LST-only + HI-only)

