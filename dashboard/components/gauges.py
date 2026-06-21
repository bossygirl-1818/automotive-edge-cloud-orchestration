import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def create_gauge(title, value, max_value=100):

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
                    "range": [0, max_value],
                    "tickfont": {"color": "white", "size": 10}
                },
                "bar": {"color": "#38bdf8"},
                "bgcolor": "#111827",
                "borderwidth": 1,
                "bordercolor": "#38bdf8",
                "steps": [
                    {"range": [0, max_value * 0.5], "color": "#0f172a"},
                    {"range": [max_value * 0.5, max_value * 0.8], "color": "#1e293b"},
                    {"range": [max_value * 0.8, max_value], "color": "#334155"}
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


def render_decision_badge(decision):

    if decision == "VEHICLE":
        color = "#22c55e"
        icon = "🚗"
    elif decision == "EDGE":
        color = "#38bdf8"
        icon = "📡"
    else:
        color = "#f97316"
        icon = "☁️"

    st.markdown(
        f"""
        <div style="
            background:#020617;
            border:1px solid {color};
            border-radius:18px;
            padding:28px;
            text-align:center;
            box-shadow:0 0 25px rgba(56,189,248,0.15);
            min-height:135px;
        ">
            <div style="color:white;font-size:18px;font-weight:700;">
                Active Offloading Decision
            </div>
            <div style="color:{color};font-size:42px;font-weight:900;margin-top:12px;">
                {icon} {decision}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_gauges(active_decision=None):

    df = pd.read_csv("data/vehicle_telemetry.csv")

    if "telemetry_index" not in st.session_state:
        st.session_state.telemetry_index = 0

    latest = df.iloc[st.session_state.telemetry_index]

    st.session_state.telemetry_index += 1

    if st.session_state.telemetry_index >= len(df):
        st.session_state.telemetry_index = 0

    vehicle_cpu = latest["vehicle_cpu"]
    battery = latest["battery"]
    edge_load = latest["edge_load"]
    cloud_load = latest["cloud_load"]
    network_latency = latest["network_latency"]

    telemetry_decision = latest["decision"]

    final_decision = active_decision if active_decision is not None else telemetry_decision

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.plotly_chart(
            create_gauge("🚗 Vehicle CPU", vehicle_cpu),
            use_container_width=True
        )

    with row1_col2:
        st.plotly_chart(
            create_gauge("🔋 Battery", battery),
            use_container_width=True
        )

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.plotly_chart(
            create_gauge("📡 Edge Load", edge_load),
            use_container_width=True
        )

    with row2_col2:
        st.plotly_chart(
            create_gauge("☁️ Cloud Load", cloud_load),
            use_container_width=True
        )

    row3_col1, row3_col2 = st.columns(2)

    with row3_col1:
        st.plotly_chart(
            create_gauge("⚡ Network Latency", network_latency, max_value=250),
            use_container_width=True
        )

    with row3_col2:
        render_decision_badge(final_decision)