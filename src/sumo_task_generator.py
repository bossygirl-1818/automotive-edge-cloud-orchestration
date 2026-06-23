import random


TASK_TYPES = [
    "lane_detection",
    "obstacle_detection",
    "traffic_sign_recognition",
    "route_planning",
    "vehicle_diagnostics",
    "driver_behavior_analysis"
]


def estimate_traffic_density(vehicle_count):

    if vehicle_count >= 15:
        return "HIGH"

    elif vehicle_count >= 7:
        return "MEDIUM"

    else:
        return "LOW"


def estimate_network_quality(speed, traffic_density):

    if traffic_density == "HIGH":
        return random.choice(["POOR", "MODERATE"])

    if speed < 5:
        return random.choice(["MODERATE", "POOR"])

    if speed > 18:
        return random.choice(["GOOD", "MODERATE"])

    return random.choice(["GOOD", "MODERATE"])


def generate_sumo_task(vehicle_id, speed, position, vehicle_count):

    task_type = random.choice(TASK_TYPES)

    traffic_density = estimate_traffic_density(vehicle_count)
    network_quality = estimate_network_quality(speed, traffic_density)

    battery_level = round(random.uniform(35, 95), 2)

    if task_type in ["lane_detection", "obstacle_detection"]:
        priority = random.randint(8, 10)
        latency_requirement = random.randint(10, 30)
        task_size = random.randint(10, 35)

    elif task_type == "traffic_sign_recognition":
        priority = random.randint(6, 8)
        latency_requirement = random.randint(30, 70)
        task_size = random.randint(20, 50)

    elif task_type == "route_planning":
        priority = random.randint(4, 7)
        latency_requirement = random.randint(70, 120)
        task_size = random.randint(40, 90)

    else:
        priority = random.randint(1, 5)
        latency_requirement = random.randint(100, 200)
        task_size = random.randint(50, 120)

    return {
        "vehicle_id": vehicle_id,
        "speed": round(speed, 2),
        "position_x": round(position[0], 2),
        "position_y": round(position[1], 2),
        "traffic_density": traffic_density,
        "network_quality": network_quality,
        "battery": battery_level,
        "task_type": task_type,
        "priority": priority,
        "latency_requirement": latency_requirement,
        "task_size": task_size
    }