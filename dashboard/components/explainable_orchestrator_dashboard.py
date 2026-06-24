import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "explainable_orchestration_history"


def render_explainable_orchestrator_dashboard():

    st.markdown(
        '<div class="section-title">🧠 Explainable AI Orchestrator</div>',
        unsafe_allow_html=True
    )

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    conn.close()

    if df.empty:
        st.warning("No XAI history found. Run: python -m src.explainable_orchestrator_history")
        return

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("XAI Records", len(df))

    with col2:
        st.metric("Avg Battery", f"{df['battery'].mean():.2f}%")

    with col3:
        st.metric("Avg Speed", f"{df['speed'].mean():.2f} m/s")

    with col4:
        st.metric("Most Used Decision", df["decision"].mode()[0])

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
        height=500,
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
        annotations=[
            dict(
                text=f"{len(df)}<br>Records",
                x=0.5,
                y=0.5,
                font=dict(size=24, color="#38bdf8"),
                showarrow=False
            )
        ]
    )

    st.plotly_chart(
        fig1,
        use_container_width=True,
        key="xai_decision_distribution"
    )

    traffic_counts = df["traffic_density"].value_counts().reset_index()
    traffic_counts.columns = ["Traffic Density", "Count"]

    fig2 = px.pie(
        traffic_counts,
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
        height=500,
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
        annotations=[
            dict(
                text=f"{len(df)}<br>Records",
                x=0.5,
                y=0.5,
                font=dict(size=24, color="#38bdf8"),
                showarrow=False
            )
        ]
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
        key="xai_traffic_density_distribution"
    )

    st.markdown(
        '<div class="section-title">Latest Explainable Decisions</div>',
        unsafe_allow_html=True
    )

    latest_df = df[
        [
            "timestamp",
            "vehicle_id",
            "decision",
            "traffic_density",
            "battery",
            "speed",
            "task_type",
            "explanation"
        ]
    ].tail(10)

    st.dataframe(
        latest_df,
        use_container_width=True,
        hide_index=True,
        height=350
    )