import json
import sqlite3


DB_PATH = "data/orchestrator.db"
XAI_FILE = "data/explainable_orchestration_result.json"


def create_xai_history_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS explainable_orchestration_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            vehicle_id TEXT,
            decision TEXT,
            traffic_density TEXT,
            network_quality TEXT,
            battery REAL,
            speed REAL,
            task_type TEXT,
            explanation TEXT
        )
    """)

    conn.commit()
    conn.close()


def store_xai_history():
    create_xai_history_table()

    with open(XAI_FILE, "r") as file:
        result = json.load(file)

    state = result["rl_state"]
    explanation_text = " | ".join(result["explanation"])

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO explainable_orchestration_history (
            timestamp,
            vehicle_id,
            decision,
            traffic_density,
            network_quality,
            battery,
            speed,
            task_type,
            explanation
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        result["timestamp"],
        result["vehicle_id"],
        result["decision"],
        state["traffic_density"],
        state["network_quality"],
        state["battery"],
        state["speed"],
        state["task_type"],
        explanation_text
    ))

    conn.commit()
    conn.close()

    print("Explainable orchestration history stored successfully.")


if __name__ == "__main__":
    store_xai_history()