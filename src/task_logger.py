from datetime import datetime
from src.database import get_connection


def log_task(
    task_id,
    task_type,
    priority,
    latency,
    task_size,
    predicted_location
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks
    (
        task_id,
        task_type,
        priority,
        latency,
        task_size,
        predicted_location,
        timestamp
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        task_id,
        task_type,
        priority,
        latency,
        task_size,
        predicted_location,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()