import random

TASK_TYPES = [
    {
        "name": "lane_detection",
        "latency": 10,
        "cpu": 50,
        "memory": 100
    },
    {
        "name": "obstacle_detection",
        "latency": 15,
        "cpu": 60,
        "memory": 120
    },
    {
        "name": "traffic_sign_recognition",
        "latency": 50,
        "cpu": 40,
        "memory": 80
    },
    {
        "name": "route_planning",
        "latency": 150,
        "cpu": 30,
        "memory": 60
    },
    {
        "name": "vehicle_diagnostics",
        "latency": 300,
        "cpu": 20,
        "memory": 40
    }
]


class TaskGenerator:

    def generate_task(self, task_id):

        task = random.choice(TASK_TYPES)

        return {
            "task_id": task_id,
            "task_type": task["name"],
            "latency_requirement": task["latency"],
            "cpu_requirement": task["cpu"],
            "memory_requirement": task["memory"]
        }