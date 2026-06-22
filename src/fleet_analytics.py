import pandas as pd


RESULT_FILE = "data/fleet_simulation_results.csv"


def analyze_fleet():

    df = pd.read_csv(RESULT_FILE)

    print("\n===== FLEET SIMULATION ANALYSIS =====\n")

    print(f"Total Fleet Tasks: {len(df)}")
    print(f"Vehicles Simulated: {df['vehicle_id'].nunique()}")
    print(f"Average Queue Wait Time: {df['queue_wait_time'].mean():.2f}")
    print(f"Average Processing Time: {df['processing_time'].mean():.2f}")
    print(f"Average Total Completion Time: {df['total_time'].mean():.2f}")

    print("\nTask Distribution by Decision:")
    print(df["decision"].value_counts())

    print("\nTasks Per Vehicle:")
    print(df["vehicle_id"].value_counts().sort_index())

    print("\nAverage Completion Time Per Vehicle:")
    print(df.groupby("vehicle_id")["total_time"].mean())


if __name__ == "__main__":
    analyze_fleet()