import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report


df = pd.read_csv("data/training_data.csv")

features = [
    "vehicle_cpu",
    "battery",
    "vehicle_speed",
    "traffic_density",
    "edge_delay",
    "edge_bandwidth",
    "cloud_delay",
    "cloud_bandwidth",
    "task_latency",
    "task_priority",
    "task_size"
]

X = df[features]
y = df["decision"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

results = []

best_model = None
best_accuracy = 0
best_model_name = ""

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    results.append({
        "model": name,
        "accuracy": accuracy
    })

    print("\n==============================")
    print(name)
    print("==============================")
    print(f"Accuracy: {accuracy:.4f}")
    print(classification_report(y_test, predictions))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_model_name = name

results_df = pd.DataFrame(results)
results_df.to_csv("data/model_comparison.csv", index=False)

joblib.dump(best_model, "data/orchestrator_model.pkl")

print("\nBest Model:", best_model_name)
print(f"Best Accuracy: {best_accuracy:.4f}")
print("Best model saved to data/orchestrator_model.pkl")
print("Model comparison saved to data/model_comparison.csv")