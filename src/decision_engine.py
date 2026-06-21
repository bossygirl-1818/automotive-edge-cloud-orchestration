class DecisionEngine:

    def decide(self, task, vehicle, edge, cloud):

        task_type = task["task_type"]
        priority = task["task_priority"]
        task_size = task["task_size"]
        latency = task["latency_requirement"]

        vehicle_cpu = vehicle["cpu_usage"]
        battery = vehicle["battery_level"]
        vehicle_speed = vehicle["vehicle_speed"]
        traffic_density = vehicle["traffic_density"]

        edge_delay = edge["network_delay"]
        edge_bandwidth = edge["network_bandwidth"]
        edge_cpu = edge["cpu_usage"]

        cloud_delay = cloud["network_delay"]
        cloud_bandwidth = cloud["network_bandwidth"]
        cloud_cpu = cloud["cpu_usage"]

        # 1. Safety-critical tasks must prefer onboard vehicle
        if task_type in ["lane_detection", "obstacle_detection"]:

            if vehicle_cpu <= 85 and battery >= 20:
                return "VEHICLE"

            if edge_delay <= 25 and edge_bandwidth >= task_size and edge_cpu <= 75:
                return "EDGE"

            return "VEHICLE"

        # 2. Medium-priority perception/navigation tasks prefer edge
        if task_type in ["traffic_sign_recognition", "route_planning"]:

            if edge_delay <= 45 and edge_bandwidth >= task_size and edge_cpu <= 80:
                return "EDGE"

            if vehicle_cpu <= 60 and battery >= 40 and traffic_density <= 60:
                return "VEHICLE"

            if cloud_delay <= 130 and cloud_bandwidth >= task_size and cloud_cpu <= 70:
                return "CLOUD"

            return "EDGE"

        # 3. Low-priority diagnostics prefer cloud
        if task_type == "vehicle_diagnostics":

            if cloud_delay <= 150 and cloud_bandwidth >= task_size and cloud_cpu <= 75:
                return "CLOUD"

            if edge_delay <= 50 and edge_bandwidth >= task_size:
                return "EDGE"

            return "VEHICLE"

        # 4. Fallback rule
        if latency <= 20:
            return "VEHICLE"

        if latency <= 150:
            return "EDGE"

        return "CLOUD"