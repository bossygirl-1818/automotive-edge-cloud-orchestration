import os
import pandas as pd
import streamlit as st
import plotly.express as px


def render_fleet_dashboard():

    file_path = "data/fleet_simulation_results.csv"

    st.markdown(
        '<div class="section-title">🚗🚗 Multi-Vehicle Fleet Simulation</div>',
        unsafe_allow_html=True
    )

    if not os.path.exists(file_path):
        st.warning("Fleet simulation results not found. Run: python -m src.fleet_simulation")
        return

    df = pd.read_csv(file_path)

    fleet_size = df["vehicle_id"].nunique()
    total_tasks = len(df)
    avg_wait = df["queue_wait_time"].mean()
    avg_completion = df["total_time"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Fleet Size", fleet_size)

    with col2:
        st.metric("Fleet Tasks", total_tasks)

    with col3:
        st.metric("Avg Queue Wait", f"{avg_wait:.2f}")

    with col4:
        st.metric("Avg Completion", f"{avg_completion:.2f}")

    decision_counts = df["decision"].value_counts().reset_index()
    decision_counts.columns = ["Decision", "Count"]

    fig1 = px.pie(
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
                text=f"{total_tasks}<br>Tasks",
                x=0.5,
                y=0.5,
                font=dict(size=22, color="#38bdf8"),
                showarrow=False
            )
        ]
    )

    st.plotly_chart(fig1, use_container_width=True)

    avg_vehicle_time = (
        df.groupby("vehicle_id")["total_time"]
        .mean()
        .reset_index()
    )

    fig2 = px.bar(
        avg_vehicle_time,
        x="vehicle_id",
        y="total_time",
        title="Average Completion Time Per Vehicle"
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=430
    )

    fig2.update_xaxes(title="Vehicle ID", color="white")
    fig2.update_yaxes(title="Average Completion Time", color="white")

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=350
    )