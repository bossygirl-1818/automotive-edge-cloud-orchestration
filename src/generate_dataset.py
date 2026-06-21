import pandas as pd

from src.task_generator import TaskGenerator
from src.resource_monitor import ResourceMonitor
from src.decision_engine import DecisionEngine

generator = TaskGenerator()
monitor = ResourceMonitor()
engine = DecisionEngine()

data = []

NUM_SAMPLES = 5000

for i in range(NUM_SAMPLES):

    task = generator.generate_task(i)

    vehicle = monitor.get_vehicle_resources()
    edge = monitor.get_edge_resources()
    cloud = monitor.get_cloud_resources()

    decision = engine.decide(
        task,
        vehicle,
        edge,
        cloud
    )

    data.append({
        "vehicle_cpu": vehicle["cpu_usage"],
        "battery": vehicle["battery_level"],
        "edge_delay": edge["network_delay"],
        "cloud_delay": cloud["network_delay"],
        "task_latency": task["latency_requirement"],
        "decision": decision
    })

df = pd.DataFrame(data)

df.to_csv("data/training_data.csv", index=False)

print("Dataset generated successfully!")
print(f"Rows generated: {len(df)}")
print(df.head())