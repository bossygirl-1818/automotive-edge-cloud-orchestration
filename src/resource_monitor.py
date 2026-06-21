import random


class ResourceMonitor:

    def get_vehicle_resources(self):
        return {
            "cpu_usage": random.randint(40, 90),
            "memory_usage": random.randint(30, 80),
            "battery_level": random.randint(20, 100)
        }

    def get_edge_resources(self):
        return {
            "cpu_usage": random.randint(20, 70),
            "memory_usage": random.randint(20, 60),
            "network_delay": random.randint(5, 30)
        }

    def get_cloud_resources(self):
        return {
            "cpu_usage": random.randint(10, 50),
            "memory_usage": random.randint(10, 40),
            "network_delay": random.randint(50, 150)
        }