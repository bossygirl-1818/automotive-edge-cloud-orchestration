import os
import pandas as pd
import plotly.express as px


INPUT_FILE = "data/sumo_advanced_orchestration.csv"
OUTPUT_DIR = "data/advanced_traffic_visualizations"


def create_visualizations():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)

    charts = {
        "decision_distribution.html": px.pie(
            df["decision"].value_counts().reset_index(),
            names="decision",
            values="count",
            title="Advanced Traffic-Aware Offloading Decisions",
            hole=0.55
        ),

        "traffic_density_distribution.html": px.pie(
            df["traffic_density"].value_counts().reset_index(),
            names="traffic_density",
            values="count",
            title="Traffic Density Distribution",
            hole=0.55
        ),

        "network_quality_distribution.html": px.bar(
            df["network_quality"].value_counts().reset_index(),
            x="network_quality",
            y="count",
            title="Network Quality Distribution"
        ),

        "task_type_distribution.html": px.bar(
            df["task_type"].value_counts().reset_index(),
            x="task_type",
            y="count",
            title="Task Type Distribution"
        ),

        "average_speed_over_time.html": px.line(
            df.groupby("step")["speed"].mean().reset_index(),
            x="step",
            y="speed",
            title="Average Vehicle Speed Over Time"
        ),

        "average_battery_over_time.html": px.line(
            df.groupby("step")["battery"].mean().reset_index(),
            x="step",
            y="battery",
            title="Average Battery Level Over Time"
        )
    }

    for filename, fig in charts.items():
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#020617",
            plot_bgcolor="#020617",
            font=dict(color="#ffffff")
        )

        fig.write_html(
            os.path.join(OUTPUT_DIR, filename)
        )

    print("Advanced traffic visualizations generated successfully.")
    print(f"Saved inside: {OUTPUT_DIR}")


if __name__ == "__main__":
    create_visualizations()