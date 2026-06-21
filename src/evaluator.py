from src.task_generator import TaskGenerator
from src.resource_monitor import ResourceMonitor
from src.decision_engine import DecisionEngine
from src.ml_orchestrator import MLOrchestrator
from src.simulator import ExecutionSimulator


class Evaluator:

    def __init__(self):

        self.generator = TaskGenerator()
        self.monitor = ResourceMonitor()
        self.adaptive_engine = DecisionEngine()
        self.ml_engine = MLOrchestrator()
        self.simulator = ExecutionSimulator()

    def evaluate(self, num_tasks=1000):

        adaptive_latency = 0
        ml_latency = 0

        adaptive_vehicle = 0
        adaptive_edge = 0
        adaptive_cloud = 0

        ml_vehicle = 0
        ml_edge = 0
        ml_cloud = 0

        for i in range(1, num_tasks + 1):

            task = self.generator.generate_task(i)

            vehicle = self.monitor.get_vehicle_resources()
            edge = self.monitor.get_edge_resources()
            cloud = self.monitor.get_cloud_resources()

            # Adaptive Engine Decision
            adaptive_decision = self.adaptive_engine.decide(
                task,
                vehicle,
                edge,
                cloud
            )

            adaptive_latency += self.simulator.execute(
                adaptive_decision
            )

            if adaptive_decision == "VEHICLE":
                adaptive_vehicle += 1
            elif adaptive_decision == "EDGE":
                adaptive_edge += 1
            else:
                adaptive_cloud += 1

            # ML Decision
            ml_decision = self.ml_engine.decide(
                vehicle_cpu=vehicle["cpu_usage"],
                battery=vehicle["battery_level"],
                edge_delay=edge["network_delay"],
                cloud_delay=cloud["network_delay"],
                task_latency=task["latency_requirement"]
            )

            ml_latency += self.simulator.execute(
                ml_decision
            )

            if ml_decision == "VEHICLE":
                ml_vehicle += 1
            elif ml_decision == "EDGE":
                ml_edge += 1
            else:
                ml_cloud += 1

        print("\n==============================")
        print(" PERFORMANCE COMPARISON ")
        print("==============================")

        print(
            f"\nAdaptive Average Latency: "
            f"{adaptive_latency / num_tasks:.2f} ms"
        )

        print(
            f"ML Average Latency: "
            f"{ml_latency / num_tasks:.2f} ms"
        )

        print("\nAdaptive Task Distribution")
        print(f"Vehicle: {adaptive_vehicle}")
        print(f"Edge   : {adaptive_edge}")
        print(f"Cloud  : {adaptive_cloud}")

        print("\nML Task Distribution")
        print(f"Vehicle: {ml_vehicle}")
        print(f"Edge   : {ml_edge}")
        print(f"Cloud  : {ml_cloud}")