class DecisionEngine:

    def decide(self, task):

        latency = task["latency_requirement"]

        if latency <= 20:
            return "VEHICLE"

        elif latency <= 100:
            return "EDGE"

        else:
            return "CLOUD"