import streamlit as st
import plotly.graph_objects as go

from src.live_resources import (
    get_vehicle_resources,
    get_edge_resources,
    get_cloud_resources
)


def create_gauge(title, value):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#38bdf8"},
                "bgcolor": "#111827",
                "borderwidth": 2,
                "bordercolor": "#38bdf8",
                "steps": [
                    {"range": [0, 50], "color": "#0f172a"},
                    {"range": [50, 80], "color": "#1e293b"},
                    {"range": [80, 100], "color": "#334155"}
                ]
            }
        )
    )

    fig.update_layout(
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(
            color="white",
            size=16
        ),
        height=250,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    return fig


def render_gauges():

    vehicle = get_vehicle_resources()
    edge = get_edge_resources()
    cloud = get_cloud_resources()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.plotly_chart(
            create_gauge(
                "🚗 Vehicle CPU",
                vehicle["cpu"]
            ),
            use_container_width=True
        )
        st.metric(
            "CPU Usage",
            f"{vehicle['cpu']}%"
        )

    with col2:
        st.plotly_chart(
            create_gauge(
                "🔋 Battery",
                vehicle["battery"]
            ),
            use_container_width=True
        )
        st.metric(
            "Battery Level",
            f"{vehicle['battery']}%"
        )

    with col3:
        st.plotly_chart(
            create_gauge(
                "📡 Edge Load",
                edge["load"]
            ),
            use_container_width=True
        )
        st.metric(
            "Edge Utilization",
            f"{edge['load']}%"
        )

    with col4:
        st.plotly_chart(
            create_gauge(
                "☁️ Cloud Load",
                cloud["load"]
            ),
            use_container_width=True
        )
        st.metric(
            "Cloud Utilization",
            f"{cloud['load']}%"
        )