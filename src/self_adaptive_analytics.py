import sqlite3
import pandas as pd


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "self_adaptive_history"


def run_self_adaptive_analytics():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    conn.close()

    if df.empty:
        print("No self-adaptive history found.")
        print("Run: python -m src.self_adaptive_history")
        return

    overrides = df[df["rl_decision"] != df["final_decision"]]
    override_rate = (len(overrides) / len(df)) * 100

    print("\n===== SELF-ADAPTIVE CONTROLLER ANALYTICS =====\n")

    print("Total Adaptive Records:", len(df))

    print("\nRL Decision Distribution:")
    print(df["rl_decision"].value_counts())

    print("\nFinal Decision Distribution:")
    print(df["final_decision"].value_counts())

    print("\nOverride Count:", len(overrides))
    print(f"Override Rate: {override_rate:.2f}%")

    print("\nMost Common Adaptation Reasons:")
    print(df["adaptation_reason"].value_counts().head(5))


if __name__ == "__main__":
    run_self_adaptive_analytics()