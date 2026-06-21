import streamlit as st
import pandas as pd
import plotly.express as px


def render_offloading_distribution():

    df = pd.read_csv(
        "data/rl_reward_history.csv"
    )

    counts = (
        df["decision"]
        .value_counts()
        .reset_index()
    )

    counts.columns = [
        "Target",
        "Count"
    ]

    total = counts["Count"].sum()

    st.markdown(
        '<div class="section-title">🚀 Offloading Distribution</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    edge_ratio = (
        counts.loc[
            counts["Target"] == "EDGE",
            "Count"
        ].sum() / total
    ) * 100

    vehicle_ratio = (
        counts.loc[
            counts["Target"] == "VEHICLE",
            "Count"
        ].sum() / total
    ) * 100

    cloud_ratio = (
        counts.loc[
            counts["Target"] == "CLOUD",
            "Count"
        ].sum() / total
    ) * 100

    with col1:
        st.metric(
            "Vehicle %",
            f"{vehicle_ratio:.1f}%"
        )

    with col2:
        st.metric(
            "Edge %",
            f"{edge_ratio:.1f}%"
        )

    with col3:
        st.metric(
            "Cloud %",
            f"{cloud_ratio:.1f}%"
        )

    fig = px.bar(
        counts,
        x="Target",
        y="Count",
        color="Target"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        showlegend=False,
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )