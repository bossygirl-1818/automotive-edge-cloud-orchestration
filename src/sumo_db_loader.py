import pandas as pd

from src.database import get_connection, create_tables


SUMO_FILE = "data/sumo_orchestration_tasks.csv"


def load_sumo_tasks_to_db():
    create_tables()

    df = pd.read_csv(SUMO_FILE)

    conn = get_connection()

    df.to_sql(
        "sumo_orchestration_tasks",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("SUMO orchestration tasks loaded into SQLite.")
    print(f"Total records loaded: {len(df)}")


if __name__ == "__main__":
    load_sumo_tasks_to_db()