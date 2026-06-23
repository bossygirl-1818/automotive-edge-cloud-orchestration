import time
import pandas as pd

from prometheus_client import Gauge, start_http_server


RESULTS_FILE = "data/traffic_rl_evaluation_results.csv"


traffic_rl_total_records = Gauge(
    "traffic_rl_total_records",
    "Total records evaluated by Traffic RL agent"
)

traffic_rl_correct_predictions = Gauge(
    "traffic_rl_correct_predictions",
    "Correct Traffic RL predictions"
)

traffic_rl_wrong_predictions = Gauge(
    "traffic_rl_wrong_predictions",
    "Wrong Traffic RL predictions"
)

traffic_rl_accuracy = Gauge(
    "traffic_rl_accuracy",
    "Traffic RL prediction accuracy percentage"
)


def update_metrics():
    df = pd.read_csv(RESULTS_FILE)

    total = len(df)
    correct = (df["decision"] == df["rl_prediction"]).sum()
    wrong = total - correct
    accuracy = (correct / total) * 100

    traffic_rl_total_records.set(total)
    traffic_rl_correct_predictions.set(correct)
    traffic_rl_wrong_predictions.set(wrong)
    traffic_rl_accuracy.set(accuracy)

    print(
        f"Traffic RL metrics updated | "
        f"Accuracy={accuracy:.2f}% | "
        f"Correct={correct} | Wrong={wrong}"
    )


def run_server():
    start_http_server(8003)

    print("Traffic RL Prometheus metrics running on http://localhost:8003/metrics")

    while True:
        update_metrics()
        time.sleep(5)


if __name__ == "__main__":
    run_server()