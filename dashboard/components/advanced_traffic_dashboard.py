import os
import pandas as pd
import streamlit as st
import plotly.express as px


FILE_PATH = "data/sumo_advanced_orchestration.csv"


def render_advanced_traffic_dashboard():

    st.markdown(
        '<div class="section-title">🚦 Advanced Traffic-Aware Orchestration</div>',
        unsafe_allow_html=True
    )

    if not os.path.exists(FILE_PATH):
        st.warning("Advanced traffic data not found. Run: python -m src.advanced_traffic_orchestrator")
        return

    df = pd.read_csv(FILE_PATH)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Records", len(df))

    with col2:
        st.metric("Vehicles", df["vehicle_id"].nunique())

    with col3:
        st.metric("Avg Speed", f"{df['speed'].mean():.2f} m/s")

    with col4:
        st.metric("Avg Battery", f"{df['battery'].mean():.2f}%")

    decision_counts = df["decision"].value_counts().reset_index()
    decision_counts.columns = ["Decision", "Count"]

    fig1 = px.pie(
        decision_counts,
        names="Decision",
        values="Count",
        hole=0.58,
        color="Decision",
        color_discrete_map={
            "EDGE": "#38bdf8",
            "VEHICLE": "#22c55e",
            "CLOUD": "#f97316"
        }
    )

    fig1.update_traces(
        textposition="inside",
        textinfo="percent+label",
        textfont=dict(color="white", size=16),
        marker=dict(line=dict(color="#020617", width=4))
    )

    fig1.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=430,
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
        annotations=[
            dict(
                text=f"{len(df)}<br>Records",
                x=0.5,
                y=0.5,
                font=dict(size=22, color="#38bdf8"),
                showarrow=False
            )
        ]
    )

    st.plotly_chart(fig1, use_container_width=True)

    density_counts = df["traffic_density"].value_counts().reset_index()
    density_counts.columns = ["Traffic Density", "Count"]

    fig2 = px.pie(
        density_counts,
        names="Traffic Density",
        values="Count",
        hole=0.58,
        color="Traffic Density",
        color_discrete_map={
            "LOW": "#22c55e",
            "MEDIUM": "#facc15",
            "HIGH": "#ef4444"
        }
    )

    fig2.update_traces(
        textposition="inside",
        textinfo="percent+label",
        textfont=dict(color="white", size=16),
        marker=dict(line=dict(color="#020617", width=4))
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=430,
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
        annotations=[
            dict(
                text=f"{len(df)}<br>Records",
                x=0.5,
                y=0.5,
                font=dict(size=22, color="#38bdf8"),
                showarrow=False
            )
        ]
    )

    st.plotly_chart(fig2, use_container_width=True)

    network_counts = df["network_quality"].value_counts().reset_index()
    network_counts.columns = ["Network Quality", "Count"]

    fig3 = px.bar(
        network_counts,
        x="Network Quality",
        y="Count",
        title="Network Quality Distribution"
    )

    fig3.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=430
    )

    st.plotly_chart(fig3, use_container_width=True)

    speed_df = df.groupby("step")["speed"].mean().reset_index()

    fig4 = px.line(
        speed_df,
        x="step",
        y="speed",
        title="Average Speed Over Time"
    )

    fig4.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=430
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=350
    )