import random


def get_vehicle_resources():
    return {
        "cpu": random.randint(30, 95),
        "battery": random.randint(20, 100)
    }


def get_edge_resources():
    return {
        "load": random.randint(20, 90)
    }


def get_cloud_resources():
    return {
        "load": random.randint(10, 80)
    }