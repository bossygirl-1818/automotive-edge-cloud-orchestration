import os
import pandas as pd

from src.RL_Files.environment import AutomotiveEnv
from src.RL_Files.dqn_agent import DQNAgent


def train_dqn(
    episodes=500,
    steps_per_episode=50
):
    env = AutomotiveEnv()
    agent = DQNAgent(
        state_size=env.state_size,
        action_size=env.action_space
    )

    rewards_history = []

    for episode in range(1, episodes + 1):

        state, raw = env.reset()
        total_reward = 0

        for _ in range(steps_per_episode):

            action = agent.act(state)

            next_state_data, reward, done, raw = env.step(action)

            next_state, next_raw = next_state_data

            agent.remember(
                state,
                action,
                reward,
                next_state,
                done
            )

            state = next_state
            total_reward += reward

            agent.replay()

        rewards_history.append({
            "episode": episode,
            "reward": total_reward,
            "epsilon": agent.epsilon
        })

        if episode % 25 == 0:
            print(
                f"Episode {episode}/{episodes} | "
                f"Reward: {total_reward:.2f} | "
                f"Epsilon: {agent.epsilon:.4f}"
            )

    os.makedirs("data", exist_ok=True)

    agent.save("data/dqn_orchestrator.pth")

    rewards_df = pd.DataFrame(rewards_history)
    rewards_df.to_csv(
        "data/dqn_training_rewards.csv",
        index=False
    )

    print("\nDQN training completed!")
    print("Model saved: data/dqn_orchestrator.pth")
    print("Rewards saved: data/dqn_training_rewards.csv")


if __name__ == "__main__":
    train_dqn()