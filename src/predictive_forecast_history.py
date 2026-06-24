import sqlite3
import pandas as pd
from datetime import datetime


DB_PATH = "data/orchestrator.db"
FORECAST_FILE = "data/predictive_traffic_forecast.csv"


def create_forecast_history_table():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictive_forecast_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,

            congestion_score REAL,
            congestion_level TEXT,

            edge_load REAL,
            edge_risk TEXT,

            cloud_latency REAL,
            cloud_risk TEXT,

            battery_drain REAL,
            battery_risk TEXT
        )
    """)

    conn.commit()
    conn.close()


def store_forecast_history():

    create_forecast_history_table()

    df = pd.read_csv(FORECAST_FILE)
    row = df.iloc[0]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictive_forecast_history (
            timestamp,

            congestion_score,
            congestion_level,

            edge_load,
            edge_risk,

            cloud_latency,
            cloud_risk,

            battery_drain,
            battery_risk
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        row["predicted_congestion_score"],
        row["predicted_congestion_level"],

        row["predicted_edge_load"],
        row["predicted_edge_risk"],

        row["predicted_cloud_latency"],
        row["predicted_cloud_risk"],

        row["predicted_battery_drain"],
        row["predicted_battery_risk"]
    ))

    conn.commit()
    conn.close()

    print("Predictive forecast stored in history table successfully.")


if __name__ == "__main__":
    store_forecast_history()