import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "predictive_forecast_history"


def apply_forecast_chart_style(fig, height=430):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        title=dict(font=dict(color="#ffffff", size=20), x=0.02),
        height=height,
        margin=dict(l=45, r=35, t=70, b=55)
    )

    fig.update_xaxes(
        gridcolor="#1e293b",
        zerolinecolor="#334155",
        title_font=dict(color="#ffffff"),
        tickfont=dict(color="#cbd5e1")
    )

    fig.update_yaxes(
        gridcolor="#1e293b",
        zerolinecolor="#334155",
        title_font=dict(color="#ffffff"),
        tickfont=dict(color="#cbd5e1")
    )

    return fig


def render_predictive_forecast_history_dashboard():

    st.markdown(
        '<div class="section-title">📈 Predictive Forecast History</div>',
        unsafe_allow_html=True
    )

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    conn.close()

    if df.empty:
        st.warning("No forecast history found. Run: python -m src.predictive_forecast_history")
        return

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Forecast Records", len(df))

    with col2:
        st.metric("Avg Congestion", f"{df['congestion_score'].mean():.2f}")

    with col3:
        st.metric("Avg Edge Load", f"{df['edge_load'].mean():.2f}%")

    with col4:
        st.metric("Avg Cloud Latency", f"{df['cloud_latency'].mean():.2f} ms")

    fig1 = px.line(
        df,
        x="timestamp",
        y="congestion_score",
        title="Predicted Congestion Score Over Time"
    )
    fig1 = apply_forecast_chart_style(fig1)
    fig1.update_traces(line=dict(width=4, color="#38bdf8"))
    fig1.update_xaxes(title="Timestamp")
    fig1.update_yaxes(title="Congestion Score")

    st.plotly_chart(
        fig1,
        use_container_width=True,
        key="forecast_congestion_score_trend"
    )

    fig2 = px.line(
        df,
        x="timestamp",
        y="edge_load",
        title="Predicted Edge Load Over Time"
    )
    fig2 = apply_forecast_chart_style(fig2)
    fig2.update_traces(line=dict(width=4, color="#38bdf8"))
    fig2.update_xaxes(title="Timestamp")
    fig2.update_yaxes(title="Edge Load (%)")

    st.plotly_chart(
        fig2,
        use_container_width=True,
        key="forecast_edge_load_trend"
    )

    fig3 = px.line(
        df,
        x="timestamp",
        y="cloud_latency",
        title="Predicted Cloud Latency Over Time"
    )
    fig3 = apply_forecast_chart_style(fig3)
    fig3.update_traces(line=dict(width=4, color="#38bdf8"))
    fig3.update_xaxes(title="Timestamp")
    fig3.update_yaxes(title="Cloud Latency (ms)")

    st.plotly_chart(
        fig3,
        use_container_width=True,
        key="forecast_cloud_latency_trend"
    )

    fig4 = px.line(
        df,
        x="timestamp",
        y="battery_drain",
        title="Predicted Battery Drain Over Time"
    )
    fig4 = apply_forecast_chart_style(fig4)
    fig4.update_traces(line=dict(width=4, color="#38bdf8"))
    fig4.update_xaxes(title="Timestamp")
    fig4.update_yaxes(title="Battery Drain (%)")

    st.plotly_chart(
        fig4,
        use_container_width=True,
        key="forecast_battery_drain_trend"
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=350
    )