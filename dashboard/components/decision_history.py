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
            "Vehicle Processing": random.randint(10, 30),
            "Edge Server Processing": random.randint(10, 25),
            "Cloud Server Processing": random.randint(5, 20)
        })

    df = pd.DataFrame(data)

    fig = px.line(
        df,
        x="Time",
        y=[
            "Vehicle Processing",
            "Edge Server Processing",
            "Cloud Server Processing"
        ],
        markers=True
    )

    fig.update_traces(line=dict(width=4))

    fig.data[0].line.color = "#22c55e"
    fig.data[1].line.color = "#38bdf8"
    fig.data[2].line.color = "#f97316"

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        showlegend=False,
        height=500,
        title=""
    )

    fig.update_xaxes(
        title_text="Timeline",
        tickfont=dict(color="#ffffff", size=14),
        title_font=dict(color="#38bdf8", size=18),
        gridcolor="#1e293b"
    )

    fig.update_yaxes(
        title_text="Tasks Processed",
        tickfont=dict(color="#ffffff", size=14),
        title_font=dict(color="#38bdf8", size=18),
        gridcolor="#1e293b"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("""
    <div style="display:flex; gap:25px; margin-top:-10px; margin-bottom:25px; flex-wrap:wrap;">
        <div style="color:white; font-weight:700; font-size:16px;">
            <span style="color:#22c55e;">●</span> Vehicle Processing
        </div>
        <div style="color:white; font-weight:700; font-size:16px;">
            <span style="color:#38bdf8;">●</span> Edge Server Processing
        </div>
        <div style="color:white; font-weight:700; font-size:16px;">
            <span style="color:#f97316;">●</span> Cloud Server Processing
        </div>
    </div>
    """, unsafe_allow_html=True)