import os
import pandas as pd
import plotly.express as px


RESULT_FILE = "data/fleet_simulation_results.csv"
OUTPUT_DIR = "data/fleet_visualizations"


def create_fleet_visualizations():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = pd.read_csv(RESULT_FILE)

    # 1. Task Distribution
    decision_counts = (
        df["decision"]
        .value_counts()
        .reset_index()
    )

    decision_counts.columns = ["Decision", "Count"]

    fig1 = px.pie(
        decision_counts,
        names="Decision",
        values="Count",
        title="Fleet Task Distribution Across Vehicle, Edge and Cloud",
        hole=0.45
    )

    fig1.write_html(
        f"{OUTPUT_DIR}/fleet_task_distribution.html"
    )

    # 2. Tasks Per Vehicle
    vehicle_counts = (
        df["vehicle_id"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    vehicle_counts.columns = ["Vehicle ID", "Task Count"]

    fig2 = px.bar(
        vehicle_counts,
        x="Vehicle ID",
        y="Task Count",
        title="Tasks Generated Per Vehicle"
    )

    fig2.write_html(
        f"{OUTPUT_DIR}/tasks_per_vehicle.html"
    )

    # 3. Average Completion Time Per Vehicle
    avg_completion = (
        df.groupby("vehicle_id")["total_time"]
        .mean()
        .reset_index()
    )

    avg_completion.columns = [
        "Vehicle ID",
        "Average Completion Time"
    ]

    fig3 = px.bar(
        avg_completion,
        x="Vehicle ID",
        y="Average Completion Time",
        title="Average Task Completion Time Per Vehicle"
    )

    fig3.write_html(
        f"{OUTPUT_DIR}/avg_completion_time_per_vehicle.html"
    )

    # 4. Queue Wait Time Distribution
    fig4 = px.box(
        df,
        x="decision",
        y="queue_wait_time",
        title="Queue Wait Time by Execution Location"
    )

    fig4.write_html(
        f"{OUTPUT_DIR}/queue_wait_time_distribution.html"
    )

    print("Fleet visualizations generated successfully.")
    print(f"Saved inside: {OUTPUT_DIR}")


if __name__ == "__main__":
    create_fleet_visualizations()