import csv
import os
from datetime import datetime

import traci

from src.sumo_task_generator import generate_sumo_task


SUMO_BINARY = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo.exe"
SUMO_CONFIG = "sumo/simulation.sumocfg"
OUTPUT_FILE = "data/sumo_orchestration_tasks.csv"


def decide_offloading(task):

    if task["priority"] >= 8 and task["latency_requirement"] <= 30:
        return "VEHICLE"

    if task["network_quality"] == "GOOD" and task["battery"] < 50:
        return "EDGE"

    if task["traffic_density"] == "HIGH":
        return "EDGE"

    if task["latency_requirement"] > 100:
        return "CLOUD"

    return "EDGE"


def run_sumo_orchestration():

    os.makedirs("data", exist_ok=True)

    traci.start([
        SUMO_BINARY,
        "-c",
        SUMO_CONFIG
    ])

    print("SUMO Connected Successfully\n")

    with open(OUTPUT_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "step",
            "vehicle_id",
            "speed",
            "position_x",
            "position_y",
            "traffic_density",
            "network_quality",
            "battery",
            "task_type",
            "priority",
            "latency_requirement",
            "task_size",
            "decision",
            "timestamp"
        ])

        step = 0

        while traci.simulation.getMinExpectedNumber() > 0:

            traci.simulationStep()

            vehicles = traci.vehicle.getIDList()
            vehicle_count = len(vehicles)

            print(f"\nStep {step} | Active Vehicles: {vehicle_count}")

            for vehicle_id in vehicles:

                speed = traci.vehicle.getSpeed(vehicle_id)
                position = traci.vehicle.getPosition(vehicle_id)

                task = generate_sumo_task(
                    vehicle_id,
                    speed,
                    position,
                    vehicle_count
                )

                decision = decide_offloading(task)

                writer.writerow([
                    step,
                    task["vehicle_id"],
                    task["speed"],
                    task["position_x"],
                    task["position_y"],
                    task["traffic_density"],
                    task["network_quality"],
                    task["battery"],
                    task["task_type"],
                    task["priority"],
                    task["latency_requirement"],
                    task["task_size"],
                    decision,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ])

                print(
                    f"{vehicle_id} | "
                    f"Task={task['task_type']} | "
                    f"Speed={task['speed']} | "
                    f"Density={task['traffic_density']} | "
                    f"Network={task['network_quality']} | "
                    f"Decision={decision}"
                )

            step += 1

    traci.close()

    print("\nSUMO orchestration simulation finished.")
    print(f"Results saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    run_sumo_orchestration()