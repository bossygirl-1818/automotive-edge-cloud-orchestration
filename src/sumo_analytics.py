import pandas as pd

df = pd.read_csv("data/sumo_orchestration_tasks.csv")

print("\n===== SUMO ORCHESTRATION ANALYTICS =====\n")

print("Total Tasks:", len(df))

print("\nDecision Distribution:")
print(df["decision"].value_counts())

print("\nTask Type Distribution:")
print(df["task_type"].value_counts())

print("\nTraffic Density Distribution:")
print(df["traffic_density"].value_counts())

print("\nNetwork Quality Distribution:")
print(df["network_quality"].value_counts())

print("\nAverage Vehicle Speed:")
print(round(df["speed"].mean(), 2))

print("\nAverage Battery Level:")
print(round(df["battery"].mean(), 2))