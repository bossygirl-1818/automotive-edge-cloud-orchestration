from src.ml_orchestrator import MLOrchestrator

orchestrator = MLOrchestrator()

decision = orchestrator.decide(
    vehicle_cpu=92,
    battery=18,
    edge_delay=10,
    cloud_delay=120,
    task_latency=10
)

print("Predicted Decision:", decision)