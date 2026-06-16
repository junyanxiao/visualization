"""Assignment 3 visualizations using Toronto KSI collision data.

Dataset: City of Toronto Open Data, "Motor Vehicle Collisions Involving
Killed or Seriously Injured Persons".
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go


DATA_URL = (
    "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/"
    "73a8e475-9683-42e1-ac06-b8690dcba062/resource/"
    "b95f5270-4eb0-40c2-917d-37fb494328a1/download/"
    "motor-vehicle-collisions-with-ksi-data-4326.csv"
)

OUTPUT_DIR = Path(__file__).parent
FIG1_PATH = OUTPUT_DIR / "visualization_1_python_matplotlib.png"
FIG2_STATIC_PATH = OUTPUT_DIR / "visualization_2_plotly_static.png"
FIG2_HTML_PATH = OUTPUT_DIR / "visualization_2_plotly.html"


def load_collision_data() -> pd.DataFrame:
    """Load the public CSV and prepare date fields."""
    df = pd.read_csv(DATA_URL)
    df["accdate"] = pd.to_datetime(df["accdate"], errors="coerce")
    df["year"] = df["accdate"].dt.year
    return df


def make_event_level_data(df: pd.DataFrame) -> pd.DataFrame:
    """Collapse person-level rows to one row per collision event."""
    event_fields = [
        "collision_id",
        "accdate",
        "year",
        "acclass",
        "longitude",
        "latitude",
        "wardname",
        "neighbourhood",
        "road_class",
        "light",
        "rdsfcond",
    ]
    flag_fields = [
        "aggressive",
        "distracted",
        "cyclist",
        "motorcyclist",
        "other_micromobility",
        "older_adult",
        "pedestrian",
        "red_light",
        "school_child",
        "heavy_truck",
    ]

    events = (
        df[event_fields]
        .sort_values(["collision_id", "accdate"])
        .drop_duplicates("collision_id")
        .set_index("collision_id")
    )
    flags = (
        df[["collision_id", *flag_fields]]
        .replace({"true": True, "false": False, "True": True, "False": False})
        .fillna(False)
        .astype({field: bool for field in flag_fields})
        .groupby("collision_id")
        .any()
    )
    fatal_by_collision = (
        df.groupby("collision_id")["acclass"]
        .apply(lambda classes: classes.fillna("").str.startswith("Fatal").any())
        .rename("is_fatal")
    )
    events = events.join(flags, how="left").reset_index()
    events = events.join(fatal_by_collision, on="collision_id")
    events["severity"] = events["is_fatal"].map(
        {True: "Fatal", False: "Serious injury"}
    )
    events["vulnerable_road_user"] = events[
        ["pedestrian", "cyclist", "motorcyclist", "other_micromobility"]
    ].any(axis=1)
    return events


def last_complete_year(events: pd.DataFrame) -> int:
    """Return the last full calendar year in the current data extract."""
    latest_date = events["accdate"].max()
    if latest_date.month == 12 and latest_date.day == 31:
        return int(latest_date.year)
    return int(latest_date.year - 1)


def plot_annual_trend(events: pd.DataFrame, complete_year: int) -> None:
    """Create a Matplotlib stacked bar chart of annual KSI collision events."""
    trend = events.query("2006 <= year <= @complete_year")
    annual = (
        trend.groupby(["year", "severity"])
        .size()
        .unstack(fill_value=0)
        .reindex(columns=["Serious injury", "Fatal"], fill_value=0)
    )

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.subplots_adjust(top=0.82, bottom=0.16, left=0.08, right=0.98)
    colors = {"Serious injury": "#0072B2", "Fatal": "#D55E00"}

    ax.bar(
        annual.index,
        annual["Serious injury"],
        color=colors["Serious injury"],
        label="Serious injury collision",
    )
    ax.bar(
        annual.index,
        annual["Fatal"],
        bottom=annual["Serious injury"],
        color=colors["Fatal"],
        label="Fatal collision",
    )

    total_latest = int(annual.loc[complete_year].sum())
    total_peak_year = int(annual.sum(axis=1).idxmax())
    total_peak = int(annual.sum(axis=1).max())

    fig.suptitle(
        "Toronto KSI collision events remain below their 2006 peak",
        fontsize=17,
        y=0.96,
    )
    fig.text(
        0.08,
        0.89,
        f"Unique collisions involving a killed or seriously injured person, 2006-{complete_year}",
        fontsize=11,
        color="#4A4A4A",
    )
    ax.annotate(
        f"Peak: {total_peak} events",
        xy=(total_peak_year, total_peak),
        xytext=(total_peak_year + 0.6, total_peak + 22),
        arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 1.2},
        fontsize=10,
    )
    ax.annotate(
        f"{complete_year}: {total_latest} events",
        xy=(complete_year, total_latest),
        xytext=(complete_year - 4.5, total_latest + 45),
        arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 1.2},
        fontsize=10,
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Number of unique KSI collision events")
    ax.set_xticks(list(range(2006, complete_year + 1, 2)))
    ax.legend(frameon=False, loc="upper right")
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(
        0,
        -0.14,
        "Source: City of Toronto Open Data. 2026 is excluded because it is a partial year.",
        transform=ax.transAxes,
        fontsize=9,
        color="#555555",
    )

    fig.savefig(FIG1_PATH, dpi=220)
    plt.close(fig)


def plot_recent_neighbourhoods(events: pd.DataFrame, complete_year: int) -> None:
    """Create a Plotly HTML chart and a static PNG counterpart."""
    start_year = complete_year - 4
    recent = events.query("@start_year <= year <= @complete_year").copy()
    recent["road_user_group"] = recent["vulnerable_road_user"].map(
        {True: "Pedestrian, cyclist, motorcyclist, or micromobility involved", False: "Other KSI collision event"}
    )

    top_neighbourhoods = (
        recent.groupby("neighbourhood")
        .size()
        .sort_values(ascending=False)
        .head(12)
        .index
    )
    neighbourhood_counts = (
        recent[recent["neighbourhood"].isin(top_neighbourhoods)]
        .groupby(["neighbourhood", "road_user_group"])
        .size()
        .unstack(fill_value=0)
    )
    neighbourhood_counts["total"] = neighbourhood_counts.sum(axis=1)
    neighbourhood_counts = neighbourhood_counts.sort_values("total")

    categories = neighbourhood_counts.index.tolist()
    vulnerable = neighbourhood_counts[
        "Pedestrian, cyclist, motorcyclist, or micromobility involved"
    ].tolist()
    other = neighbourhood_counts["Other KSI collision event"].tolist()

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            y=categories,
            x=vulnerable,
            name="Vulnerable road user involved",
            orientation="h",
            marker={"color": "#009E73"},
            hovertemplate="%{y}<br>%{x} events<extra></extra>",
        )
    )
    fig.add_trace(
        go.Bar(
            y=categories,
            x=other,
            name="Other KSI event",
            orientation="h",
            marker={"color": "#CC79A7"},
            hovertemplate="%{y}<br>%{x} events<extra></extra>",
        )
    )
    fig.update_layout(
        title=(
            "Top Toronto neighbourhoods for KSI collision events, "
            f"{start_year}-{complete_year}"
        ),
        barmode="stack",
        xaxis_title="Number of unique KSI collision events",
        yaxis_title="Neighbourhood",
        template="plotly_white",
        width=1100,
        height=760,
        legend_title_text="Collision context",
        margin={"l": 260, "r": 40, "t": 90, "b": 70},
        font={"family": "Arial", "size": 14},
    )
    fig.add_annotation(
        text="Source: City of Toronto Open Data. Counts use one row per collision event, not one row per person.",
        xref="paper",
        yref="paper",
        x=0,
        y=-0.12,
        showarrow=False,
        align="left",
        font={"size": 12, "color": "#555555"},
    )
    fig.write_html(FIG2_HTML_PATH, include_plotlyjs="cdn")

    plt.style.use("seaborn-v0_8-whitegrid")
    static_fig, ax = plt.subplots(figsize=(12, 8), constrained_layout=True)
    ax.barh(categories, vulnerable, color="#009E73", label="Vulnerable road user involved")
    ax.barh(
        categories,
        other,
        left=vulnerable,
        color="#CC79A7",
        label="Other KSI event",
    )
    ax.set_title(
        f"Top Toronto neighbourhoods for KSI collision events, {start_year}-{complete_year}",
        fontsize=16,
        pad=16,
    )
    ax.set_xlabel("Number of unique KSI collision events")
    ax.set_ylabel("Neighbourhood")
    ax.legend(frameon=False, loc="lower right")
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(
        0,
        -0.11,
        "Source: City of Toronto Open Data. Static export of the Plotly visualization.",
        transform=ax.transAxes,
        fontsize=9,
        color="#555555",
    )
    static_fig.savefig(FIG2_STATIC_PATH, dpi=220)
    plt.close(static_fig)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = load_collision_data()
    events = make_event_level_data(df)
    complete_year = last_complete_year(events)

    plot_annual_trend(events, complete_year)
    plot_recent_neighbourhoods(events, complete_year)

    print(f"Created {FIG1_PATH}")
    print(f"Created {FIG2_HTML_PATH}")
    print(f"Created {FIG2_STATIC_PATH}")


if __name__ == "__main__":
    main()
