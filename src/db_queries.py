import sqlite3
import pandas as pd

DB_PATH = "data/orchestrator.db"


def get_rl_rewards():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM rl_rewards",
        conn
    )

    conn.close()

    return df


def get_telemetry():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM telemetry",
        conn
    )

    conn.close()

    return df


def get_decisions():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM decisions",
        conn
    )

    conn.close()

    return df


def get_tasks():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM tasks",
        conn
    )

    conn.close()

    return df