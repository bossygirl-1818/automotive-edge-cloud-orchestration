import pandas as pd

from src.database import get_connection, create_tables


CSV_FILE = "data/sumo_advanced_orchestration.csv"
TABLE_NAME = "advanced_traffic_tasks"


def load_advanced_traffic_to_db():

    create_tables()

    df = pd.read_csv(CSV_FILE)

    conn = get_connection()

    df.to_sql(
        TABLE_NAME,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Advanced traffic data loaded into SQLite.")
    print(f"Table name: {TABLE_NAME}")
    print(f"Total records loaded: {len(df)}")


if __name__ == "__main__":
    load_advanced_traffic_to_db()