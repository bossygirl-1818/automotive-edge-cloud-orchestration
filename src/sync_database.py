import pandas as pd

from src.database import get_connection, create_tables


def sync_telemetry():
    df = pd.read_csv("data/vehicle_telemetry.csv")
    conn = get_connection()

    df.to_sql(
        "telemetry",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()
    print("Telemetry synced to database.")


def sync_rl_rewards():
    df = pd.read_csv("data/rl_reward_history.csv")
    conn = get_connection()

    df.to_sql(
        "rl_rewards",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()
    print("RL rewards synced to database.")


def sync_all():
    create_tables()
    sync_telemetry()
    sync_rl_rewards()
    print("Database sync completed.")


if __name__ == "__main__":
    sync_all()