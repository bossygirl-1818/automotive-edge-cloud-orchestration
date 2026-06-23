import sqlite3
import time

from prometheus_client import Gauge, start_http_server


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "digital_twin_states"


digital_twin_total_states = Gauge(
    "digital_twin_total_states",
    "Total digital twin states stored"
)

digital_twin_average_vehicle_speed = Gauge(
    "digital_twin_average_vehicle_speed",
    "Average vehicle speed from digital twin states"
)

digital_twin_average_vehicle_battery = Gauge(
    "digital_twin_average_vehicle_battery",
    "Average vehicle battery from digital twin states"
)

digital_twin_average_edge_cpu = Gauge(
    "digital_twin_average_edge_cpu",
    "Average edge CPU load from digital twin states"
)

digital_twin_average_cloud_latency = Gauge(
    "digital_twin_average_cloud_latency",
    "Average cloud latency from digital twin states"
)

digital_twin_active_vehicles = Gauge(
    "digital_twin_active_vehicles",
    "Latest active vehicles from road twin"
)


def fetch_digital_twin_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    total_states = cursor.fetchone()[0]

    cursor.execute(f"SELECT AVG(vehicle_speed) FROM {TABLE_NAME}")
    avg_vehicle_speed = cursor.fetchone()[0] or 0

    cursor.execute(f"SELECT AVG(vehicle_battery) FROM {TABLE_NAME}")
    avg_vehicle_battery = cursor.fetchone()[0] or 0

    cursor.execute(f"SELECT AVG(edge_cpu_load) FROM {TABLE_NAME}")
    avg_edge_cpu = cursor.fetchone()[0] or 0

    cursor.execute(f"SELECT AVG(cloud_latency_ms) FROM {TABLE_NAME}")
    avg_cloud_latency = cursor.fetchone()[0] or 0

    cursor.execute(f"""
        SELECT active_vehicles
        FROM {TABLE_NAME}
        ORDER BY id DESC
        LIMIT 1
    """)
    latest_active_vehicles = cursor.fetchone()
    latest_active_vehicles = latest_active_vehicles[0] if latest_active_vehicles else 0

    conn.close()

    return {
        "total_states": total_states,
        "avg_vehicle_speed": avg_vehicle_speed,
        "avg_vehicle_battery": avg_vehicle_battery,
        "avg_edge_cpu": avg_edge_cpu,
        "avg_cloud_latency": avg_cloud_latency,
        "active_vehicles": latest_active_vehicles
    }


def update_metrics():
    metrics = fetch_digital_twin_metrics()

    digital_twin_total_states.set(metrics["total_states"])
    digital_twin_average_vehicle_speed.set(metrics["avg_vehicle_speed"])
    digital_twin_average_vehicle_battery.set(metrics["avg_vehicle_battery"])
    digital_twin_average_edge_cpu.set(metrics["avg_edge_cpu"])
    digital_twin_average_cloud_latency.set(metrics["avg_cloud_latency"])
    digital_twin_active_vehicles.set(metrics["active_vehicles"])

    print(
        "Digital Twin metrics updated | "
        f"States={metrics['total_states']} | "
        f"Speed={metrics['avg_vehicle_speed']:.2f} | "
        f"Edge CPU={metrics['avg_edge_cpu']:.2f}"
    )


def run_server():
    start_http_server(8004)

    print("Digital Twin Prometheus metrics running on http://localhost:8004/metrics")

    while True:
        update_metrics()
        time.sleep(5)


if __name__ == "__main__":
    run_server()