import torch
import numpy as np

from src.RL_Files.environment import AutomotiveEnv
from src.RL_Files.dqn_agent import DQNAgent


ACTION_MAP = {
    0: "VEHICLE",
    1: "EDGE",
    2: "CLOUD"
}


class RLOrchestrator:
    def __init__(self, model_path="data/dqn_orchestrator.pth"):
        self.env = AutomotiveEnv()

        self.agent = DQNAgent(
            state_size=self.env.state_size,
            action_size=self.env.action_space
        )

        self.agent.load(model_path)
        self.agent.epsilon = 0.0

    def predict(self):
        state, raw = self.env.reset()

        state_tensor = torch.FloatTensor(
            np.array(state)
        ).unsqueeze(0).to(self.agent.device)

        with torch.no_grad():
            q_values = self.agent.model(state_tensor)

        action = torch.argmax(q_values).item()
        decision = ACTION_MAP[action]

        return {
            "decision": decision,
            "q_values": q_values.cpu().numpy().flatten().tolist(),
            "task_latency": raw["task_latency"],
            "task_priority": raw["task_priority"],
            "task_size": raw["task_size"],
            "vehicle_cpu": raw["vehicle_cpu"],
            "battery": raw["battery"],
            "edge_delay": raw["edge_delay"],
            "cloud_delay": raw["cloud_delay"]
        }