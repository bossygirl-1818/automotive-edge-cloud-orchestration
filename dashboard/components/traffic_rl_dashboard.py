import os
import pandas as pd
import streamlit as st
import plotly.express as px


RESULTS_FILE = "data/traffic_rl_evaluation_results.csv"


def render_traffic_rl_dashboard():

    st.markdown(
        '<div class="section-title">🧠 Traffic-Aware RL Orchestrator</div>',
        unsafe_allow_html=True
    )

    if not os.path.exists(RESULTS_FILE):
        st.warning("Traffic RL results not found. Run: python -m src.traffic_rl_evaluator")
        return

    df = pd.read_csv(RESULTS_FILE)

    total = len(df)
    correct = (df["decision"] == df["rl_prediction"]).sum()
    wrong = total - correct
    accuracy = (correct / total) * 100

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Records", total)

    with col2:
        st.metric("Correct", correct)

    with col3:
        st.metric("Wrong", wrong)

    with col4:
        st.metric("RL Accuracy", f"{accuracy:.2f}%")

    prediction_counts = (
        df["rl_prediction"]
        .value_counts()
        .reset_index()
    )
    prediction_counts.columns = ["Decision", "Count"]

    fig1 = px.pie(
        prediction_counts,
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
        height=430,
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
        annotations=[
            dict(
                text=f"{total}<br>Predictions",
                x=0.5,
                y=0.5,
                font=dict(size=22, color="#38bdf8"),
                showarrow=False
            )
        ]
    )

    st.plotly_chart(fig1, use_container_width=True)

    matrix = pd.crosstab(
        df["decision"],
        df["rl_prediction"]
    )

    fig2 = px.imshow(
        matrix,
        text_auto=True,
        title="Actual vs Predicted RL Decisions"
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=430
    )

    fig2.update_xaxes(title="Predicted Decision")
    fig2.update_yaxes(title="Actual Decision")

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=350
    )