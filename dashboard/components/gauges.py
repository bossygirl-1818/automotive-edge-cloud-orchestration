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
            title={
                "text": title,
                "font": {"size": 14, "color": "white"}
            },
            number={
                "font": {"size": 22, "color": "#38bdf8"}
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickfont": {"color": "white", "size": 10}
                },
                "bar": {"color": "#38bdf8"},
                "bgcolor": "#111827",
                "borderwidth": 1,
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
        font=dict(color="white"),
        height=190,
        margin=dict(l=10, r=10, t=45, b=10)
    )

    return fig


def render_gauges():

    vehicle = get_vehicle_resources()
    edge = get_edge_resources()
    cloud = get_cloud_resources()

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.plotly_chart(
            create_gauge("🚗 Vehicle CPU", vehicle["cpu"]),
            use_container_width=True
        )

    with row1_col2:
        st.plotly_chart(
            create_gauge("🔋 Battery", vehicle["battery"]),
            use_container_width=True
        )

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.plotly_chart(
            create_gauge("📡 Edge Load", edge["load"]),
            use_container_width=True
        )

    with row2_col2:
        st.plotly_chart(
            create_gauge("☁️ Cloud Load", cloud["load"]),
            use_container_width=True
        )