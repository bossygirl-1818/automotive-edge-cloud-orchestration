import os
import sqlite3
import pandas as pd
import plotly.express as px


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "predictive_forecast_history"
OUTPUT_DIR = "data/predictive_forecast_visualizations"


def generate_predictive_forecast_visualizations():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    conn.close()

    if df.empty:
        print("No forecast history found.")
        print("Run: python -m src.predictive_forecast_history")
        return

    charts = {
        "congestion_score_trend.html": px.line(
            df,
            x="timestamp",
            y="congestion_score",
            title="Predicted Congestion Score Over Time"
        ),

        "edge_load_trend.html": px.line(
            df,
            x="timestamp",
            y="edge_load",
            title="Predicted Edge Load Over Time"
        ),

        "cloud_latency_trend.html": px.line(
            df,
            x="timestamp",
            y="cloud_latency",
            title="Predicted Cloud Latency Over Time"
        ),

        "battery_drain_trend.html": px.line(
            df,
            x="timestamp",
            y="battery_drain",
            title="Predicted Battery Drain Over Time"
        )
    }

    for filename, fig in charts.items():
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#020617",
            plot_bgcolor="#020617",
            font=dict(color="#ffffff", size=15),
            height=430
        )

        fig.write_html(
            os.path.join(OUTPUT_DIR, filename)
        )

    print("Predictive forecast visualizations generated successfully.")
    print(f"Saved inside: {OUTPUT_DIR}")


if __name__ == "__main__":
    generate_predictive_forecast_visualizations()