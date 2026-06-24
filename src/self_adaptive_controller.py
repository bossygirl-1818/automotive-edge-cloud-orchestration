import json
import pandas as pd
from datetime import datetime

from src.digital_twin_rl_fusion import map_digital_twin_to_rl_state
from src.traffic_rl_inference import predict_decision
from src.explainable_orchestrator import generate_explanation


DIGITAL_TWIN_FILE = "data/digital_twin_state.json"
FORECAST_FILE = "data/predictive_traffic_forecast.csv"
OUTPUT_FILE = "data/self_adaptive_decision.json"


def apply_self_adaptive_policy(rl_decision, rl_state, forecast):

    congestion_level = forecast["predicted_congestion_level"]
    edge_risk = forecast["predicted_edge_risk"]
    cloud_risk = forecast["predicted_cloud_risk"]
    battery_risk = forecast["predicted_battery_risk"]

    final_decision = rl_decision
    adaptation_reason = "RL decision accepted without override."

    if (
    congestion_level == "HIGH"
    and rl_decision == "VEHICLE"
    and rl_state["battery"] < 40
):
        final_decision = "EDGE"
        adaptation_reason = (
            "High predicted congestion detected; "
            "VEHICLE execution overridden to EDGE."
        )

    elif cloud_risk == "HIGH":
        final_decision = "EDGE"
        adaptation_reason = "High predicted cloud latency detected; CLOUD avoided and EDGE selected."

    elif battery_risk == "HIGH" and rl_decision == "VEHICLE":
        final_decision = "EDGE"
        adaptation_reason = "High battery drain risk detected; VEHICLE execution avoided."

    elif edge_risk == "HIGH" and cloud_risk != "HIGH":
        final_decision = "CLOUD"
        adaptation_reason = "High predicted edge load detected; CLOUD selected to reduce edge pressure."

    return final_decision, adaptation_reason


def run_self_adaptive_controller():

    with open(DIGITAL_TWIN_FILE, "r") as file:
        twin_state = json.load(file)

    forecast_df = pd.read_csv(FORECAST_FILE)
    forecast = forecast_df.iloc[0].to_dict()

    rl_state = map_digital_twin_to_rl_state(twin_state)
    rl_decision = predict_decision(rl_state)

    final_decision, adaptation_reason = apply_self_adaptive_policy(
        rl_decision,
        rl_state,
        forecast
    )

    explanation = generate_explanation(
        rl_state,
        final_decision
    )

    result = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "vehicle_id": twin_state["vehicle_twin"]["vehicle_id"],
        "rl_state": rl_state,
        "rl_decision": rl_decision,
        "final_decision": final_decision,
        "adaptation_reason": adaptation_reason,
        "forecast": forecast,
        "explanation": explanation
    }

    with open(OUTPUT_FILE, "w") as file:
        json.dump(result, file, indent=4)

    print("\n===== SELF-ADAPTIVE CONTROLLER =====\n")
    print("Vehicle:", result["vehicle_id"])
    print("RL Decision:", rl_decision)
    print("Final Adaptive Decision:", final_decision)
    print("Adaptation Reason:", adaptation_reason)

    print("\nExplanation:")
    for reason in explanation:
        print("-", reason)

    print("\nSaved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    run_self_adaptive_controller()