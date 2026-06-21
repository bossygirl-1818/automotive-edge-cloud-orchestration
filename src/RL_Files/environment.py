import random
import numpy as np


class AutomotiveEnv:
    """
    Deep RL environment for automotive edge-cloud task orchestration.

    Actions:
    0 = VEHICLE
    1 = EDGE
    2 = CLOUD
    """

    def __init__(self):
        self.action_space = 3
        self.state_size = 11
        self.current_state = None

    def reset(self):
        self.current_state = self._generate_state()
        return self.current_state

    def _generate_state(self):
        vehicle_cpu = random.uniform(30, 95)
        battery = random.uniform(10, 100)
        vehicle_speed = random.uniform(0, 120)
        traffic_density = random.uniform(1, 100)

        edge_delay = random.uniform(5, 50)
        edge_bandwidth = random.uniform(20, 100)

        cloud_delay = random.uniform(60, 180)
        cloud_bandwidth = random.uniform(50, 200)

        task_latency = random.choice([10, 15, 50, 150, 300])
        task_priority = random.choice([1, 2, 3])
        task_size = random.choice([5, 10, 15, 20, 25])

        state = np.array([
            vehicle_cpu / 100,
            battery / 100,
            vehicle_speed / 120,
            traffic_density / 100,
            edge_delay / 100,
            edge_bandwidth / 200,
            cloud_delay / 200,
            cloud_bandwidth / 200,
            task_latency / 300,
            task_priority / 3,
            task_size / 25
        ], dtype=np.float32)

        raw = {
            "vehicle_cpu": vehicle_cpu,
            "battery": battery,
            "vehicle_speed": vehicle_speed,
            "traffic_density": traffic_density,
            "edge_delay": edge_delay,
            "edge_bandwidth": edge_bandwidth,
            "cloud_delay": cloud_delay,
            "cloud_bandwidth": cloud_bandwidth,
            "task_latency": task_latency,
            "task_priority": task_priority,
            "task_size": task_size
        }

        return state, raw

    def step(self, action):
        state, raw = self.current_state

        reward = self._calculate_reward(action, raw)

        next_state = self._generate_state()
        done = False
        self.current_state = next_state

        return next_state, reward, done, raw

    def _calculate_reward(self, action, raw):
        latency = raw["task_latency"]
        priority = raw["task_priority"]
        vehicle_cpu = raw["vehicle_cpu"]
        battery = raw["battery"]
        edge_delay = raw["edge_delay"]
        cloud_delay = raw["cloud_delay"]

        reward = 0

        # Safety-critical tasks: VEHICLE is best
        if latency <= 20:
            if action == 0:
                reward += 100

                if vehicle_cpu < 85:
                    reward += 30

                if battery > 20:
                    reward += 20

            elif action == 1:
                reward -= 50

            else:
                reward -= 100

        # Medium-latency tasks: EDGE is best
        elif latency <= 150:
            if action == 1:
                reward += 100

                if edge_delay < 40:
                    reward += 20

            elif action == 0:
                reward += 20

            else:
                reward -= 30

        # Low-priority / high-latency tasks: CLOUD is best
        else:
            if action == 2:
                reward += 100

                if cloud_delay < 150:
                    reward += 20

            elif action == 1:
                reward += 20

            else:
                reward -= 40

        reward += (4 - priority) * 5

        return reward