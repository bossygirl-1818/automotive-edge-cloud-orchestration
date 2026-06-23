import json

from src.traffic_rl_inference import predict_decision


DIGITAL_TWIN_FILE = "data/digital_twin_state.json"


def map_digital_twin_to_rl_state(twin_state):

    vehicle = twin_state["vehicle_twin"]
    road = twin_state["road_twin"]

    rl_state = {
        "traffic_density": road["traffic_density"],
        "network_quality": "MODERATE",
        "battery": vehicle["battery"],
        "speed": vehicle["speed"],
        "task_type": "obstacle_detection"
    }

    return rl_state


def run_digital_twin_rl_fusion():

    with open(DIGITAL_TWIN_FILE, "r") as file:
        twin_state = json.load(file)

    rl_state = map_digital_twin_to_rl_state(twin_state)

    decision = predict_decision(rl_state)

    print("\n===== DIGITAL TWIN + RL FUSION =====\n")
    print("Digital Twin Timestamp:", twin_state["timestamp"])
    print("Vehicle:", twin_state["vehicle_twin"]["vehicle_id"])
    print("Traffic Density:", rl_state["traffic_density"])
    print("Battery:", rl_state["battery"])
    print("Speed:", rl_state["speed"])
    print("Task Type:", rl_state["task_type"])
    print("\nRL Decision:", decision)


if __name__ == "__main__":
    run_digital_twin_rl_fusion()