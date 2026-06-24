import sqlite3
import pandas as pd


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "explainable_orchestration_history"


def run_xai_analytics():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    conn.close()

    if df.empty:
        print("No XAI history found.")
        print("Run: python -m src.explainable_orchestrator_history")
        return

    print("\n===== EXPLAINABLE ORCHESTRATOR ANALYTICS =====\n")

    print("Total XAI Records:", len(df))

    print("\nDecision Distribution:")
    print(df["decision"].value_counts())

    print("\nTraffic Density Distribution:")
    print(df["traffic_density"].value_counts())

    print("\nAverage Battery:")
    print(round(df["battery"].mean(), 2))

    print("\nAverage Speed:")
    print(round(df["speed"].mean(), 2))

    print("\nMost Common Explanation Patterns:")
    print(df["explanation"].value_counts().head(5))


if __name__ == "__main__":
    run_xai_analytics()