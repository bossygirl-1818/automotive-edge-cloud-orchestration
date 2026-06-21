import random


class ResourceMonitor:

    def get_vehicle_resources(self):
        return {
            "cpu_usage": random.randint(40, 95),
            "memory_usage": random.randint(30, 85),
            "battery_level": random.randint(10, 100),
            "vehicle_speed": random.randint(0, 120),
            "traffic_density": random.randint(1, 100)
        }

    def get_edge_resources(self):
        return {
            "cpu_usage": random.randint(20, 80),
            "memory_usage": random.randint(20, 70),
            "network_delay": random.randint(5, 50),
            "network_bandwidth": random.randint(20, 100)
        }

    def get_cloud_resources(self):
        return {
            "cpu_usage": random.randint(10, 60),
            "memory_usage": random.randint(10, 50),
            "network_delay": random.randint(60, 180),
            "network_bandwidth": random.randint(50, 200)
        }