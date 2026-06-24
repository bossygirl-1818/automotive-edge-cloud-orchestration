import os
import sqlite3
import pandas as pd
import plotly.express as px


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "self_adaptive_history"
OUTPUT_DIR = "data/self_adaptive_visualizations"


def generate_self_adaptive_visualizations():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    conn.close()

    if df.empty:
        print("No self-adaptive history found.")
        return

    rl_counts = df["rl_decision"].value_counts().reset_index()
    rl_counts.columns = ["Decision", "Count"]

    fig1 = px.pie(
        rl_counts,
        names="Decision",
        values="Count",
        title="RL Decision Distribution",
        hole=0.55
    )

    final_counts = df["final_decision"].value_counts().reset_index()
    final_counts.columns = ["Decision", "Count"]

    fig2 = px.pie(
        final_counts,
        names="Decision",
        values="Count",
        title="Final Adaptive Decision Distribution",
        hole=0.55
    )

    df["override_status"] = df.apply(
        lambda row: "OVERRIDDEN" if row["rl_decision"] != row["final_decision"] else "ACCEPTED",
        axis=1
    )

    override_counts = df["override_status"].value_counts().reset_index()
    override_counts.columns = ["Status", "Count"]

    fig3 = px.bar(
        override_counts,
        x="Status",
        y="Count",
        title="RL Decision Override Analysis"
    )

    reason_counts = df["adaptation_reason"].value_counts().head(10).reset_index()
    reason_counts.columns = ["Adaptation Reason", "Count"]

    fig4 = px.bar(
        reason_counts,
        x="Count",
        y="Adaptation Reason",
        title="Top Adaptation Reasons",
        orientation="h"
    )

    charts = {
        "rl_decision_distribution.html": fig1,
        "final_decision_distribution.html": fig2,
        "override_analysis.html": fig3,
        "adaptation_reason_analysis.html": fig4
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

    print("\nSelf-adaptive visualizations generated successfully.")
    print("Saved to:")
    print(OUTPUT_DIR)


if __name__ == "__main__":
    generate_self_adaptive_visualizations()