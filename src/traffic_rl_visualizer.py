import os
import pandas as pd
import plotly.express as px


RESULTS_FILE = "data/traffic_rl_evaluation_results.csv"
OUTPUT_DIR = "data/traffic_rl_visualizations"


def generate_rl_visualizations():

    if not os.path.exists(RESULTS_FILE):
        print("Evaluation results not found.")
        print("Run: python -m src.traffic_rl_evaluator")
        return

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )

    df = pd.read_csv(RESULTS_FILE)

    prediction_counts = (
        df["rl_prediction"]
        .value_counts()
        .reset_index()
    )

    prediction_counts.columns = [
        "Decision",
        "Count"
    ]

    fig1 = px.pie(
        prediction_counts,
        names="Decision",
        values="Count",
        title="RL Prediction Distribution",
        hole=0.55
    )

    fig1.write_html(
        f"{OUTPUT_DIR}/prediction_distribution.html"
    )

    actual_vs_predicted = pd.crosstab(
        df["decision"],
        df["rl_prediction"]
    )

    fig2 = px.imshow(
        actual_vs_predicted,
        text_auto=True,
        title="Actual vs Predicted Decisions"
    )

    fig2.write_html(
        f"{OUTPUT_DIR}/actual_vs_predicted.html"
    )

    accuracy = (
        (df["decision"] == df["rl_prediction"])
        .mean()
        * 100
    )

    accuracy_df = pd.DataFrame({
        "Metric": ["Accuracy"],
        "Value": [accuracy]
    })

    fig3 = px.bar(
        accuracy_df,
        x="Metric",
        y="Value",
        title="Traffic RL Accuracy (%)"
    )

    fig3.write_html(
        f"{OUTPUT_DIR}/accuracy.html"
    )

    print(
        "Traffic RL visualizations generated successfully."
    )

    print(
        f"Saved inside: {OUTPUT_DIR}"
    )


if __name__ == "__main__":
    generate_rl_visualizations()