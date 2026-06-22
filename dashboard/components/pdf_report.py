import streamlit as st
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

from src.db_queries import get_rl_rewards, get_telemetry


def generate_pdf():

    reward_df = get_rl_rewards()
    telemetry_df = get_telemetry()

    avg_reward = reward_df["reward"].mean()
    avg_latency = telemetry_df["network_latency"].mean()
    avg_battery = telemetry_df["battery"].mean()

    edge_ratio = (
        reward_df[reward_df["decision"] == "EDGE"].shape[0]
        / len(reward_df)
    ) * 100

    vehicle_ratio = (
        reward_df[reward_df["decision"] == "VEHICLE"].shape[0]
        / len(reward_df)
    ) * 100

    cloud_ratio = (
        reward_df[reward_df["decision"] == "CLOUD"].shape[0]
        / len(reward_df)
    ) * 100

    pdf_path = "Automotive_Report.pdf"

    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()
    content = []

    content.append(
        Paragraph(
            "Automotive Edge-Cloud Orchestration Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(Paragraph("Project Overview", styles["Heading2"]))
    content.append(
        Paragraph(
            "Self-Adaptive Task Orchestration using Machine Learning and "
            "Deep Reinforcement Learning for Vehicle-Edge-Cloud environments.",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 15))

    content.append(Paragraph("System Metrics", styles["Heading2"]))

    metrics_data = [
        ["Metric", "Value"],
        ["Average Reward", f"{avg_reward:.2f}"],
        ["Average Network Latency", f"{avg_latency:.2f} ms"],
        ["Average Battery", f"{avg_battery:.2f} %"],
        ["Total RL Episodes", str(len(reward_df))],
        ["Telemetry Records", str(len(telemetry_df))]
    ]

    metrics_table = Table(metrics_data, colWidths=[250, 180])
    metrics_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
        ])
    )

    content.append(metrics_table)

    content.append(Spacer(1, 15))

    content.append(Paragraph("Offloading Distribution", styles["Heading2"]))

    distribution_data = [
        ["Target", "Percentage"],
        ["Vehicle Processing", f"{vehicle_ratio:.1f} %"],
        ["Edge Offloading", f"{edge_ratio:.1f} %"],
        ["Cloud Offloading", f"{cloud_ratio:.1f} %"]
    ]

    distribution_table = Table(distribution_data, colWidths=[250, 180])
    distribution_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
        ])
    )

    content.append(distribution_table)

    content.append(Spacer(1, 15))

    content.append(Paragraph("Executive Summary", styles["Heading2"]))
    content.append(
        Paragraph(
            "The Hybrid ML + DQN Orchestrator achieved strong overall "
            "performance by balancing network latency, energy efficiency, "
            "reward optimization, and adaptive workload offloading across "
            "Vehicle, Edge, and Cloud resources.",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 15))

    strategy_data = [
        ["Best Strategy Selected"],
        ["Hybrid Orchestrator"],
        ["Reason"],
        ["Lowest average latency"],
        ["Highest reward score"],
        ["Improved adaptive decision making"],
        ["Balanced energy and resource utilization"]
    ]

    strategy_table = Table(strategy_data, colWidths=[430])
    strategy_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
        ])
    )

    content.append(strategy_table)

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["BodyText"]
        )
    )

    doc.build(content)

    return pdf_path


def render_pdf_report():

    st.markdown(
        '<div class="section-title">📄 Export Evaluation Report</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "Generate PDF Report",
        use_container_width=True
    ):

        pdf_file = generate_pdf()

        with open(pdf_file, "rb") as f:
            st.download_button(
                label="⬇ Download Report",
                data=f,
                file_name="Automotive_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )