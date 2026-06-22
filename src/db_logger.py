from datetime import datetime
from src.database import get_connection


def log_decision(
    ml_decision,
    dqn_decision,
    hybrid_decision,
    selected_engine
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO decisions
    (
        ml_decision,
        dqn_decision,
        hybrid_decision,
        selected_engine,
        timestamp
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        ml_decision,
        dqn_decision,
        hybrid_decision,
        selected_engine,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()