import time
import pandas as pd

from prometheus_client import Gauge, start_http_server


FORECAST_FILE = "data/predictive_traffic_forecast.csv"


predictive_congestion_score = Gauge(
    "predictive_congestion_score",
    "Predicted traffic congestion score"
)

predictive_edge_load = Gauge(
    "predictive_edge_load",
    "Predicted edge server load"
)

predictive_cloud_latency = Gauge(
    "predictive_cloud_latency",
    "Predicted cloud latency"
)

predictive_battery_drain = Gauge(
    "predictive_battery_drain",
    "Predicted vehicle battery drain"
)


def update_metrics():

    df = pd.read_csv(FORECAST_FILE)
    row = df.iloc[0]

    predictive_congestion_score.set(row["predicted_congestion_score"])
    predictive_edge_load.set(row["predicted_edge_load"])
    predictive_cloud_latency.set(row["predicted_cloud_latency"])
    predictive_battery_drain.set(row["predicted_battery_drain"])

    print(
        "Predictive traffic metrics updated | "
        f"Congestion={row['predicted_congestion_score']} | "
        f"Edge={row['predicted_edge_load']} | "
        f"Cloud={row['predicted_cloud_latency']} | "
        f"Battery={row['predicted_battery_drain']}"
    )


def run_server():

    start_http_server(8005)

    print("Predictive Traffic Prometheus metrics running on http://localhost:8005/metrics")

    while True:
        update_metrics()
        time.sleep(5)


if __name__ == "__main__":
    run_server()