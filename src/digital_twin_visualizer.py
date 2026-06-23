import os
import sqlite3
import pandas as pd
import plotly.express as px


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "digital_twin_states"
OUTPUT_DIR = "data/digital_twin_visualizations"


def generate_digital_twin_visualizations():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )
    conn.close()

    if df.empty:
        print("No digital twin data found.")
        print("Run: python -m src.digital_twin_db_loader")
        return

    charts = {
        "vehicle_health_distribution.html": px.pie(
            df["vehicle_health_status"].value_counts().reset_index(),
            names="vehicle_health_status",
            values="count",
            title="Vehicle Health Status Distribution",
            hole=0.55
        ),

        "traffic_density_distribution.html": px.pie(
            df["traffic_density"].value_counts().reset_index(),
            names="traffic_density",
            values="count",
            title="Traffic Density Distribution",
            hole=0.55
        ),

        "congestion_distribution.html": px.pie(
            df["congestion_level"].value_counts().reset_index(),
            names="congestion_level",
            values="count",
            title="Congestion Level Distribution",
            hole=0.55
        ),

        "vehicle_speed_trend.html": px.line(
            df,
            x="timestamp",
            y="vehicle_speed",
            title="Vehicle Speed Trend"
        ),

        "edge_cpu_trend.html": px.line(
            df,
            x="timestamp",
            y="edge_cpu_load",
            title="Edge CPU Load Trend"
        ),

        "cloud_latency_trend.html": px.line(
            df,
            x="timestamp",
            y="cloud_latency_ms",
            title="Cloud Latency Trend"
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

    print("Digital twin visualizations generated successfully.")
    print(f"Saved inside: {OUTPUT_DIR}")


if __name__ == "__main__":
    generate_digital_twin_visualizations()