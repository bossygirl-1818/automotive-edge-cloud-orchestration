import random


class ExecutionSimulator:

    def execute(self, destination):

        if destination == "VEHICLE":
            latency = random.randint(5, 20)

        elif destination == "EDGE":
            latency = random.randint(20, 50)

        else:
            latency = random.randint(80, 150)

        return latency