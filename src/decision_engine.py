class DecisionEngine:

    def decide(self, task, vehicle, edge, cloud):

        latency = task["latency_requirement"]

        # Safety-critical tasks
        if latency <= 20:

            # Vehicle overloaded or battery too low
            if vehicle["cpu_usage"] > 85 or vehicle["battery_level"] < 20:
                return "EDGE"

            return "VEHICLE"

        # Medium-priority tasks
        elif latency <= 100:

            if edge["network_delay"] < 40:
                return "EDGE"

            return "CLOUD"

        # Low-priority tasks
        else:

            if cloud["network_delay"] < 120:
                return "CLOUD"

            return "EDGE"