import sqlite3
import os


DB_PATH = "data/orchestrator.db"


def get_connection():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS telemetry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        episode INTEGER,
        vehicle_cpu REAL,
        battery REAL,
        edge_load REAL,
        cloud_load REAL,
        network_latency REAL,
        edge_delay REAL,
        cloud_delay REAL,
        decision TEXT,
        timestamp TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rl_rewards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        episode INTEGER,
        reward REAL,
        decision TEXT,
        latency REAL,
        battery REAL,
        edge_delay REAL,
        cloud_delay REAL,
        task_size REAL,
        priority INTEGER,
        timestamp TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS decisions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ml_decision TEXT,
        dqn_decision TEXT,
        hybrid_decision TEXT,
        selected_engine TEXT,
        timestamp TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id TEXT,
        task_type TEXT,
        priority INTEGER,
        latency REAL,
        task_size REAL,
        predicted_location TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("Database and tables created successfully.")


if __name__ == "__main__":
    create_tables()