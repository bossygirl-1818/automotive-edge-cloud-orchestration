import os
import sqlite3
import pandas as pd
import plotly.express as px


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "explainable_orchestration_history"
OUTPUT_DIR = "data/xai_visualizations"


def generate_xai_visualizations():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    conn.close()

    if df.empty:
        print("No XAI history found.")
        return

    decision_counts = (
        df["decision"]
        .value_counts()
        .reset_index()
    )
    decision_counts.columns = ["Decision", "Count"]

    fig1 = px.pie(
        decision_counts,
        names="Decision",
        values="Count",
        title="Decision Distribution"
    )

    fig1.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617"
    )

    fig1.write_html(
        os.path.join(
            OUTPUT_DIR,
            "decision_distribution.html"
        )
    )

    traffic_counts = (
        df["traffic_density"]
        .value_counts()
        .reset_index()
    )
    traffic_counts.columns = [
        "Traffic Density",
        "Count"
    ]

    fig2 = px.bar(
        traffic_counts,
        x="Traffic Density",
        y="Count",
        title="Traffic Density Distribution"
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617"
    )

    fig2.write_html(
        os.path.join(
            OUTPUT_DIR,
            "traffic_density_distribution.html"
        )
    )

    fig3 = px.histogram(
        df,
        x="battery",
        nbins=15,
        title="Battery Distribution"
    )

    fig3.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617"
    )

    fig3.write_html(
        os.path.join(
            OUTPUT_DIR,
            "battery_distribution.html"
        )
    )

    fig4 = px.histogram(
        df,
        x="speed",
        nbins=15,
        title="Vehicle Speed Distribution"
    )

    fig4.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617"
    )

    fig4.write_html(
        os.path.join(
            OUTPUT_DIR,
            "speed_distribution.html"
        )
    )

    print("\nXAI visualizations generated successfully.")
    print("Saved to:")
    print(OUTPUT_DIR)


if __name__ == "__main__":
    generate_xai_visualizations()