import os
import csv
import random
from datetime import datetime


OUTPUT_FILE = "data/vehicle_telemetry.csv"


def generate_telemetry(episodes=1000):

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

                # Vehicle processing consumes more battery
                battery -= random.uniform(0.03, 0.08)

            elif episode % 11 == 0:
                decision = "CLOUD"
                vehicle_cpu -= random.randint(3, 8)
                edge_load -= random.randint(2, 5)
                cloud_load += random.randint(8, 14)

                # Cloud offloading consumes least onboard battery
                battery -= random.uniform(0.01, 0.03)

            else:
                decision = "EDGE"
                vehicle_cpu -= random.randint(1, 4)
                edge_load += random.randint(3, 8)
                cloud_load -= random.randint(1, 3)

                # Edge offloading consumes moderate battery
                battery -= random.uniform(0.02, 0.05)

            # Rare heavy workload dip
            if random.random() < 0.03:
                battery -= random.uniform(0.2, 0.7)

            # Natural EV battery fluctuation
            battery += random.uniform(-0.08, 0.08)

            # Heavy local CPU usage consumes extra power
            if vehicle_cpu > 75:
                battery -= random.uniform(0.08, 0.18)

            # Cloud offloading gives slight battery relief
            if decision == "CLOUD":
                battery += random.uniform(0.02, 0.10)

            vehicle_cpu = min(max(vehicle_cpu, 20), 90)
            edge_load = min(max(edge_load, 20), 95)
            cloud_load = min(max(cloud_load, 20), 95)

            # Keep battery realistic for long 1000-episode simulation
            battery = min(max(battery, 35), 100)

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
    generate_telemetry(1000)