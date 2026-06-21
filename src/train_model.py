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
    "Decision Tree": {
        "model": DecisionTreeClassifier(random_state=42),
        "file": "data/decision_tree.pkl"
    },
    "Random Forest": {
        "model": RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),
        "file": "data/random_forest.pkl"
    },
    "Gradient Boosting": {
        "model": GradientBoostingClassifier(random_state=42),
        "file": "data/gradient_boosting.pkl"
    }
}

results = []

best_accuracy = 0
best_model_name = ""
best_model = None

for name, item in models.items():

    model = item["model"]
    model_file = item["file"]

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    joblib.dump(model, model_file)

    results.append({
        "model": name,
        "accuracy": accuracy,
        "model_file": model_file
    })

    print("\n==============================")
    print(name)
    print("==============================")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Saved Model: {model_file}")
    print(classification_report(y_test, predictions))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model_name = name
        best_model = model

results_df = pd.DataFrame(results)

results_df.to_csv(
    "data/model_comparison.csv",
    index=False
)

joblib.dump(
    best_model,
    "data/orchestrator_model.pkl"
)

print("\n==============================")
print("BEST MODEL SUMMARY")
print("==============================")
print("Best Model:", best_model_name)
print(f"Best Accuracy: {best_accuracy:.4f}")
print("Best model also saved to data/orchestrator_model.pkl")
print("Model comparison saved to data/model_comparison.csv")