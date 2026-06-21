class MetricsCollector:

    def __init__(self):

        self.total_latency = 0
        self.total_tasks = 0

        self.vehicle_count = 0
        self.edge_count = 0
        self.cloud_count = 0

    def record(self, destination, latency):

        self.total_tasks += 1
        self.total_latency += latency

        if destination == "VEHICLE":
            self.vehicle_count += 1

        elif destination == "EDGE":
            self.edge_count += 1

        else:
            self.cloud_count += 1

    def report(self):

        avg_latency = self.total_latency / self.total_tasks

        print("\n========== RESULTS ==========")

        print(f"Total Tasks: {self.total_tasks}")
        print(f"Average Latency: {avg_latency:.2f} ms")

        print(f"Vehicle Tasks: {self.vehicle_count}")
        print(f"Edge Tasks: {self.edge_count}")
        print(f"Cloud Tasks: {self.cloud_count}")