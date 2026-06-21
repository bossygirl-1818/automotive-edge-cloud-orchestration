import streamlit as st


def calculate_dqn_reward(rl_result):

    latency = rl_result["task_latency"]
    battery = rl_result["battery"]
    decision = rl_result["decision"]

    latency_reward = 10 if latency < 50 else -5
    battery_reward = 5 if battery > 40 else -10
    decision_reward = 8 if decision == "EDGE" else 4 if decision == "VEHICLE" else 2

    total_reward = latency_reward + battery_reward + decision_reward

    return {
        "latency_reward": latency_reward,
        "battery_reward": battery_reward,
        "decision_reward": decision_reward,
        "total_reward": total_reward
    }


def render_dqn_reward(rl_result):

    reward = calculate_dqn_reward(rl_result)

    st.markdown(
        '<div class="section-title">🎯 DQN Reward Analysis</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Latency Reward", reward["latency_reward"])

    with col2:
        st.metric("Battery Reward", reward["battery_reward"])

    with col3:
        st.metric("Decision Reward", reward["decision_reward"])

    with col4:
        st.metric("Total Reward", reward["total_reward"])

    if reward["total_reward"] > 0:
        st.success(f"Positive reward achieved: {reward['total_reward']}")
    else:
        st.error(f"Negative reward detected: {reward['total_reward']}")