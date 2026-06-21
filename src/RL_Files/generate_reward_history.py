import random

from src.RL_Files.reward_logger import log_reward


def generate_rewards(episodes=100):

    for episode in range(1, episodes + 1):

        decision = random.choice(["VEHICLE", "EDGE", "CLOUD"])
        latency = random.randint(10, 300)
        battery = random.randint(10, 100)
        edge_delay = random.randint(5, 50)
        cloud_delay = random.randint(60, 180)

        reward = 0

        if latency <= 50:
            reward += 20
        elif latency <= 150:
            reward += 10
        else:
            reward -= 5

        if battery > 40:
            reward += 10
        else:
            reward -= 10

        if decision == "EDGE":
            reward += 15
        elif decision == "VEHICLE":
            reward += 10
        else:
            reward += 5

        log_reward(
            episode,
            reward,
            decision,
            latency,
            battery,
            edge_delay,
            cloud_delay
        )

    print(f"Generated {episodes} RL reward records successfully.")


if __name__ == "__main__":
    generate_rewards(100)