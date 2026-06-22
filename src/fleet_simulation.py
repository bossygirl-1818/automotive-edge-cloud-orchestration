import simpy
import random
import csv
import os
from datetime import datetime


OUTPUT_FILE = "data/fleet_simulation_results.csv"


class Vehicle:

    def __init__(self, env, vehicle_id):
        self.env = env
        self.vehicle_id = vehicle_id
        self.resource = simpy.Resource(env, capacity=1)


class EdgeCluster:

    def __init__(self, env):
        self.env = env
        self.resource = simpy.Resource(env, capacity=5)


class CloudServer:

    def __init__(self, env):
        self.env = env
        self.resource = simpy.Resource(env, capacity=10)


def choose_execution_node(priority, task_size):

    if priority >= 8 and task_size <= 40:
        return "VEHICLE"

    elif priority >= 5:
        return "EDGE"

    else:
        return "CLOUD"


def process_task(env, vehicle, edge, cloud, task_id, writer):

    arrival_time = env.now

    priority = random.randint(1, 10)
    task_size = random.randint(5, 120)

    decision = choose_execution_node(
        priority,
        task_size
    )

    if decision == "VEHICLE":
        resource = vehicle.resource
        processing_time = random.uniform(1, 3)

    elif decision == "EDGE":
        resource = edge.resource
        processing_time = random.uniform(2, 4)

    else:
        resource = cloud.resource
        processing_time = random.uniform(4, 7)

    with resource.request() as request:
        yield request

        queue_wait_time = env.now - arrival_time

        yield env.timeout(processing_time)

        completion_time = env.now

    total_time = completion_time - arrival_time

    writer.writerow([
        task_id,
        vehicle.vehicle_id,
        priority,
        task_size,
        decision,
        round(arrival_time, 2),
        round(queue_wait_time, 2),
        round(processing_time, 2),
        round(total_time, 2),
        round(completion_time, 2),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ])

    print(
        f"[Time {completion_time:.2f}] "
        f"Vehicle {vehicle.vehicle_id} | "
        f"Task {task_id} -> {decision} | "
        f"Wait {queue_wait_time:.2f} | "
        f"Total {total_time:.2f}"
    )


def vehicle_task_generator(
    env,
    vehicle,
    edge,
    cloud,
    writer,
    tasks_per_vehicle
):

    for task_no in range(1, tasks_per_vehicle + 1):

        task_id = f"V{vehicle.vehicle_id}_T{task_no}"

        env.process(
            process_task(
                env,
                vehicle,
                edge,
                cloud,
                task_id,
                writer
            )
        )

        inter_arrival_time = random.uniform(0.5, 2.5)

        yield env.timeout(inter_arrival_time)


def run_fleet_simulation(
    vehicle_count=5,
    tasks_per_vehicle=50
):

    os.makedirs("data", exist_ok=True)

    env = simpy.Environment()

    vehicles = [
        Vehicle(env, vehicle_id=i)
        for i in range(1, vehicle_count + 1)
    ]

    edge = EdgeCluster(env)
    cloud = CloudServer(env)

    with open(OUTPUT_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "task_id",
            "vehicle_id",
            "priority",
            "task_size",
            "decision",
            "arrival_time",
            "queue_wait_time",
            "processing_time",
            "total_time",
            "completion_time",
            "timestamp"
        ])

        for vehicle in vehicles:
            env.process(
                vehicle_task_generator(
                    env,
                    vehicle,
                    edge,
                    cloud,
                    writer,
                    tasks_per_vehicle
                )
            )

        env.run()

    print("\nFleet simulation completed successfully.")
    print(f"Vehicles simulated: {vehicle_count}")
    print(f"Tasks per vehicle: {tasks_per_vehicle}")
    print(f"Total tasks: {vehicle_count * tasks_per_vehicle}")
    print(f"Results saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    run_fleet_simulation(
        vehicle_count=5,
        tasks_per_vehicle=50
    )