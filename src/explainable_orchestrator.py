import json

from src.digital_twin_rl_fusion import map_digital_twin_to_rl_state
from src.traffic_rl_inference import predict_decision


DIGITAL_TWIN_FILE = "data/digital_twin_state.json"
OUTPUT_FILE = "data/explainable_orchestration_result.json"


def generate_explanation(rl_state, decision):

    reasons = []

    traffic = rl_state["traffic_density"]
    battery = float(rl_state["battery"])
    speed = float(rl_state["speed"])
    network = rl_state["network_quality"]
    task = rl_state["task_type"]

    if traffic == "HIGH":
        reasons.append("High traffic density increases local congestion risk.")

    if battery < 40:
        reasons.append("Vehicle battery is low, so local execution may be risky.")

    if speed < 8:
        reasons.append("Low vehicle speed indicates possible congestion.")

    if network == "POOR":
        reasons.append("Poor network quality reduces cloud offloading reliability.")

    if task in ["obstacle_detection", "traffic_sign_recognition", "lane_detection"]:
        reasons.append("Safety-critical task requires low-latency processing.")

    if decision == "EDGE":
        reasons.append("EDGE was selected to reduce latency while avoiding vehicle overload.")

    elif decision == "CLOUD":
        reasons.append("CLOUD was selected because remote processing can handle heavier computation.")

    elif decision == "VEHICLE":
        reasons.append("VEHICLE was selected to avoid network dependency and process locally.")

    return reasons


def run_explainable_orchestrator():

    with open(DIGITAL_TWIN_FILE, "r") as file:
        twin_state = json.load(file)

    rl_state = map_digital_twin_to_rl_state(twin_state)

    decision = predict_decision(rl_state)

    explanation = generate_explanation(
        rl_state,
        decision
    )

    result = {
        "timestamp": twin_state["timestamp"],
        "vehicle_id": twin_state["vehicle_twin"]["vehicle_id"],
        "rl_state": rl_state,
        "decision": decision,
        "explanation": explanation
    }

    with open(OUTPUT_FILE, "w") as file:
        json.dump(result, file, indent=4)

    print("\n===== EXPLAINABLE ORCHESTRATOR =====\n")
    print("Vehicle:", result["vehicle_id"])
    print("Decision:", decision)

    print("\nExplanation:")
    for reason in explanation:
        print("-", reason)

    print("\nSaved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    run_explainable_orchestrator()