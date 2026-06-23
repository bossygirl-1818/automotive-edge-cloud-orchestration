import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


DB_PATH = "data/orchestrator.db"


def style_donut_chart(fig, center_text):
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        textfont=dict(color="white", size=16),
        marker=dict(
            line=dict(color="#020617", width=4)
        )
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=430,
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
        annotations=[
            dict(
                text=center_text,
                x=0.5,
                y=0.5,
                font=dict(size=22, color="#38bdf8"),
                showarrow=False
            )
        ]
    )

    return fig


def style_bar_chart(fig):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=430,
        margin=dict(l=30, r=30, t=55, b=80),
        showlegend=False
    )

    fig.update_xaxes(
        title="Task Type",
        tickangle=-20,
        title_font=dict(color="#ffffff"),
        tickfont=dict(color="#ffffff", size=13),
        gridcolor="#1e293b"
    )

    fig.update_yaxes(
        title="Count",
        title_font=dict(color="#ffffff"),
        tickfont=dict(color="#ffffff", size=13),
        gridcolor="#1e293b"
    )

    return fig


def render_sumo_dashboard():

    st.markdown(
        '<div class="section-title">🚦 SUMO Traffic-Aware Orchestration</div>',
        unsafe_allow_html=True
    )

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM sumo_orchestration_tasks",
        conn
    )

    conn.close()

    if df.empty:
        st.warning(
            "No SUMO orchestration data found. Run: python -m src.sumo_db_loader"
        )
        return

    total_tasks = len(df)
    avg_speed = df["speed"].mean()
    avg_battery = df["battery"].mean()
    vehicle_count = df["vehicle_id"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("SUMO Tasks", total_tasks)

    with col2:
        st.metric("Vehicles", vehicle_count)

    with col3:
        st.metric("Avg Speed", f"{avg_speed:.2f} m/s")

    with col4:
        st.metric("Avg Battery", f"{avg_battery:.2f}%")

    decision_counts = (
        df["decision"]
        .value_counts()
        .reset_index()
    )

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

    fig1 = style_donut_chart(
        fig1,
        f"{total_tasks}<br>Tasks"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    task_counts = (
        df["task_type"]
        .value_counts()
        .reset_index()
    )

    task_counts.columns = ["Task Type", "Count"]

    fig2 = px.bar(
        task_counts,
        x="Task Type",
        y="Count",
        title="SUMO Task Type Distribution"
    )

    fig2 = style_bar_chart(fig2)

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=350
    )