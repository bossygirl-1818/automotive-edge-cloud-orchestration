import os
import pandas as pd
import streamlit as st
import plotly.express as px


def render_digital_twin_dashboard():

    file_path = "data/digital_twin_results.csv"

    st.markdown(
        '<div class="section-title">🧬 SimPy Digital Twin Simulation</div>',
        unsafe_allow_html=True
    )

    if not os.path.exists(file_path):
        st.warning("Digital Twin results not found. Run: python -m src.digital_twin")
        return

    df = pd.read_csv(file_path)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Digital Twin Tasks", len(df))

    with col2:
        st.metric("Avg Queue Wait", f"{df['queue_wait_time'].mean():.2f}")

    with col3:
        st.metric("Avg Processing", f"{df['processing_time'].mean():.2f}")

    with col4:
        st.metric("Avg Completion", f"{df['total_time'].mean():.2f}")

    decision_counts = (
        df["decision"]
        .value_counts()
        .reset_index()
    )

    decision_counts.columns = ["Decision", "Count"]

    total_tasks = decision_counts["Count"].sum()

    fig = px.pie(
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

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        textfont=dict(color="white", size=16),
        marker=dict(
            line=dict(
                color="#020617",
                width=4
            )
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
                text=f"{total_tasks}<br>Tasks",
                x=0.5,
                y=0.5,
                font=dict(size=22, color="#38bdf8"),
                showarrow=False
            )
        ]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=350
    )