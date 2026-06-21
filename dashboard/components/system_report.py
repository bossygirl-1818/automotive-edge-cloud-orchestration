import streamlit as st
import pandas as pd


def render_system_report():

    df = pd.read_csv("data/rl_reward_history.csv")

    avg_reward = df["reward"].mean()
    avg_latency = df["latency"].mean()

    edge_ratio = (df[df["decision"] == "EDGE"].shape[0] / len(df)) * 100
    vehicle_ratio = (df[df["decision"] == "VEHICLE"].shape[0] / len(df)) * 100
    cloud_ratio = (df[df["decision"] == "CLOUD"].shape[0] / len(df)) * 100

    avg_battery = df["battery"].mean()

    st.markdown(
        '<div class="section-title">📄 System Performance Report</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Avg Reward", f"{avg_reward:.2f}")

    with col2:
        st.metric("Avg Latency", f"{avg_latency:.2f} ms")

    with col3:
        st.metric("Avg Battery", f"{avg_battery:.2f}%")

    with col4:
        st.metric("Best Engine", "Hybrid")

    st.markdown(f"""
    <div class="success-box">
        ✅ Hybrid Orchestrator Summary<br><br>
        Edge Offloading: {edge_ratio:.1f}% |
        Vehicle Processing: {vehicle_ratio:.1f}% |
        Cloud Offloading: {cloud_ratio:.1f}%<br><br>
        The hybrid ML + DQN orchestration strategy improves adaptive decision-making by combining supervised prediction with reward-based optimization.
    </div>
    """, unsafe_allow_html=True)