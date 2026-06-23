import random
import pickle
from collections import defaultdict

from src.traffic_rl_environment import TrafficRLEnvironment


MODEL_PATH = "data/traffic_rl_q_table.pkl"


class TrafficRLAgent:

    def __init__(
        self,
        actions,
        learning_rate=0.1,
        discount_factor=0.9,
        exploration_rate=0.2
    ):
        self.actions = actions
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_rate
        self.q_table = defaultdict(
            lambda: {action: 0.0 for action in self.actions}
        )

    def state_to_key(self, state):
        return (
            state["traffic_density"],
            state["network_quality"],
            round(float(state["battery"]) / 10) * 10,
            round(float(state["speed"]) / 5) * 5,
            state["task_type"]
        )

    def choose_action(self, state):
        state_key = self.state_to_key(state)

        if random.random() < self.epsilon:
            return random.choice(self.actions)

        return max(
            self.q_table[state_key],
            key=self.q_table[state_key].get
        )

    def learn(self, state, action, reward):
        state_key = self.state_to_key(state)

        old_value = self.q_table[state_key][action]

        self.q_table[state_key][action] = old_value + self.lr * (
            reward - old_value
        )

    def save(self):
        with open(MODEL_PATH, "wb") as file:
            pickle.dump(dict(self.q_table), file)

        print(f"Traffic RL model saved to {MODEL_PATH}")


if __name__ == "__main__":

    env = TrafficRLEnvironment()

    agent = TrafficRLAgent(
        actions=env.actions
    )

    episodes = 5000
    total_reward = 0

    for episode in range(episodes):

        state = env.reset()

        action = agent.choose_action(state)

        _, reward, _, info = env.step(action)

        agent.learn(
            state,
            action,
            reward
        )

        total_reward += reward

        if (episode + 1) % 500 == 0:
            print(
                f"Episode {episode + 1} | "
                f"Total Reward: {total_reward}"
            )

    agent.save()

    print("\nTraffic-Aware RL Agent training completed.")