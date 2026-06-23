import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("data/sumo_visualizations", exist_ok=True)

df = pd.read_csv("data/sumo_orchestration_tasks.csv")

# Decision Distribution
plt.figure(figsize=(8,5))
df["decision"].value_counts().plot(kind="bar")
plt.title("Offloading Decision Distribution")
plt.tight_layout()
plt.savefig("data/sumo_visualizations/decision_distribution.png")
plt.close()

# Task Types
plt.figure(figsize=(10,5))
df["task_type"].value_counts().plot(kind="bar")
plt.title("Task Type Distribution")
plt.tight_layout()
plt.savefig("data/sumo_visualizations/task_types.png")
plt.close()

# Traffic Density
plt.figure(figsize=(8,5))
df["traffic_density"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Traffic Density Distribution")
plt.savefig("data/sumo_visualizations/traffic_density.png")
plt.close()

# Speed Distribution
plt.figure(figsize=(8,5))
plt.hist(df["speed"], bins=20)
plt.title("Vehicle Speed Distribution")
plt.tight_layout()
plt.savefig("data/sumo_visualizations/speed_distribution.png")
plt.close()

print("SUMO visualizations generated successfully.")