import time
import sqlite3
import pandas as pd

from prometheus_client import Gauge, start_http_server


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "self_adaptive_history"


adaptive_total_records = Gauge(
    "adaptive_total_records",
    "Total self-adaptive controller records"
)

adaptive_override_count = Gauge(
    "adaptive_override_count",
    "Total adaptive overrides"
)

adaptive_override_rate = Gauge(
    "adaptive_override_rate",
    "Adaptive override percentage"
)

adaptive_edge_decisions = Gauge(
    "adaptive_edge_decisions",
    "Final EDGE decisions"
)

adaptive_cloud_decisions = Gauge(
    "adaptive_cloud_decisions",
    "Final CLOUD decisions"
)

adaptive_vehicle_decisions = Gauge(
    "adaptive_vehicle_decisions",
    "Final VEHICLE decisions"
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

    overrides = df[
        df["rl_decision"] != df["final_decision"]
    ]

    override_rate = (
        len(overrides) / len(df)
    ) * 100

    adaptive_total_records.set(len(df))
    adaptive_override_count.set(len(overrides))
    adaptive_override_rate.set(override_rate)

    decision_counts = (
        df["final_decision"]
        .value_counts()
    )

    adaptive_edge_decisions.set(
        decision_counts.get("EDGE", 0)
    )

    adaptive_cloud_decisions.set(
        decision_counts.get("CLOUD", 0)
    )

    adaptive_vehicle_decisions.set(
        decision_counts.get("VEHICLE", 0)
    )

    print(
        f"Adaptive Metrics Updated | "
        f"Records={len(df)} | "
        f"Override Rate={override_rate:.2f}%"
    )


def run_server():

    start_http_server(8008)

    print(
        "Adaptive Prometheus metrics running on "
        "http://localhost:8008/metrics"
    )

    while True:
        update_metrics()
        time.sleep(5)


if __name__ == "__main__":
    run_server()