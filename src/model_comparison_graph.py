import pandas as pd
import matplotlib.pyplot as plt


def create_model_comparison_graph():
    df = pd.read_csv("data/model_comparison.csv")

    plt.figure(figsize=(7, 5))
    plt.bar(df["model"], df["accuracy"] * 100)

    plt.title("ML Model Accuracy Comparison")
    plt.ylabel("Accuracy (%)")
    plt.xlabel("Model")

    plt.ylim(95, 100.5)

    plt.savefig(
        "data/model_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    print("Graph saved: data/model_comparison.png")


if __name__ == "__main__":
    create_model_comparison_graph()