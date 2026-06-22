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
        hole=0.55,
        title="Fleet Offloading Distribution"
    )

    fig1.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff"),
        height=420
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
        font=dict(color="#ffffff"),
        height=420
    )

    fig2.update_xaxes(title="Vehicle ID")
    fig2.update_yaxes(title="Average Completion Time")

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=350
    )