import random


def calculate_edge_score(edge):

    latency_score = (100 - edge["latency"]) * 0.5
    bandwidth_score = edge["bandwidth"] * 0.3
    cpu_score = (100 - edge["cpu"]) * 0.2

    return round(
        latency_score +
        bandwidth_score +
        cpu_score,
        2
    )


def get_edge_servers():

    edges = [
        {
            "name": "Edge-1",
            "latency": random.randint(15, 50),
            "cpu": random.randint(30, 90),
            "bandwidth": random.randint(50, 200)
        },
        {
            "name": "Edge-2",
            "latency": random.randint(15, 50),
            "cpu": random.randint(30, 90),
            "bandwidth": random.randint(50, 200)
        },
        {
            "name": "Edge-3",
            "latency": random.randint(15, 50),
            "cpu": random.randint(30, 90),
            "bandwidth": random.randint(50, 200)
        }
    ]

    for edge in edges:
        edge["score"] = calculate_edge_score(edge)

    return edges


def select_best_edge(edges):

    return max(
        edges,
        key=lambda x: x["score"]
    )