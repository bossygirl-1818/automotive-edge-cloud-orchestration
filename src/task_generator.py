import random

TASK_TYPES = [
    {
        "name": "lane_detection",
        "latency": 10,
        "cpu": 50,
        "memory": 100,
        "priority": 3,
        "task_size": 20
    },
    {
        "name": "obstacle_detection",
        "latency": 15,
        "cpu": 60,
        "memory": 120,
        "priority": 3,
        "task_size": 25
    },
    {
        "name": "traffic_sign_recognition",
        "latency": 50,
        "cpu": 40,
        "memory": 80,
        "priority": 2,
        "task_size": 15
    },
    {
        "name": "route_planning",
        "latency": 150,
        "cpu": 30,
        "memory": 60,
        "priority": 2,
        "task_size": 10
    },
    {
        "name": "vehicle_diagnostics",
        "latency": 300,
        "cpu": 20,
        "memory": 40,
        "priority": 1,
        "task_size": 5
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
            "memory_requirement": task["memory"],
            "task_priority": task["priority"],
            "task_size": task["task_size"]
        }