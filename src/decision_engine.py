class DecisionEngine:

    def decide(self, task, vehicle, edge, cloud):

        latency = task["latency_requirement"]
        priority = task["task_priority"]
        task_size = task["task_size"]

        vehicle_cpu = vehicle["cpu_usage"]
        battery = vehicle["battery_level"]
        speed = vehicle["vehicle_speed"]
        traffic = vehicle["traffic_density"]

        edge_delay = edge["network_delay"]
        edge_bandwidth = edge["network_bandwidth"]

        cloud_delay = cloud["network_delay"]
        cloud_bandwidth = cloud["network_bandwidth"]

        # High-priority safety-critical tasks
        if priority == 3 or latency <= 20:

            if (
                vehicle_cpu < 85
                and battery > 20
                and traffic < 80
            ):
                return "VEHICLE"

            if edge_delay < 30 and edge_bandwidth > task_size:
                return "EDGE"

            return "VEHICLE"

        # Medium-priority tasks
        if priority == 2 or latency <= 100:

            if edge_delay < 40 and edge_bandwidth > task_size:
                return "EDGE"

            if cloud_delay < 130 and cloud_bandwidth > task_size:
                return "CLOUD"

            return "VEHICLE"

        # Low-priority tasks
        if priority == 1:

            if cloud_delay < 150 and cloud_bandwidth > task_size:
                return "CLOUD"

            if edge_delay < 50:
                return "EDGE"

            return "VEHICLE"