import os
import csv
from datetime import datetime


REWARD_FILE = "data/rl_reward_history.csv"


def initialize_reward_file():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(REWARD_FILE):
        with open(REWARD_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "episode",
                "reward",
                "decision",
                "latency",
                "battery",
                "edge_delay",
                "cloud_delay",
                "timestamp"
            ])


def log_reward(
    episode,
    reward,
    decision,
    latency,
    battery,
    edge_delay,
    cloud_delay
):

    initialize_reward_file()

    with open(REWARD_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            episode,
            reward,
            decision,
            latency,
            battery,
            edge_delay,
            cloud_delay,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])