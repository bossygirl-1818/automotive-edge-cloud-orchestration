import sqlite3


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "digital_twin_states"


def run_digital_twin_queries():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("\n===== DIGITAL TWIN DATABASE ANALYTICS =====\n")

    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    print("Total Twin States:", cursor.fetchone()[0])

    cursor.execute(f"SELECT ROUND(AVG(vehicle_speed), 2) FROM {TABLE_NAME}")
    print("Average Vehicle Speed:", cursor.fetchone()[0])

    cursor.execute(f"SELECT ROUND(AVG(vehicle_battery), 2) FROM {TABLE_NAME}")
    print("Average Vehicle Battery:", cursor.fetchone()[0])

    cursor.execute(f"SELECT ROUND(AVG(edge_cpu_load), 2) FROM {TABLE_NAME}")
    print("Average Edge CPU Load:", cursor.fetchone()[0])

    cursor.execute(f"SELECT ROUND(AVG(cloud_latency_ms), 2) FROM {TABLE_NAME}")
    print("Average Cloud Latency:", cursor.fetchone()[0])

    print("\nVehicle Health Status:")
    cursor.execute(f"""
        SELECT vehicle_health_status, COUNT(*)
        FROM {TABLE_NAME}
        GROUP BY vehicle_health_status
    """)
    for row in cursor.fetchall():
        print(row[0], ":", row[1])

    print("\nTraffic Density:")
    cursor.execute(f"""
        SELECT traffic_density, COUNT(*)
        FROM {TABLE_NAME}
        GROUP BY traffic_density
    """)
    for row in cursor.fetchall():
        print(row[0], ":", row[1])

    print("\nCongestion Level:")
    cursor.execute(f"""
        SELECT congestion_level, COUNT(*)
        FROM {TABLE_NAME}
        GROUP BY congestion_level
    """)
    for row in cursor.fetchall():
        print(row[0], ":", row[1])

    conn.close()


if __name__ == "__main__":
    run_digital_twin_queries()