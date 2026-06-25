from graphviz import Digraph
import os

OUT_DIR = "docs/images"
os.makedirs(OUT_DIR, exist_ok=True)

BMW_BLUE = "#0066B1"
DARK_BG = "#08111F"
CARD = "#132238"
TEXT = "#FFFFFF"
SUBTEXT = "#AAB7C4"


def node_label(title, subtitle):
    title = title.replace("&", "&amp;")
    subtitle = subtitle.replace("&", "&amp;")

    return f"""<
    <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="6">
        <TR><TD><FONT POINT-SIZE="16"><B>{title}</B></FONT></TD></TR>
        <TR><TD><FONT POINT-SIZE="11" COLOR="{SUBTEXT}">{subtitle}</FONT></TD></TR>
    </TABLE>
    >"""


def add_node(dot, name, title, subtitle):
    dot.node(
        name,
        label=node_label(title, subtitle),
        shape="rect",
        style="rounded,filled",
        fillcolor=CARD,
        color=BMW_BLUE,
        fontcolor=TEXT,
        penwidth="2",
        margin="0.16",
    )


def build_architecture():
    dot = Digraph("architecture", format="png")
    dot.attr(
        rankdir="TB",
        bgcolor=DARK_BG,
        splines="ortho",
        nodesep="0.7",
        ranksep="0.9",
        pad="0.4",
    )

    dot.attr(
        "node",
        fontname="Arial",
        fontsize="14",
    )

    dot.attr(
        "edge",
        color=BMW_BLUE,
        fontcolor=SUBTEXT,
        arrowsize="0.8",
        penwidth="2",
        fontname="Arial",
    )

    # Title
    dot.node(
        "title",
        label="Self-Adaptive Automotive Edge–Cloud Orchestration Architecture",
        shape="plain",
        fontcolor=TEXT,
        fontsize="24",
        fontname="Arial Bold",
    )

    # Input layer
    with dot.subgraph(name="cluster_input") as c:
        c.attr(
            label="Input & Telemetry Layer",
            color=BMW_BLUE,
            fontcolor=TEXT,
            style="rounded",
            penwidth="2",
            bgcolor="#0B1628",
        )
        add_node(c, "sensors", "Vehicle Sensors", "CPU, battery, telemetry")
        add_node(c, "tasks", "Task Generator", "Automotive workloads")
        add_node(c, "monitor", "Resource Monitor", "Latency, load, bandwidth")

    # AI layer
    with dot.subgraph(name="cluster_ai") as c:
        c.attr(
            label="AI Decision Layer",
            color=BMW_BLUE,
            fontcolor=TEXT,
            style="rounded",
            penwidth="2",
            bgcolor="#0B1628",
        )
        add_node(c, "ml", "ML Orchestrator", "Supervised decision model")
        add_node(c, "dqn", "DQN Agent", "Reinforcement learning policy")
        add_node(c, "hybrid", "Hybrid Decision Engine", "ML + RL decision fusion")

    # Execution layer
    with dot.subgraph(name="cluster_execution") as c:
        c.attr(
            label="Execution Layer",
            color=BMW_BLUE,
            fontcolor=TEXT,
            style="rounded",
            penwidth="2",
            bgcolor="#0B1628",
        )
        add_node(c, "vehicle", "Vehicle Compute", "Low-latency local execution")
        add_node(c, "edge", "Edge Server", "Nearby task offloading")
        add_node(c, "cloud", "Cloud Server", "Heavy computation")

    # Intelligence layer
    with dot.subgraph(name="cluster_intelligence") as c:
        c.attr(
            label="Intelligence Services",
            color=BMW_BLUE,
            fontcolor=TEXT,
            style="rounded",
            penwidth="2",
            bgcolor="#0B1628",
        )
        add_node(c, "twin", "Digital Twin", "Virtual vehicle state")
        add_node(c, "predictive", "Predictive AI", "Congestion & latency forecast")
        add_node(c, "xai", "Explainable AI", "Decision transparency")
        add_node(c, "adaptive", "Self-Adaptive AI", "Runtime optimization")

    # Monitoring layer
    with dot.subgraph(name="cluster_monitoring") as c:
        c.attr(
            label="Monitoring & Visualization Layer",
            color=BMW_BLUE,
            fontcolor=TEXT,
            style="rounded",
            penwidth="2",
            bgcolor="#0B1628",
        )
        add_node(c, "prometheus", "Prometheus", "Metrics collection")
        add_node(c, "grafana", "Grafana", "Live observability")
        add_node(c, "streamlit", "Streamlit Dashboard", "Executive UI")

    # Main flow
    dot.edge("title", "sensors", style="invis")

    dot.edge("sensors", "tasks")
    dot.edge("tasks", "monitor")
    dot.edge("monitor", "ml")
    dot.edge("monitor", "dqn")

    dot.edge("ml", "hybrid")
    dot.edge("dqn", "hybrid")

    dot.edge("hybrid", "vehicle")
    dot.edge("hybrid", "edge")
    dot.edge("hybrid", "cloud")

    dot.edge("vehicle", "twin")
    dot.edge("edge", "predictive")
    dot.edge("cloud", "xai")

    dot.edge("twin", "predictive")
    dot.edge("predictive", "xai")
    dot.edge("xai", "adaptive")

    dot.edge("adaptive", "prometheus")
    dot.edge("prometheus", "grafana")
    dot.edge("grafana", "streamlit")

    dot.render(f"{OUT_DIR}/architecture", cleanup=True)


