import sqlite3
import time

from prometheus_client import Gauge, start_http_server


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "advanced_traffic_tasks"


advanced_traffic_total_records = Gauge(
    "advanced_traffic_total_records",
    "Total advanced traffic orchestration records"
)

advanced_traffic_vehicle_count = Gauge(
    "advanced_traffic_vehicle_count",
    "Number of vehicles in advanced traffic dataset"
)

advanced_traffic_average_speed = Gauge(
    "advanced_traffic_average_speed",
    "Average vehicle speed in advanced traffic orchestration"
)

advanced_traffic_average_battery = Gauge(
    "advanced_traffic_average_battery",
    "Average battery level in advanced traffic orchestration"
)

advanced_traffic_edge_tasks = Gauge(
    "advanced_traffic_edge_tasks",
    "Advanced traffic tasks offloaded to EDGE"
)

advanced_traffic_cloud_tasks = Gauge(
    "advanced_traffic_cloud_tasks",
    "Advanced traffic tasks offloaded to CLOUD"
)

advanced_traffic_vehicle_tasks = Gauge(
    "advanced_traffic_vehicle_tasks",
    "Advanced traffic tasks executed on VEHICLE"
)


def fetch_metrics():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    total_records = cursor.fetchone()[0]

    cursor.execute(f"SELECT COUNT(DISTINCT vehicle_id) FROM {TABLE_NAME}")
    vehicle_count = cursor.fetchone()[0]

    cursor.execute(f"SELECT AVG(speed) FROM {TABLE_NAME}")
    avg_speed = cursor.fetchone()[0] or 0

    cursor.execute(f"SELECT AVG(battery) FROM {TABLE_NAME}")
    avg_battery = cursor.fetchone()[0] or 0

    cursor.execute(f"""
        SELECT decision, COUNT(*)
        FROM {TABLE_NAME}
        GROUP BY decision
    """)

    decision_counts = dict(cursor.fetchall())

    conn.close()

    return {
        "total_records": total_records,
        "vehicle_count": vehicle_count,
        "avg_speed": avg_speed,
        "avg_battery": avg_battery,
        "edge_tasks": decision_counts.get("EDGE", 0),
        "cloud_tasks": decision_counts.get("CLOUD", 0),
        "vehicle_tasks": decision_counts.get("VEHICLE", 0)
    }


def update_metrics():

    metrics = fetch_metrics()

    advanced_traffic_total_records.set(metrics["total_records"])
    advanced_traffic_vehicle_count.set(metrics["vehicle_count"])
    advanced_traffic_average_speed.set(metrics["avg_speed"])
    advanced_traffic_average_battery.set(metrics["avg_battery"])
    advanced_traffic_edge_tasks.set(metrics["edge_tasks"])
    advanced_traffic_cloud_tasks.set(metrics["cloud_tasks"])
    advanced_traffic_vehicle_tasks.set(metrics["vehicle_tasks"])

    print(
        "Advanced traffic metrics updated | "
        f"Records={metrics['total_records']} | "
        f"Vehicles={metrics['vehicle_count']} | "
        f"Speed={metrics['avg_speed']:.2f}"
    )


def run_server():

    start_http_server(8002)

    print(
        "Advanced Traffic Prometheus metrics running on "
        "http://localhost:8002/metrics"
    )

    while True:
        update_metrics()
        time.sleep(5)


if __name__ == "__main__":
    run_server()