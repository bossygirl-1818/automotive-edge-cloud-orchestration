import time
import sqlite3
import pandas as pd

from prometheus_client import Gauge, start_http_server


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "explainable_orchestration_history"


xai_total_records = Gauge(
    "xai_total_records",
    "Total explainable orchestration records"
)

xai_edge_decisions = Gauge(
    "xai_edge_decisions",
    "Total EDGE decisions in XAI history"
)

xai_cloud_decisions = Gauge(
    "xai_cloud_decisions",
    "Total CLOUD decisions in XAI history"
)

xai_vehicle_decisions = Gauge(
    "xai_vehicle_decisions",
    "Total VEHICLE decisions in XAI history"
)

xai_average_battery = Gauge(
    "xai_average_battery",
    "Average battery level in XAI history"
)

xai_average_speed = Gauge(
    "xai_average_speed",
    "Average speed in XAI history"
)


def update_metrics():
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    conn.close()

    if df.empty:
        return

    xai_total_records.set(len(df))

    decision_counts = df["decision"].value_counts()

    xai_edge_decisions.set(decision_counts.get("EDGE", 0))
    xai_cloud_decisions.set(decision_counts.get("CLOUD", 0))
    xai_vehicle_decisions.set(decision_counts.get("VEHICLE", 0))

    xai_average_battery.set(df["battery"].mean())
    xai_average_speed.set(df["speed"].mean())

    print(
        f"XAI metrics updated | "
        f"Records={len(df)} | "
        f"EDGE={decision_counts.get('EDGE', 0)} | "
        f"CLOUD={decision_counts.get('CLOUD', 0)} | "
        f"VEHICLE={decision_counts.get('VEHICLE', 0)}"
    )


def run_server():
    start_http_server(8007)

    print(
        "XAI Prometheus metrics running on "
        "http://localhost:8007/metrics"
    )

    while True:
        update_metrics()
        time.sleep(5)


if __name__ == "__main__":
    run_server()