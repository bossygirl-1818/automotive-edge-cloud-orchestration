from prometheus_client import Gauge, Counter, start_http_server
import time

from src.db_queries import get_telemetry, get_rl_rewards, get_decisions


vehicle_cpu_gauge = Gauge(
    "vehicle_cpu_usage",
    "Current vehicle CPU usage percentage"
)

battery_gauge = Gauge(
    "vehicle_battery_level",
    "Current vehicle battery level percentage"
)

edge_load_gauge = Gauge(
    "edge_server_load",
    "Current edge server load percentage"
)

cloud_load_gauge = Gauge(
    "cloud_server_load",
    "Current cloud server load percentage"
)

network_latency_gauge = Gauge(
    "network_latency_ms",
    "Current network latency in milliseconds"
)

average_reward_gauge = Gauge(
    "average_rl_reward",
    "Average reinforcement learning reward"
)

decision_counter = Counter(
    "orchestration_decisions_total",
    "Total orchestration decisions",
    ["decision"]
)


def update_metrics():
    telemetry_df = get_telemetry()
    reward_df = get_rl_rewards()
    decision_df = get_decisions()

    latest_telemetry = telemetry_df.iloc[-1]

    vehicle_cpu_gauge.set(latest_telemetry["vehicle_cpu"])
    battery_gauge.set(latest_telemetry["battery"])
    edge_load_gauge.set(latest_telemetry["edge_load"])
    cloud_load_gauge.set(latest_telemetry["cloud_load"])
    network_latency_gauge.set(latest_telemetry["network_latency"])

    average_reward_gauge.set(
        reward_df["reward"].mean()
    )

    if not decision_df.empty:
        latest_decision = decision_df.iloc[-1]["hybrid_decision"]
        decision_counter.labels(
            decision=latest_decision
        ).inc()


def run_metrics_server():
    start_http_server(8000)
    print("Prometheus metrics server running on http://localhost:8000/metrics")

    while True:
        update_metrics()
        time.sleep(5)


if __name__ == "__main__":
    run_metrics_server()