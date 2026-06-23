import sqlite3
import time

from prometheus_client import Gauge, start_http_server


DB_PATH = "data/orchestrator.db"


sumo_total_tasks = Gauge(
    "sumo_total_tasks",
    "Total SUMO orchestration tasks"
)

sumo_vehicle_count = Gauge(
    "sumo_vehicle_count",
    "Number of unique SUMO vehicles"
)

sumo_average_speed = Gauge(
    "sumo_average_speed",
    "Average SUMO vehicle speed"
)

sumo_average_battery = Gauge(
    "sumo_average_battery",
    "Average SUMO vehicle battery level"
)

sumo_edge_tasks = Gauge(
    "sumo_edge_tasks",
    "Total SUMO tasks offloaded to EDGE"
)

sumo_cloud_tasks = Gauge(
    "sumo_cloud_tasks",
    "Total SUMO tasks offloaded to CLOUD"
)

sumo_vehicle_tasks = Gauge(
    "sumo_vehicle_tasks",
    "Total SUMO tasks executed on VEHICLE"
)


def fetch_sumo_metrics():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM sumo_orchestration_tasks")
    total_tasks = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT vehicle_id) FROM sumo_orchestration_tasks")
    vehicle_count = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(speed) FROM sumo_orchestration_tasks")
    avg_speed = cursor.fetchone()[0] or 0

    cursor.execute("SELECT AVG(battery) FROM sumo_orchestration_tasks")
    avg_battery = cursor.fetchone()[0] or 0

    cursor.execute("""
        SELECT decision, COUNT(*)
        FROM sumo_orchestration_tasks
        GROUP BY decision
    """)
    decision_counts = dict(cursor.fetchall())

    conn.close()

    return {
        "total_tasks": total_tasks,
        "vehicle_count": vehicle_count,
        "avg_speed": avg_speed,
        "avg_battery": avg_battery,
        "edge_tasks": decision_counts.get("EDGE", 0),
        "cloud_tasks": decision_counts.get("CLOUD", 0),
        "vehicle_tasks": decision_counts.get("VEHICLE", 0)
    }


def update_sumo_metrics():

    metrics = fetch_sumo_metrics()

    sumo_total_tasks.set(metrics["total_tasks"])
    sumo_vehicle_count.set(metrics["vehicle_count"])
    sumo_average_speed.set(metrics["avg_speed"])
    sumo_average_battery.set(metrics["avg_battery"])
    sumo_edge_tasks.set(metrics["edge_tasks"])
    sumo_cloud_tasks.set(metrics["cloud_tasks"])
    sumo_vehicle_tasks.set(metrics["vehicle_tasks"])

    print(
        "SUMO metrics updated | "
        f"Tasks={metrics['total_tasks']} | "
        f"Vehicles={metrics['vehicle_count']} | "
        f"Speed={metrics['avg_speed']:.2f}"
    )


def run_sumo_metrics_server():

    start_http_server(8001)

    print("SUMO Prometheus metrics running on http://localhost:8001/metrics")

    while True:
        update_sumo_metrics()
        time.sleep(5)


if __name__ == "__main__":
    run_sumo_metrics_server()