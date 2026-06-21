import os
import csv
import random
from datetime import datetime


OUTPUT_FILE = "data/vehicle_telemetry.csv"


def generate_telemetry(episodes=150):

    os.makedirs("data", exist_ok=True)

    battery = 96.0
    vehicle_cpu = 35
    edge_load = 40
    cloud_load = 35

    with open(OUTPUT_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "episode",
            "vehicle_cpu",
            "battery",
            "edge_load",
            "cloud_load",
            "network_latency",
            "edge_delay",
            "cloud_delay",
            "decision",
            "timestamp"
        ])

        for episode in range(1, episodes + 1):

            learning_factor = episode / episodes

            edge_delay = max(
                10,
                int(45 - learning_factor * 20 + random.randint(-4, 4))
            )

            cloud_delay = max(
                65,
                int(125 - learning_factor * 25 + random.randint(-8, 8))
            )

            network_latency = max(
                25,
                int(210 - learning_factor * 120 + random.randint(-12, 12))
            )

            if episode % 9 == 0:
                decision = "VEHICLE"
                vehicle_cpu += random.randint(8, 14)
                edge_load -= random.randint(1, 4)
                cloud_load -= random.randint(1, 3)
                battery -= random.uniform(0.45, 0.75)

            elif episode % 11 == 0:
                decision = "CLOUD"
                vehicle_cpu -= random.randint(3, 8)
                edge_load -= random.randint(2, 5)
                cloud_load += random.randint(8, 14)
                battery -= random.uniform(0.18, 0.35)

            else:
                decision = "EDGE"
                vehicle_cpu -= random.randint(1, 4)
                edge_load += random.randint(3, 8)
                cloud_load -= random.randint(1, 3)
                battery -= random.uniform(0.25, 0.50)

            # Rare heavy workload battery drop
            if random.random() < 0.12:
                battery -= random.uniform(1.0, 3.5)

            # Natural battery fluctuation
            battery += random.uniform(-1.0, 1.0)

            # Heavy local processing consumes extra battery
            if vehicle_cpu > 75:
                battery -= random.uniform(0.5, 1.5)

            # Cloud offloading gives small battery relief
            if decision == "CLOUD":
                battery += random.uniform(0.5, 1.5)

            vehicle_cpu = min(max(vehicle_cpu, 20), 90)
            edge_load = min(max(edge_load, 20), 95)
            cloud_load = min(max(cloud_load, 20), 95)

            # Allow battery to continue naturally instead of flat 35%
            battery = min(battery, 100)

            if battery < 15:
                battery = random.uniform(15, 22)

            writer.writerow([
                episode,
                round(vehicle_cpu, 2),
                round(battery, 2),
                round(edge_load, 2),
                round(cloud_load, 2),
                network_latency,
                edge_delay,
                cloud_delay,
                decision,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])

    print(f"Generated {episodes} telemetry records successfully.")


if __name__ == "__main__":
    generate_telemetry(150)