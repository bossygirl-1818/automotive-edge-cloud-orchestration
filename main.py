from src.task_generator import TaskGenerator
from src.resource_monitor import ResourceMonitor
from src.decision_engine import DecisionEngine
from src.simulator import ExecutionSimulator
from src.metrics import MetricsCollector

generator = TaskGenerator()
monitor = ResourceMonitor()
engine = DecisionEngine()
simulator = ExecutionSimulator()
metrics = MetricsCollector()

NUM_TASKS = 100

for i in range(1, NUM_TASKS + 1):

    task = generator.generate_task(i)

    vehicle = monitor.get_vehicle_resources()
    edge = monitor.get_edge_resources()
    cloud = monitor.get_cloud_resources()

    destination = engine.decide(
        task,
        vehicle,
        edge,
        cloud
    )

    latency = simulator.execute(destination)

    metrics.record(destination, latency)

metrics.report()