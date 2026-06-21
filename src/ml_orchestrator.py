import joblib
import pandas as pd


class MLOrchestrator:

    def __init__(self):
        self.model = joblib.load("data/orchestrator_model.pkl")

    def decide(
        self,
        vehicle_cpu,
        battery,
        edge_delay,
        cloud_delay,
        task_latency
    ):

        data = pd.DataFrame([{
            "vehicle_cpu": vehicle_cpu,
            "battery": battery,
            "edge_delay": edge_delay,
            "cloud_delay": cloud_delay,
            "task_latency": task_latency
        }])

        prediction = self.model.predict(data)

        return prediction[0]