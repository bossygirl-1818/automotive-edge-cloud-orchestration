import streamlit as st
import pandas as pd
import plotly.express as px


def render_decision_analytics():

    df = pd.read_csv("data/rl_reward_history.csv")

    decision_counts = (
        df["decision"]
        .value_counts()
        .reset_index()
    )

    decision_counts.columns = [
        "Decision",
        "Count"
    ]

    total_decisions = decision_counts["Count"].sum()

    st.markdown(
        '<div class="section-title">🎯 RL Decision Analytics</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    edge_count = int(
        decision_counts.loc[
            decision_counts["Decision"] == "EDGE",
            "Count"
        ].sum()
    )

    vehicle_count = int(
        decision_counts.loc[
            decision_counts["Decision"] == "VEHICLE",
            "Count"
        ].sum()
    )

    cloud_count = int(
        decision_counts.loc[
            decision_counts["Decision"] == "CLOUD",
            "Count"
        ].sum()
    )

    with col1:
        st.metric("EDGE Decisions", edge_count)

    with col2:
        st.metric("VEHICLE Decisions", vehicle_count)

    with col3:
        st.metric("CLOUD Decisions", cloud_count)

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
        textfont=dict(
            color="white",
            size=16
        ),
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
        font=dict(
            color="#ffffff",
            size=15
        ),
        height=430,
        showlegend=False,
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        annotations=[
            dict(
                text=f"{total_decisions}<br>Decisions",
                x=0.5,
                y=0.5,
                font=dict(
                    size=22,
                    color="#38bdf8"
                ),
                showarrow=False
            )
        ]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

   