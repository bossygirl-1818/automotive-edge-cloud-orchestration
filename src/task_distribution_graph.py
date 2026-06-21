import matplotlib.pyplot as plt


def create_task_distribution_graph():

    adaptive = [386, 361, 253]
    ml = [386, 361, 253]

    locations = ["Vehicle", "Edge", "Cloud"]

    x = range(len(locations))

    width = 0.35

    plt.figure(figsize=(8, 5))

    plt.bar(
        [i - width/2 for i in x],
        adaptive,
        width,
        label="Adaptive"
    )

    plt.bar(
        [i + width/2 for i in x],
        ml,
        width,
        label="ML"
    )

    plt.xticks(x, locations)

    plt.ylabel("Number of Tasks")
    plt.title("Task Distribution Comparison")

    plt.legend()

    plt.savefig("data/task_distribution.png")

    print("Graph saved: data/task_distribution.png")