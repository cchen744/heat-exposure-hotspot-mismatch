# RQ1 new-city onboarding note

Current batch-ready cities:
- Houston
- Phoenix

Core target schema for any new city:
- GEOID
- lst_c
- hi_c
- total_population
- geometry

Recommended onboarding rule:
Prepare one merged tract-level GPKG per city that already contains the core target schema above. This is the most stable and scalable path for the multicity workflow.
