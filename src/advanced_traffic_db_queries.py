from src.database import get_connection


TABLE_NAME = "advanced_traffic_tasks"


def run_advanced_traffic_db_queries():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n===== ADVANCED TRAFFIC DATABASE ANALYTICS =====\n")

    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    print("Total Records:", cursor.fetchone()[0])

    cursor.execute(f"SELECT COUNT(DISTINCT vehicle_id) FROM {TABLE_NAME}")
    print("Vehicles:", cursor.fetchone()[0])

    cursor.execute(f"SELECT ROUND(AVG(speed), 2) FROM {TABLE_NAME}")
    print("Average Speed:", cursor.fetchone()[0])

    cursor.execute(f"SELECT ROUND(AVG(battery), 2) FROM {TABLE_NAME}")
    print("Average Battery:", cursor.fetchone()[0])

    print("\nDecision Distribution:")
    cursor.execute(f"""
        SELECT decision, COUNT(*)
        FROM {TABLE_NAME}
        GROUP BY decision
    """)
    for row in cursor.fetchall():
        print(row[0], ":", row[1])

    print("\nTraffic Density Distribution:")
    cursor.execute(f"""
        SELECT traffic_density, COUNT(*)
        FROM {TABLE_NAME}
        GROUP BY traffic_density
    """)
    for row in cursor.fetchall():
        print(row[0], ":", row[1])

    print("\nNetwork Quality Distribution:")
    cursor.execute(f"""
        SELECT network_quality, COUNT(*)
        FROM {TABLE_NAME}
        GROUP BY network_quality
    """)
    for row in cursor.fetchall():
        print(row[0], ":", row[1])

    print("\nDecision by Traffic Density:")
    cursor.execute(f"""
        SELECT traffic_density, decision, COUNT(*)
        FROM {TABLE_NAME}
        GROUP BY traffic_density, decision
        ORDER BY traffic_density, decision
    """)
    for row in cursor.fetchall():
        print(row[0], "-", row[1], ":", row[2])

    conn.close()


if __name__ == "__main__":
    run_advanced_traffic_db_queries()