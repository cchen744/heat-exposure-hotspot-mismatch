from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

project_root = Path.cwd()
figure_dir = project_root / "figures" / "pilot"
output_dir = project_root / "outputs" / "pilot"
figure_dir.mkdir(parents=True, exist_ok=True)
output_dir.mkdir(parents=True, exist_ok=True)

def draw_box(ax, x, y, title, text, facecolor):
    ax.text(
        x, y,
        f"{title}\n\n{text}",
        ha="center",
        va="center",
        fontsize=10.5,
        bbox=dict(
            boxstyle="round,pad=0.5",
            facecolor=facecolor,
            edgecolor="#4d4d4d",
            linewidth=1.2
        )
    )

def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="->",
            color="#444444",
            lw=1.6
        )
    )

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

ax.text(
    0.5, 0.96,
    "RQ1 workflow: comparing tract-level LST and Heat Index heat exposure",
    ha="center",
    va="top",
    fontsize=18,
    fontweight="bold"
)

draw_box(
    ax, 0.18, 0.78,
    "A. Study area + units",
    "Houston and Phoenix\nCensus tracts as analysis units\nTract-level spatial comparison",
    "#e8f1fb"
)

draw_box(
    ax, 0.50, 0.78,
    "B. Core heat inputs",
    "Summer Land Surface Temperature (LST)\nSummer Heat Index (HI)\nProcessed to tract-level values",
    "#fff1e6"
)

draw_box(
    ax, 0.82, 0.78,
    "C. Spatial harmonization",
    "Merge heat variables to tract geometries\nKeep valid geometry + available values\nCreate city-specific comparable layers",
    "#eef7ea"
)

draw_box(
    ax, 0.18, 0.46,
    "D. Hotspot definition",
    "Within each city and each measure\nDefine hotspots as top 20% of tracts\nSeparate thresholds for LST and HI",
    "#f7e8fb"
)

draw_box(
    ax, 0.50, 0.46,
    "E. Comparison framework",
    "Classify tracts into:\nOverlap hotspot\nLST-only hotspot\nHI-only hotspot\nNeither / Missing",
    "#fff7d6"
)

draw_box(
    ax, 0.82, 0.46,
    "F. Continuous interpretation",
    "Compute standardized gap:\nHI_z - LST_z\nPositive = humidity-sensitive heat stronger\nNegative = surface heat stronger",
    "#eaf4f4"
)

draw_box(
    ax, 0.50, 0.14,
    "G. Outputs for RQ1",
    "Original-value choropleth maps\nHotspot mismatch maps\nStandardized HI-LST gap maps\nCity summary tables + results notes",
    "#f2f2f2"
)

draw_arrow(ax, 0.28, 0.78, 0.40, 0.78)
draw_arrow(ax, 0.60, 0.78, 0.72, 0.78)

draw_arrow(ax, 0.18, 0.70, 0.18, 0.54)
draw_arrow(ax, 0.50, 0.70, 0.50, 0.57)
draw_arrow(ax, 0.82, 0.70, 0.82, 0.54)

draw_arrow(ax, 0.28, 0.46, 0.40, 0.46)
draw_arrow(ax, 0.60, 0.46, 0.72, 0.46)

draw_arrow(ax, 0.50, 0.36, 0.50, 0.22)

ax.text(
    0.5, 0.02,
    "Hotspots are defined separately within each city and each measure as the top 20% of tracts.",
    ha="center",
    va="bottom",
    fontsize=10,
    color="#333333"
)

workflow_fig_out = figure_dir / "rq1_methods_workflow_figure_terminal.png"
plt.savefig(workflow_fig_out, dpi=300, bbox_inches="tight")
plt.close(fig)

workflow_caption = """# RQ1 workflow figure caption

Figure X. Workflow for tract-level comparison of Land Surface Temperature (LST) and Heat Index (HI) in Houston and Phoenix. Summer LST and HI were harmonized to census-tract geometries and analyzed at the tract level. Within each city and each measure, hotspots were defined as the top 20% of tracts. Tracts were then classified into overlap hotspots, LST-only hotspots, HI-only hotspots, neither, or missing. To support interpretation beyond hotspot overlap, a standardized HI−LST gap was also computed to show where humidity-sensitive heat is relatively stronger or weaker than surface heat. Final outputs include original-value choropleth maps, hotspot mismatch maps, standardized gap maps, and city-level summary tables.
"""

workflow_caption_out = output_dir / "rq1_methods_workflow_caption_terminal.md"
workflow_caption_out.write_text(workflow_caption, encoding="utf-8")

print("DONE")
print(workflow_fig_out)
print(workflow_caption_out)
