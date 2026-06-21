from prometheus_client import Gauge, Counter, start_http_server
import random
import time


vehicle_cpu = Gauge("vehicle_cpu_usage", "Vehicle CPU usage percentage")
vehicle_battery = Gauge("vehicle_battery_level", "Vehicle battery level percentage")
edge_load = Gauge("edge_server_load", "Edge server load percentage")
cloud_load = Gauge("cloud_server_load", "Cloud server load percentage")

tasks_processed = Counter("tasks_processed_total", "Total processed orchestration tasks")
edge_offloads = Counter("edge_offloads_total", "Total tasks offloaded to edge")
cloud_offloads = Counter("cloud_offloads_total", "Total tasks offloaded to cloud")
vehicle_processed = Counter("vehicle_processed_total", "Total tasks processed on vehicle")


def update_metrics():
    vehicle_cpu.set(random.randint(20, 95))
    vehicle_battery.set(random.randint(10, 100))
    edge_load.set(random.randint(20, 90))
    cloud_load.set(random.randint(10, 85))

    decision = random.choice(["VEHICLE", "EDGE", "CLOUD"])

    tasks_processed.inc()

    if decision == "VEHICLE":
        vehicle_processed.inc()
    elif decision == "EDGE":
        edge_offloads.inc()
    else:
        cloud_offloads.inc()


if __name__ == "__main__":
    start_http_server(8000)
    print("Prometheus metrics exporter running on http://localhost:8000/metrics")

    while True:
        update_metrics()
        time.sleep(5)