def build_workflow():
    dot = Digraph("workflow", format="png")
    dot.attr(
        rankdir="TB",
        bgcolor=DARK_BG,
        splines="ortho",
        nodesep="0.55",
        ranksep="0.65",
        pad="0.35",
    )

    dot.attr("node", fontname="Arial")
    dot.attr("edge", color=BMW_BLUE, arrowsize="0.8", penwidth="2")

    steps = [
        ("task", "Vehicle Task Generated", "New workload enters the system"),
        ("resource", "Resource Monitoring", "CPU, battery, latency collected"),
        ("ml", "ML Prediction", "Initial execution target predicted"),
        ("dqn", "DQN Decision", "RL policy selects an action"),
        ("fusion", "Hybrid Fusion", "ML and RL decisions combined"),
        ("execute", "Execution Target Selected", "Vehicle, Edge, or Cloud"),
        ("twin", "Digital Twin Update", "Virtual vehicle state synchronized"),
        ("predict", "Predictive Analytics", "Forecast congestion and load"),
        ("xai", "XAI Explanation", "Human-readable decision reason"),
        ("adaptive", "Self-Adaptive Control", "Runtime optimization applied"),
        ("metrics", "Prometheus Metrics", "Telemetry exported"),
        ("dashboard", "Grafana + Streamlit", "Live visualization"),
    ]

    dot.node(
        "title",
        label="End-to-End Orchestration Workflow",
        shape="plain",
        fontcolor=TEXT,
        fontsize="24",
        fontname="Arial Bold",
    )

    previous = "title"
    for key, title, subtitle in steps:
        add_node(dot, key, title, subtitle)
        dot.edge(previous, key)
        previous = key

    dot.render(f"{OUT_DIR}/workflow", cleanup=True)


def build_ai_pipeline():
    dot = Digraph("ai_pipeline", format="png")
    dot.attr(
        rankdir="LR",
        bgcolor=DARK_BG,
        splines="ortho",
        nodesep="0.7",
        ranksep="0.9",
        pad="0.4",
    )

    dot.attr("node", fontname="Arial")
    dot.attr("edge", color=BMW_BLUE, arrowsize="0.8", penwidth="2")

    add_node(dot, "input", "Input State", "CPU, battery, latency, task priority")
    add_node(dot, "ml", "ML Model", "Supervised prediction")
    add_node(dot, "dqn", "DQN Agent", "Reward-based action")
    add_node(dot, "fusion", "Hybrid Fusion", "Final orchestration decision")

    add_node(dot, "vehicle", "Vehicle", "Local execution")
    add_node(dot, "edge", "Edge", "Low-latency offload")
    add_node(dot, "cloud", "Cloud", "Heavy computation")
    add_node(dot, "feedback", "Feedback Loop", "Rewards, XAI, adaptive overrides")

    dot.edge("input", "ml")
    dot.edge("ml", "dqn")
    dot.edge("dqn", "fusion")

    dot.edge("fusion", "vehicle")
    dot.edge("fusion", "edge")
    dot.edge("fusion", "cloud")

    dot.edge("vehicle", "feedback")
    dot.edge("edge", "feedback")
    dot.edge("cloud", "feedback")
    dot.edge("feedback", "input", style="dashed")

    dot.render(f"{OUT_DIR}/ai_pipeline", cleanup=True)


if __name__ == "__main__":
    build_architecture()
    build_workflow()
    build_ai_pipeline()

    print("Premium diagrams created:")
    print("docs/images/architecture.png")
    print("docs/images/workflow.png")
    print("docs/images/ai_pipeline.png")