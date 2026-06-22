import os
import csv
import random
from datetime import datetime


OUTPUT_FILE = "data/rl_reward_history.csv"


def calculate_decision(
    latency,
    priority,
    battery,
    edge_delay,
    cloud_delay,
    task_size
):
    """
    Realistic Vehicle-Edge-Cloud decision logic.

    VEHICLE:
    - Ultra-low latency task
    - High priority
    - Battery is healthy
    - Small task size

    EDGE:
    - Medium latency task
    - Edge delay is good
    - Battery is not too low

    CLOUD:
    - Large task
    - Low battery
    - High latency-tolerant workload
    """

    if (
        latency <= 70
        and priority == 3
        and battery >= 45
        and task_size <= 20
    ):
        return "VEHICLE"

    if (
        latency <= 180
        and edge_delay <= 45
        and battery >= 30
        and task_size <= 35
    ):
        return "EDGE"

    return "CLOUD"


def calculate_reward(
    episode,
    latency,
    battery,
    edge_delay,
    cloud_delay,
    decision,
    task_size
):
    reward = 0

    learning_bonus = min(episode * 0.10, 18)

    # Latency reward
    if latency <= 70:
        reward += 20
    elif latency <= 180:
        reward += 12
    else:
        reward += 4

    # Battery reward
    if battery >= 60:
        reward += 12
    elif battery >= 35:
        reward += 7
    else:
        reward -= 8

    # Decision reward
    if decision == "VEHICLE":
        reward += 12

        if task_size <= 20 and latency <= 70:
            reward += 6
        else:
            reward -= 4

    elif decision == "EDGE":
        reward += 15

        if edge_delay < cloud_delay:
            reward += 8

    elif decision == "CLOUD":
        reward += 8

        if battery < 35 or task_size > 35:
            reward += 8

    reward += learning_bonus

    noise = random.uniform(-3, 3)

    return round(reward + noise, 2)


def generate_realistic_history(episodes=150):

    os.makedirs("data", exist_ok=True)

    with open(OUTPUT_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "episode",
            "reward",
            "decision",
            "latency",
            "battery",
            "edge_delay",
            "cloud_delay",
            "task_size",
            "priority",
            "timestamp"
        ])

        base_latency = 230
        base_battery = 95

        for episode in range(1, episodes + 1):

            learning_factor = episode / episodes

            latency = max(
                25,
                int(base_latency - learning_factor * 145 + random.randint(-35, 35))
            )

            battery = max(
                20,
                int(base_battery - learning_factor * 42 + random.randint(-9, 9))
            )

            edge_delay = max(
                8,
                int(50 - learning_factor * 25 + random.randint(-8, 10))
            )

            cloud_delay = max(
                65,
                int(135 - learning_factor * 35 + random.randint(-15, 18))
            )

            priority = random.choices(
                [1, 2, 3],
                weights=[0.25, 0.45, 0.30]
            )[0]

            task_size = random.choices(
                [10, 15, 20, 25, 30, 40, 50],
                weights=[0.18, 0.18, 0.20, 0.18, 0.12, 0.09, 0.05]
            )[0]

            # Inject realistic task diversity
            if episode % 9 == 0:
                latency = random.randint(30, 65)
                priority = 3
                task_size = random.choice([10, 15, 20])

            if episode % 11 == 0:
                task_size = random.choice([40, 50])
                battery = random.randint(22, 38)
                latency = random.randint(180, 260)

            decision = calculate_decision(
                latency,
                priority,
                battery,
                edge_delay,
                cloud_delay,
                task_size
            )

            reward = calculate_reward(
                episode,
                latency,
                battery,
                edge_delay,
                cloud_delay,
                decision,
                task_size
            )

            writer.writerow([
                episode,
                reward,
                decision,
                latency,
                battery,
                edge_delay,
                cloud_delay,
                task_size,
                priority,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])

    print(f"Generated {episodes} realistic RL simulation records.")


if __name__ == "__main__":
    generate_realistic_history(1000)