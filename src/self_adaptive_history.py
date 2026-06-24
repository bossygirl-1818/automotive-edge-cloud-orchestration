import json
import sqlite3


DB_PATH = "data/orchestrator.db"
DECISION_FILE = "data/self_adaptive_decision.json"


def create_self_adaptive_history_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS self_adaptive_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            vehicle_id TEXT,
            traffic_density TEXT,
            network_quality TEXT,
            battery REAL,
            speed REAL,
            task_type TEXT,
            rl_decision TEXT,
            final_decision TEXT,
            adaptation_reason TEXT,
            explanation TEXT
        )
    """)

    conn.commit()
    conn.close()


def store_self_adaptive_history():
    create_self_adaptive_history_table()

    with open(DECISION_FILE, "r") as file:
        result = json.load(file)

    state = result["rl_state"]
    explanation_text = " | ".join(result["explanation"])

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO self_adaptive_history (
            timestamp,
            vehicle_id,
            traffic_density,
            network_quality,
            battery,
            speed,
            task_type,
            rl_decision,
            final_decision,
            adaptation_reason,
            explanation
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        result["timestamp"],
        result["vehicle_id"],
        state["traffic_density"],
        state["network_quality"],
        state["battery"],
        state["speed"],
        state["task_type"],
        result["rl_decision"],
        result["final_decision"],
        result["adaptation_reason"],
        explanation_text
    ))

    conn.commit()
    conn.close()

    print("Self-adaptive decision history stored successfully.")


if __name__ == "__main__":
    store_self_adaptive_history()