import sqlite3
import pandas as pd


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "predictive_forecast_history"


def run_predictive_forecast_analytics():

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

    print("\n===== PREDICTIVE FORECAST HISTORY ANALYTICS =====\n")

    print("Total Forecast Records:", len(df))

    print("\nAverage Scores:")
    print("Average Congestion Score:", round(df["congestion_score"].mean(), 2))
    print("Average Edge Load:", round(df["edge_load"].mean(), 2))
    print("Average Cloud Latency:", round(df["cloud_latency"].mean(), 2))
    print("Average Battery Drain:", round(df["battery_drain"].mean(), 2))

    print("\nCongestion Risk Distribution:")
    print(df["congestion_level"].value_counts())

    print("\nEdge Risk Distribution:")
    print(df["edge_risk"].value_counts())

    print("\nCloud Risk Distribution:")
    print(df["cloud_risk"].value_counts())

    print("\nBattery Risk Distribution:")
    print(df["battery_risk"].value_counts())


if __name__ == "__main__":
    run_predictive_forecast_analytics()