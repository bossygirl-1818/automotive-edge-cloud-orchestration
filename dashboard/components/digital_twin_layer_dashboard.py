import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "digital_twin_states"


def render_digital_twin_layer_dashboard():

    st.markdown(
        '<div class="section-title">🏙️ Digital Twin Monitoring Layer</div>',
        unsafe_allow_html=True
    )

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    conn.close()

    if df.empty:
        st.warning("No digital twin data found. Run: python -m src.digital_twin_collector")
        return

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Twin States", len(df))

    with col2:
        st.metric("Avg Vehicle Speed", f"{df['vehicle_speed'].mean():.2f} m/s")

    with col3:
        st.metric("Avg Edge CPU", f"{df['edge_cpu_load'].mean():.2f}%")

    with col4:
        st.metric("Avg Cloud Latency", f"{df['cloud_latency_ms'].mean():.2f} ms")

    health_counts = df["vehicle_health_status"].value_counts().reset_index()
    health_counts.columns = ["Health Status", "Count"]

    fig1 = px.pie(
        health_counts,
        names="Health Status",
        values="Count",
        hole=0.58,
        title="Vehicle Health Distribution"
    )

    fig1.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=430
    )

    st.plotly_chart(fig1, use_container_width=True)

    congestion_counts = df["congestion_level"].value_counts().reset_index()
    congestion_counts.columns = ["Congestion Level", "Count"]

    fig2 = px.bar(
        congestion_counts,
        x="Congestion Level",
        y="Count",
        title="Road Congestion Distribution"
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=430
    )

    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.line(
        df,
        x="timestamp",
        y="edge_cpu_load",
        title="Edge CPU Load Over Time"
    )

    fig3.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=430
    )

    st.plotly_chart(fig3, use_container_width=True)

    fig4 = px.line(
        df,
        x="timestamp",
        y="cloud_latency_ms",
        title="Cloud Latency Over Time"
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