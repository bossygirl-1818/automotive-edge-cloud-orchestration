import pandas as pd


FILE_PATH = "data/sumo_advanced_orchestration.csv"


def run_analytics():

    df = pd.read_csv(FILE_PATH)

    print("\n===== ADVANCED TRAFFIC ORCHESTRATION ANALYTICS =====\n")

    print("Total Records:", len(df))
    print("Vehicles:", df["vehicle_id"].nunique())

    print("\nDecision Distribution:")
    print(df["decision"].value_counts())

    print("\nTraffic Density Distribution:")
    print(df["traffic_density"].value_counts())

    print("\nNetwork Quality Distribution:")
    print(df["network_quality"].value_counts())

    print("\nTask Type Distribution:")
    print(df["task_type"].value_counts())

    print("\nAverage Speed:")
    print(round(df["speed"].mean(), 2))

    print("\nAverage Battery:")
    print(round(df["battery"].mean(), 2))

    print("\nDecision by Traffic Density:")
    print(pd.crosstab(df["traffic_density"], df["decision"]))

    print("\nDecision by Network Quality:")
    print(pd.crosstab(df["network_quality"], df["decision"]))


if __name__ == "__main__":
    run_analytics()