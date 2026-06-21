import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def draw_box(ax, text, x, y, width=4, height=0.9):
    box = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.04",
        linewidth=1.6,
        facecolor="white",
        edgecolor="black"
    )
    ax.add_patch(box)

    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=9,
        wrap=True
    )


def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=1.5
        )
    )


def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(10, 14))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 16)
    ax.axis("off")

    # Main pipeline
    boxes = [
        ("Vehicle Sensors\nCamera | LiDAR | Radar | GPS", 3, 14),
        ("Task Generator\nLane Detection | Obstacle Detection\nRoute Planning | Diagnostics", 3, 12.5),
        ("Task Queue", 3, 11),
        ("Resource Monitor\nVehicle CPU | Battery\nEdge Delay | Cloud Delay", 3, 9.5),
        ("Self-Adaptive ML Orchestrator\nDecision Engine", 3, 8),
    ]

    for text, x, y in boxes:
        draw_box(ax, text, x, y)

    # Execution locations
    draw_box(ax, "Vehicle\nOnboard Processing", 0.5, 6.2, 2.5, 0.9)
    draw_box(ax, "Edge Server\nLow-Latency Offloading", 3.75, 6.2, 2.5, 0.9)
    draw_box(ax, "Cloud Server\nHigh-Compute Processing", 7, 6.2, 2.5, 0.9)

    # Evaluation pipeline
    draw_box(ax, "Task Execution Layer\nLatency + Task Processing", 3, 4.6)
    draw_box(ax, "Metrics Collector\nLatency | Distribution | Offloading Ratio", 3, 3.1)
    draw_box(ax, "Streamlit Dashboard\nGraphs + Results", 3, 1.6)

    # Vertical arrows
    draw_arrow(ax, 5, 14, 5, 13.4)
    draw_arrow(ax, 5, 12.5, 5, 11.9)
    draw_arrow(ax, 5, 11, 5, 10.4)
    draw_arrow(ax, 5, 9.5, 5, 8.9)

    # Orchestrator to execution locations
    draw_arrow(ax, 5, 8, 1.75, 7.1)
    draw_arrow(ax, 5, 8, 5, 7.1)
    draw_arrow(ax, 5, 8, 8.25, 7.1)

    # Execution locations to task execution layer
    draw_arrow(ax, 1.75, 6.2, 5, 5.5)
    draw_arrow(ax, 5, 6.2, 5, 5.5)
    draw_arrow(ax, 8.25, 6.2, 5, 5.5)

    # Final flow
    draw_arrow(ax, 5, 4.6, 5, 4.0)
    draw_arrow(ax, 5, 3.1, 5, 2.5)

    plt.title(
        "Self-Adaptive Task Orchestration Architecture",
        fontsize=14,
        fontweight="bold"
    )

    plt.savefig(
        "data/architecture_diagram.png",
        dpi=300,
        bbox_inches="tight"
    )

    print("Architecture diagram saved: data/architecture_diagram.png")


if __name__ == "__main__":
    create_architecture_diagram()