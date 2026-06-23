import pandas as pd

from src.traffic_rl_inference import predict_decision


DATASET = "data/sumo_advanced_orchestration.csv"


def evaluate_traffic_rl():

    df = pd.read_csv(DATASET)

    correct = 0
    predictions = []

    for _, row in df.iterrows():

        state = {
            "traffic_density": row["traffic_density"],
            "network_quality": row["network_quality"],
            "battery": row["battery"],
            "speed": row["speed"],
            "task_type": row["task_type"]
        }

        predicted = predict_decision(state)
        actual = row["decision"]

        predictions.append(predicted)

        if predicted == actual:
            correct += 1

    accuracy = (correct / len(df)) * 100

    df["rl_prediction"] = predictions
    df.to_csv(
        "data/traffic_rl_evaluation_results.csv",
        index=False
    )

    print("\n===== TRAFFIC RL EVALUATION =====\n")
    print(f"Total Records: {len(df)}")
    print(f"Correct Predictions: {correct}")
    print(f"Wrong Predictions: {len(df) - correct}")
    print(f"Accuracy: {accuracy:.2f}%")

    print("\nPredicted Decision Distribution:")
    print(df["rl_prediction"].value_counts())

    print("\nResults saved to:")
    print("data/traffic_rl_evaluation_results.csv")


if __name__ == "__main__":
    evaluate_traffic_rl()