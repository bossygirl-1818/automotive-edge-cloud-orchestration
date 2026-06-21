from src.RL_Files.rl_agent import RLOrchestrator


def get_rl_decision():
    orchestrator = RLOrchestrator()
    result = orchestrator.predict()

    return result


if __name__ == "__main__":
    result = get_rl_decision()

    print("\nRL Orchestrator Decision")
    print("========================")
    print(f"Decision: {result['decision']}")
    print(f"Q-Values: {result['q_values']}")
    print(f"Task Latency: {result['task_latency']} ms")
    print(f"Task Priority: {result['task_priority']}")
    print(f"Battery: {result['battery']:.2f}%")
    print(f"Edge Delay: {result['edge_delay']:.2f} ms")
    print(f"Cloud Delay: {result['cloud_delay']:.2f} ms")