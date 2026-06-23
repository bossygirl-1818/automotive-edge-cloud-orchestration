import random
import pandas as pd


DATASET = "data/sumo_advanced_orchestration.csv"


class TrafficRLEnvironment:

    def __init__(self):

        self.df = pd.read_csv(DATASET)

        self.current_index = 0

        self.actions = [
            "VEHICLE",
            "EDGE",
            "CLOUD"
        ]

    def reset(self):

        self.current_index = random.randint(
            0,
            len(self.df) - 1
        )

        return self.get_state()

    def get_state(self):

        row = self.df.iloc[self.current_index]

        return {
            "traffic_density": row["traffic_density"],
            "network_quality": row["network_quality"],
            "battery": row["battery"],
            "speed": row["speed"],
            "task_type": row["task_type"]
        }

    def step(self, action):

        row = self.df.iloc[self.current_index]

        optimal_decision = row["decision"]

        reward = 10 if action == optimal_decision else -5

        done = True

        next_state = None

        return (
            next_state,
            reward,
            done,
            {
                "optimal": optimal_decision
            }
        )


if __name__ == "__main__":

    env = TrafficRLEnvironment()

    state = env.reset()

    print("\n===== RL ENVIRONMENT TEST =====\n")

    print("State:")
    print(state)

    action = random.choice(
        env.actions
    )

    print("\nChosen Action:", action)

    _, reward, _, info = env.step(action)

    print("Reward:", reward)
    print("Optimal:", info["optimal"])