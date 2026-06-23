import pickle
import random


MODEL_PATH = "data/traffic_rl_q_table.pkl"

ACTIONS = [
    "VEHICLE",
    "EDGE",
    "CLOUD"
]


def state_to_key(state):
    return (
        state["traffic_density"],
        state["network_quality"],
        round(float(state["battery"]) / 10) * 10,
        round(float(state["speed"]) / 5) * 5,
        state["task_type"]
    )


def load_model():
    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)


def predict_decision(state):
    q_table = load_model()
    state_key = state_to_key(state)

    if state_key not in q_table:
        return random.choice(ACTIONS)

    return max(
        q_table[state_key],
        key=q_table[state_key].get
    )


if __name__ == "__main__":

    sample_state = {
        "traffic_density": "HIGH",
        "network_quality": "MODERATE",
        "battery": 55,
        "speed": 6,
        "task_type": "obstacle_detection"
    }

    decision = predict_decision(sample_state)

    print("\n===== TRAFFIC RL INFERENCE TEST =====\n")
    print("Input State:", sample_state)
    print("Predicted Decision:", decision)