import streamlit as st
import pandas as pd
import random
import plotly.express as px


def render_decision_history():

    st.markdown(
        '<div class="section-title">📈 Historical Offloading Decisions</div>',
        unsafe_allow_html=True
    )

    data = []

    for i in range(20):
        data.append({
            "Time": i,
            "Vehicle": random.randint(10, 30),
            "Edge": random.randint(10, 25),
            "Cloud": random.randint(5, 20)
        })

    df = pd.DataFrame(data)

    fig = px.line(
        df,
        x="Time",
        y=["Vehicle", "Edge", "Cloud"],
        markers=True
    )

    fig.update_traces(line=dict(width=4))

    fig.data[0].line.color = "#22c55e"  # Vehicle
    fig.data[1].line.color = "#38bdf8"  # Edge
    fig.data[2].line.color = "#f97316"  # Cloud

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="white"),
        showlegend=True,
        height=500,
        title=None
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )