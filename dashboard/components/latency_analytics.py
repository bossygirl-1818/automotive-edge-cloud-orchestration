import streamlit as st
import plotly.express as px

from src.db_queries import get_telemetry


def render_latency_analytics():

    df = get_telemetry()

    avg_latency = df["network_latency"].mean()
    max_latency = df["network_latency"].max()
    min_latency = df["network_latency"].min()

    st.markdown(
        '<div class="section-title">⚡ Latency Analytics</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Avg Latency", f"{avg_latency:.2f} ms")

    with col2:
        st.metric("Max Latency", f"{max_latency:.0f} ms")

    with col3:
        st.metric("Min Latency", f"{min_latency:.0f} ms")

    fig = px.line(
        df,
        x="episode",
        y="network_latency",
        markers=False,
        title="Network Latency Optimization Over Episodes"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff"),
        height=500,
        margin=dict(l=30, r=30, t=50, b=30),
        showlegend=False
    )

    fig.update_traces(
        line=dict(width=4, color="#38bdf8")
    )

    fig.update_xaxes(
        title="Episode",
        gridcolor="#1e293b"
    )

    fig.update_yaxes(
        title="Network Latency (ms)",
        gridcolor="#1e293b"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )