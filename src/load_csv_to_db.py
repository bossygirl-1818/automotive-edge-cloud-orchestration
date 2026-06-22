import pandas as pd

from src.database import get_connection, create_tables


def load_telemetry():
    df = pd.read_csv("data/vehicle_telemetry.csv")

    conn = get_connection()
    df.to_sql(
        "telemetry",
        conn,
        if_exists="replace",
        index=False
    )
    conn.close()

    print("Telemetry data loaded.")


def load_rl_rewards():
    df = pd.read_csv("data/rl_reward_history.csv")

    conn = get_connection()
    df.to_sql(
        "rl_rewards",
        conn,
        if_exists="replace",
        index=False
    )
    conn.close()

    print("RL reward data loaded.")


def main():
    create_tables()
    load_telemetry()
    load_rl_rewards()

    print("CSV data successfully migrated to SQLite database.")


if __name__ == "__main__":
    main()