import streamlit as st
import pandas as pd
import plotly.express as px


def render_benchmark_comparison():

    st.markdown(
        '<div class="section-title">🏆 ML vs DQN vs Hybrid Benchmark</div>',
        unsafe_allow_html=True
    )

    benchmark_df = pd.DataFrame({
        "Method": ["ML", "DQN", "Hybrid"],
        "Avg Latency (ms)": [95, 72, 60],
        "Avg Reward": [18, 25, 29],
        "Energy Efficiency (%)": [62, 71, 78],
        "Decision Accuracy (%)": [92, 95, 97]
    })

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Best Latency", "Hybrid - 60 ms")

    with col2:
        st.metric("Best Reward", "Hybrid - 29")

    with col3:
        st.metric("Best Accuracy", "Hybrid - 97%")

    fig = px.bar(
        benchmark_df,
        x="Method",
        y=[
            "Avg Latency (ms)",
            "Avg Reward",
            "Energy Efficiency (%)",
            "Decision Accuracy (%)"
        ],
        barmode="group"
    )

    fig.update_layout(
        title=None,
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=500,
        margin=dict(l=20, r=20, t=60, b=20),
        legend=dict(
            title_text="",
            font=dict(color="#ffffff", size=14),
            orientation="h",
            yanchor="bottom",
            y=1.03,
            xanchor="center",
            x=0.5
        )
    )

    fig.update_xaxes(
        title="Orchestration Method",
        gridcolor="#1e293b",
        title_font=dict(color="#ffffff"),
        tickfont=dict(color="#ffffff")
    )

    fig.update_yaxes(
        title="Metric Value",
        gridcolor="#1e293b",
        title_font=dict(color="#ffffff"),
        tickfont=dict(color="#ffffff")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )