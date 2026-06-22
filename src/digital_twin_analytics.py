import os
import pandas as pd


RESULT_FILE = "data/digital_twin_results.csv"


def analyze_digital_twin():

    if not os.path.exists(RESULT_FILE):
        print("Digital twin results file not found.")
        print("Run: python -m src.digital_twin")
        return

    df = pd.read_csv(RESULT_FILE)

    print("\n===== DIGITAL TWIN ANALYSIS =====\n")

    print(f"Total Tasks: {len(df)}")
    print(f"Average Queue Wait Time: {df['queue_wait_time'].mean():.2f}")
    print(f"Average Processing Time: {df['processing_time'].mean():.2f}")
    print(f"Average Total Time: {df['total_time'].mean():.2f}")

    print("\nTask Distribution:")
    print(df["decision"].value_counts())

    print("\nFirst 5 Records:")
    print(df.head())


if __name__ == "__main__":
    analyze_digital_twin()