import pandas as pd
import torch

from src.RL_Files.environment import AutomotiveEnv
from src.RL_Files.dqn_agent import DQNAgent


ACTION_MAP = {
    0: "VEHICLE",
    1: "EDGE",
    2: "CLOUD"
}


def evaluate_dqn(num_steps=1000):

    env = AutomotiveEnv()

    agent = DQNAgent(
        state_size=env.state_size,
        action_size=env.action_space
    )

    agent.load("data/dqn_orchestrator.pth")
    agent.epsilon = 0.0

    state, raw = env.reset()

    total_reward = 0

    vehicle_count = 0
    edge_count = 0
    cloud_count = 0

    results = []

    for step in range(1, num_steps + 1):

        state_tensor = torch.FloatTensor(state).unsqueeze(0).to(agent.device)

        with torch.no_grad():
            q_values = agent.model(state_tensor)

        action = torch.argmax(q_values).item()

        next_state_data, reward, done, raw = env.step(action)
        next_state, next_raw = next_state_data

        decision = ACTION_MAP[action]

        if decision == "VEHICLE":
            vehicle_count += 1
        elif decision == "EDGE":
            edge_count += 1
        else:
            cloud_count += 1

        total_reward += reward

        results.append({
            "step": step,
            "decision": decision,
            "reward": reward,
            "task_latency": raw["task_latency"],
            "task_priority": raw["task_priority"],
            "vehicle_cpu": raw["vehicle_cpu"],
            "battery": raw["battery"],
            "edge_delay": raw["edge_delay"],
            "cloud_delay": raw["cloud_delay"]
        })

        state = next_state

    avg_reward = total_reward / num_steps

    summary = pd.DataFrame([{
        "strategy": "Deep RL",
        "average_reward": avg_reward,
        "vehicle_tasks": vehicle_count,
        "edge_tasks": edge_count,
        "cloud_tasks": cloud_count,
        "total_tasks": num_steps
    }])

    results_df = pd.DataFrame(results)

    summary.to_csv(
        "data/dqn_evaluation_summary.csv",
        index=False
    )

    results_df.to_csv(
        "data/dqn_evaluation_results.csv",
        index=False
    )

    print("\nDQN Evaluation Completed")
    print("========================")
    print(f"Total Steps: {num_steps}")
    print(f"Average Reward: {avg_reward:.2f}")
    print(f"Vehicle Tasks: {vehicle_count}")
    print(f"Edge Tasks: {edge_count}")
    print(f"Cloud Tasks: {cloud_count}")

    print("\nSaved:")
    print("data/dqn_evaluation_summary.csv")
    print("data/dqn_evaluation_results.csv")


if __name__ == "__main__":
    evaluate_dqn()