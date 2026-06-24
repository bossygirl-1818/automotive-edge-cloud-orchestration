import time
import sqlite3
import pandas as pd

from prometheus_client import Gauge, start_http_server


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "predictive_forecast_history"


forecast_history_total_records = Gauge(
    "forecast_history_total_records",
    "Total forecast history records"
)

forecast_history_avg_congestion = Gauge(
    "forecast_history_avg_congestion",
    "Average forecast congestion score"
)

forecast_history_avg_edge_load = Gauge(
    "forecast_history_avg_edge_load",
    "Average forecast edge load"
)

forecast_history_avg_cloud_latency = Gauge(
    "forecast_history_avg_cloud_latency",
    "Average forecast cloud latency"
)

forecast_history_avg_battery_drain = Gauge(
    "forecast_history_avg_battery_drain",
    "Average forecast battery drain"
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

    forecast_history_total_records.set(len(df))
    forecast_history_avg_congestion.set(df["congestion_score"].mean())
    forecast_history_avg_edge_load.set(df["edge_load"].mean())
    forecast_history_avg_cloud_latency.set(df["cloud_latency"].mean())
    forecast_history_avg_battery_drain.set(df["battery_drain"].mean())

    print(
        f"Forecast History Updated | "
        f"Records={len(df)} | "
        f"Congestion={df['congestion_score'].mean():.2f}"
    )


def run_server():

    start_http_server(8006)

    print(
        "Forecast History Prometheus metrics running on "
        "http://localhost:8006/metrics"
    )

    while True:
        update_metrics()
        time.sleep(5)


if __name__ == "__main__":
    run_server()