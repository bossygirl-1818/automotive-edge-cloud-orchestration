import json
import sqlite3


JSON_FILE = "data/digital_twin_state.json"
DB_PATH = "data/orchestrator.db"


def create_digital_twin_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS digital_twin_states (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,

            vehicle_id TEXT,
            vehicle_speed REAL,
            vehicle_battery REAL,
            vehicle_cpu_usage REAL,
            vehicle_task_queue INTEGER,
            vehicle_health_status TEXT,

            intersection_id TEXT,
            traffic_density TEXT,
            signal_state TEXT,
            active_vehicles INTEGER,
            road_average_speed REAL,
            congestion_level TEXT,

            edge_server_id TEXT,
            edge_cpu_load REAL,
            edge_memory_usage REAL,
            edge_active_tasks INTEGER,
            edge_latency_ms REAL,
            edge_status TEXT,

            cloud_region TEXT,
            cloud_cpu_load REAL,
            cloud_memory_usage REAL,
            cloud_active_tasks INTEGER,
            cloud_latency_ms REAL,
            cloud_status TEXT
        )
    """)

    conn.commit()
    conn.close()


def load_digital_twin_state_to_db():
    create_digital_twin_table()

    with open(JSON_FILE, "r") as file:
        state = json.load(file)

    vehicle = state["vehicle_twin"]
    road = state["road_twin"]
    edge = state["edge_twin"]
    cloud = state["cloud_twin"]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO digital_twin_states (
            timestamp,

            vehicle_id,
            vehicle_speed,
            vehicle_battery,
            vehicle_cpu_usage,
            vehicle_task_queue,
            vehicle_health_status,

            intersection_id,
            traffic_density,
            signal_state,
            active_vehicles,
            road_average_speed,
            congestion_level,

            edge_server_id,
            edge_cpu_load,
            edge_memory_usage,
            edge_active_tasks,
            edge_latency_ms,
            edge_status,

            cloud_region,
            cloud_cpu_load,
            cloud_memory_usage,
            cloud_active_tasks,
            cloud_latency_ms,
            cloud_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        state["timestamp"],

        vehicle["vehicle_id"],
        vehicle["speed"],
        vehicle["battery"],
        vehicle["cpu_usage"],
        vehicle["task_queue"],
        vehicle["health_status"],

        road["intersection_id"],
        road["traffic_density"],
        road["signal_state"],
        road["active_vehicles"],
        road["average_speed"],
        road["congestion_level"],

        edge["edge_server_id"],
        edge["cpu_load"],
        edge["memory_usage"],
        edge["active_tasks"],
        edge["latency_ms"],
        edge["status"],

        cloud["cloud_region"],
        cloud["cpu_load"],
        cloud["memory_usage"],
        cloud["active_tasks"],
        cloud["latency_ms"],
        cloud["status"]
    ))

    conn.commit()
    conn.close()

    print("Digital twin state loaded into SQLite successfully.")


if __name__ == "__main__":
    load_digital_twin_state_to_db()