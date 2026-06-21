import matplotlib.pyplot as plt


def create_graphs():

    adaptive_latency = 46.65
    ml_latency = 46.69

    strategies = ["Adaptive", "ML"]
    latencies = [adaptive_latency, ml_latency]

    plt.figure(figsize=(6, 4))
    plt.bar(strategies, latencies)
    plt.title("Average Latency Comparison")
    plt.ylabel("Latency (ms)")
    plt.savefig("data/latency_comparison.png")

    print("Graph saved: data/latency_comparison.png")