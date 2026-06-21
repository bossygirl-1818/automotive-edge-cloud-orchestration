import pandas as pd

from src.task_generator import TaskGenerator
from src.resource_monitor import ResourceMonitor
from src.decision_engine import DecisionEngine

generator = TaskGenerator()
monitor = ResourceMonitor()
engine = DecisionEngine()

data = []

NUM_SAMPLES = 10000

for i in range(NUM_SAMPLES):

    task = generator.generate_task(i)

    vehicle = monitor.get_vehicle_resources()
    edge = monitor.get_edge_resources()
    cloud = monitor.get_cloud_resources()

    decision = engine.decide(task, vehicle, edge, cloud)

    data.append({
        "vehicle_cpu": vehicle["cpu_usage"],
        "battery": vehicle["battery_level"],
        "vehicle_speed": vehicle["vehicle_speed"],
        "traffic_density": vehicle["traffic_density"],
        "edge_delay": edge["network_delay"],
        "edge_bandwidth": edge["network_bandwidth"],
        "cloud_delay": cloud["network_delay"],
        "cloud_bandwidth": cloud["network_bandwidth"],
        "task_latency": task["latency_requirement"],
        "task_priority": task["task_priority"],
        "task_size": task["task_size"],
        "decision": decision
    })

df = pd.DataFrame(data)

df.to_csv("data/training_data.csv", index=False)

print("Advanced dataset generated successfully!")
print(f"Rows generated: {len(df)}")
print(df.head())