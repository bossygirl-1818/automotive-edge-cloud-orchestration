from src.database import get_connection


def sumo_summary():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM sumo_orchestration_tasks"
    )
    total_tasks = cursor.fetchone()[0]

    cursor.execute("""
        SELECT decision, COUNT(*)
        FROM sumo_orchestration_tasks
        GROUP BY decision
    """)
    decisions = cursor.fetchall()

    cursor.execute("""
        SELECT AVG(speed)
        FROM sumo_orchestration_tasks
    """)
    avg_speed = round(cursor.fetchone()[0], 2)

    cursor.execute("""
        SELECT AVG(battery)
        FROM sumo_orchestration_tasks
    """)
    avg_battery = round(cursor.fetchone()[0], 2)

    conn.close()

    print("\n===== SUMO DATABASE SUMMARY =====\n")

    print("Total Tasks:", total_tasks)

    print("\nDecision Distribution:")
    for row in decisions:
        print(row[0], ":", row[1])

    print("\nAverage Speed:", avg_speed)
    print("Average Battery:", avg_battery)


if __name__ == "__main__":
    sumo_summary()