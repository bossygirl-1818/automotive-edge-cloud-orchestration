import matplotlib.pyplot as plt


def create_offloading_ratio_graph():

    local_tasks = 386
    offloaded_tasks = 614

    labels = [
        "Vehicle",
        "Offloaded"
    ]

    values = [
        local_tasks,
        offloaded_tasks
    ]

    plt.figure(figsize=(6, 6))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title("Task Offloading Ratio")

    plt.savefig("data/offloading_ratio.png")

    print("Graph saved: data/offloading_ratio.png")