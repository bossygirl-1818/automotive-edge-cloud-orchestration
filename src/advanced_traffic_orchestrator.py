import random
import pandas as pd


OUTPUT_FILE = "data/sumo_advanced_orchestration.csv"


TASK_TYPES = [
    "lane_detection",
    "obstacle_detection",
    "traffic_sign_recognition",
    "route_planning",
    "driver_behavior_analysis",
    "vehicle_diagnostics"
]


def classify_traffic_density(speed):

    if speed < 6:
        return "HIGH"

    elif speed < 12:
        return "MEDIUM"

    return "LOW"


def classify_network():

    return random.choice([
        "GOOD",
        "MODERATE",
        "POOR"
    ])


def orchestration_decision(
        battery,
        traffic_density,
        network_quality,
        task_type
):

    if battery < 20:
        return "CLOUD"

    if traffic_density == "HIGH":
        return "EDGE"

    if network_quality == "POOR":
        return "VEHICLE"

    if task_type in [
        "obstacle_detection",
        "lane_detection"
    ]:
        return "VEHICLE"

    return random.choice([
        "EDGE",
        "CLOUD"
    ])


records = []

for step in range(1, 501):

    for vehicle_id in range(1, 31):

        speed = round(
            random.uniform(2, 18),
            2
        )

        battery = round(
            random.uniform(10, 100),
            2
        )

        task_type = random.choice(
            TASK_TYPES
        )

        traffic_density = classify_traffic_density(
            speed
        )

        network_quality = classify_network()

        decision = orchestration_decision(
            battery,
            traffic_density,
            network_quality,
            task_type
        )

        records.append({
            "step": step,
            "vehicle_id": f"veh_{vehicle_id}",
            "speed": speed,
            "battery": battery,
            "traffic_density": traffic_density,
            "network_quality": network_quality,
            "task_type": task_type,
            "decision": decision
        })


df = pd.DataFrame(records)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print(
    f"Dataset generated successfully: {OUTPUT_FILE}"
)

print(
    f"Total records: {len(df)}"
)