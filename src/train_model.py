import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("data/training_data.csv")

# Features
X = df[
    [
        "vehicle_cpu",
        "battery",
        "edge_delay",
        "cloud_delay",
        "task_latency"
    ]
]

# Target
y = df["decision"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = DecisionTreeClassifier()

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy:.4f}")

# Save model
joblib.dump(model, "data/orchestrator_model.pkl")

print("\nModel saved successfully!")