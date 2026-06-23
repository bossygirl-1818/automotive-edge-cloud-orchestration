import json
import random
from datetime import datetime


OUTPUT_FILE = "data/digital_twin_state.json"


def generate_vehicle_twin():
    return {
        "vehicle_id": f"vehicle_{random.randint(1, 30)}",
        "speed": round(random.uniform(5, 22), 2),
        "battery": round(random.uniform(20, 100), 2),
        "cpu_usage": round(random.uniform(10, 95), 2),
        "task_queue": random.randint(1, 15),
        "health_status": random.choice(["NORMAL", "WARNING", "CRITICAL"])
    }


def generate_road_twin():
    return {
        "intersection_id": "advanced_sumo_junction_01",
        "traffic_density": random.choice(["LOW", "MEDIUM", "HIGH"]),
        "signal_state": random.choice(["NS_GREEN", "EW_GREEN", "ALL_RED"]),
        "active_vehicles": random.randint(5, 50),
        "average_speed": round(random.uniform(4, 18), 2),
        "congestion_level": random.choice(["SMOOTH", "MODERATE", "CONGESTED"])
    }


def generate_edge_twin():
    return {
        "edge_server_id": "edge_node_01",
        "cpu_load": round(random.uniform(20, 95), 2),
        "memory_usage": round(random.uniform(25, 90), 2),
        "active_tasks": random.randint(5, 80),
        "latency_ms": round(random.uniform(5, 40), 2),
        "status": random.choice(["NORMAL", "OVERLOADED", "DEGRADED"])
    }


def generate_cloud_twin():
    return {
        "cloud_region": "cloud_region_01",
        "cpu_load": round(random.uniform(10, 85), 2),
        "memory_usage": round(random.uniform(20, 90), 2),
        "active_tasks": random.randint(10, 120),
        "latency_ms": round(random.uniform(40, 150), 2),
        "status": random.choice(["NORMAL", "BUSY", "DEGRADED"])
    }


def generate_system_twin_state():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "vehicle_twin": generate_vehicle_twin(),
        "road_twin": generate_road_twin(),
        "edge_twin": generate_edge_twin(),
        "cloud_twin": generate_cloud_twin()
    }


def save_twin_state():
    state = generate_system_twin_state()

    with open(OUTPUT_FILE, "w") as file:
        json.dump(state, file, indent=4)

    print("Digital twin state generated successfully.")
    print(f"Saved to: {OUTPUT_FILE}")
    print(json.dumps(state, indent=4))


if __name__ == "__main__":
    save_twin_state()