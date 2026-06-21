import streamlit as st
import pandas as pd
import plotly.express as px


def render_latency_analytics():

    df = pd.read_csv(
        "data/rl_reward_history.csv"
    )

    avg_latency = df["latency"].mean()
    max_latency = df["latency"].max()
    min_latency = df["latency"].min()

    st.markdown(
        '<div class="section-title">⚡ Latency Analytics</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Avg Latency",
            f"{avg_latency:.2f} ms"
        )

    with col2:
        st.metric(
            "Max Latency",
            f"{max_latency} ms"
        )

    with col3:
        st.metric(
            "Min Latency",
            f"{min_latency} ms"
        )

    fig = px.line(
        df,
        x="episode",
        y="latency",
        markers=True
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        height=450,
        showlegend=False
    )

    fig.update_traces(
        line=dict(width=4)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )