import simpy
import random
import csv
import os
from datetime import datetime


OUTPUT_FILE = "data/digital_twin_results.csv"


class VehicleNode:

    def __init__(self, env):
        self.env = env
        self.resource = simpy.Resource(env, capacity=1)

    def process_task(self, task_id):
        processing_time = random.randint(1, 3)
        yield self.env.timeout(processing_time)
        return processing_time


class EdgeNode:

    def __init__(self, env):
        self.env = env
        self.resource = simpy.Resource(env, capacity=2)

    def process_task(self, task_id):
        processing_time = random.randint(2, 4)
        yield self.env.timeout(processing_time)
        return processing_time


class CloudNode:

    def __init__(self, env):
        self.env = env
        self.resource = simpy.Resource(env, capacity=4)

    def process_task(self, task_id):
        processing_time = random.randint(3, 6)
        yield self.env.timeout(processing_time)
        return processing_time


def choose_execution_node(task_priority):

    if task_priority >= 8:
        return "VEHICLE"

    elif task_priority >= 5:
        return "EDGE"

    else:
        return "CLOUD"


def vehicle_task_process(env, task_id, vehicle, edge, cloud, writer):

    arrival_time = env.now

    task_priority = random.randint(1, 10)
    task_size = random.randint(5, 100)

    decision = choose_execution_node(task_priority)

    if decision == "VEHICLE":
        node = vehicle
    elif decision == "EDGE":
        node = edge
    else:
        node = cloud

    with node.resource.request() as request:
        yield request

        queue_wait_time = env.now - arrival_time

        processing_start = env.now

        processing_time = yield env.process(
            node.process_task(task_id)
        )

        completion_time = env.now

    total_time = completion_time - arrival_time

    writer.writerow([
        task_id,
        task_priority,
        task_size,
        decision,
        arrival_time,
        queue_wait_time,
        processing_time,
        total_time,
        completion_time,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ])

    print(
        f"[Time {completion_time}] Task {task_id} -> {decision} | "
        f"Wait: {queue_wait_time} | Process: {processing_time} | Total: {total_time}"
    )


def task_arrival_generator(env, vehicle, edge, cloud, writer, total_tasks=100):

    for task_id in range(1, total_tasks + 1):

        env.process(
            vehicle_task_process(
                env,
                task_id,
                vehicle,
                edge,
                cloud,
                writer
            )
        )

        inter_arrival_time = random.uniform(0.5, 2.0)

        yield env.timeout(inter_arrival_time)


def run_digital_twin(total_tasks=100):

    os.makedirs("data", exist_ok=True)

    env = simpy.Environment()

    vehicle = VehicleNode(env)
    edge = EdgeNode(env)
    cloud = CloudNode(env)

    with open(OUTPUT_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "task_id",
            "task_priority",
            "task_size",
            "decision",
            "arrival_time",
            "queue_wait_time",
            "processing_time",
            "total_time",
            "completion_time",
            "timestamp"
        ])

        env.process(
            task_arrival_generator(
                env,
                vehicle,
                edge,
                cloud,
                writer,
                total_tasks
            )
        )

        env.run()

    print("Digital Twin simulation completed successfully.")
    print(f"Results saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    run_digital_twin(total_tasks=100)