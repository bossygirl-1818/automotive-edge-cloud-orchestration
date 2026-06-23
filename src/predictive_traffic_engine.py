import sqlite3
import pandas as pd


DB_PATH = "data/orchestrator.db"
OUTPUT_FILE = "data/predictive_traffic_forecast.csv"


def classify_prediction(value, low_threshold, high_threshold):
    if value < low_threshold:
        return "LOW"
    elif value < high_threshold:
        return "MEDIUM"
    return "HIGH"


def generate_predictive_forecast():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM digital_twin_states ORDER BY id",
        conn
    )

    conn.close()

    if df.empty:
        print("No digital twin data found.")
        print("Run: python -m src.digital_twin_collector")
        return

    latest = df.tail(10)

    avg_speed = latest["vehicle_speed"].mean()
    avg_edge_cpu = latest["edge_cpu_load"].mean()
    avg_cloud_latency = latest["cloud_latency_ms"].mean()
    avg_battery = latest["vehicle_battery"].mean()
    avg_active_vehicles = latest["active_vehicles"].mean()

    predicted_congestion_score = (
        (avg_active_vehicles * 1.5)
        + (100 - avg_speed) * 0.4
        + avg_edge_cpu * 0.2
    )

    predicted_edge_load = min(
        100,
        avg_edge_cpu + (avg_active_vehicles * 0.6)
    )

    predicted_cloud_latency = min(
        200,
        avg_cloud_latency + (predicted_edge_load * 0.4)
    )

    predicted_battery_drain = max(
        0,
        100 - avg_battery
    )

    forecast = {
        "avg_recent_speed": round(avg_speed, 2),
        "avg_recent_edge_cpu": round(avg_edge_cpu, 2),
        "avg_recent_cloud_latency": round(avg_cloud_latency, 2),
        "avg_recent_battery": round(avg_battery, 2),
        "avg_recent_active_vehicles": round(avg_active_vehicles, 2),

        "predicted_congestion_score": round(predicted_congestion_score, 2),
        "predicted_congestion_level": classify_prediction(
            predicted_congestion_score,
            45,
            75
        ),

        "predicted_edge_load": round(predicted_edge_load, 2),
        "predicted_edge_risk": classify_prediction(
            predicted_edge_load,
            50,
            80
        ),

        "predicted_cloud_latency": round(predicted_cloud_latency, 2),
        "predicted_cloud_risk": classify_prediction(
            predicted_cloud_latency,
            80,
            130
        ),

        "predicted_battery_drain": round(predicted_battery_drain, 2),
        "predicted_battery_risk": classify_prediction(
            predicted_battery_drain,
            30,
            60
        )
    }

    forecast_df = pd.DataFrame([forecast])

    forecast_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\n===== PREDICTIVE TRAFFIC INTELLIGENCE =====\n")
    print(forecast_df.T)

    print("\nForecast saved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    generate_predictive_forecast()