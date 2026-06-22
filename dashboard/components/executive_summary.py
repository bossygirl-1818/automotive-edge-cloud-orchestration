import streamlit as st

from src.db_queries import (
    get_rl_rewards,
    get_telemetry
)


def render_executive_summary():

    reward_df = get_rl_rewards()
    telemetry_df = get_telemetry()

    avg_reward = reward_df["reward"].mean()
    avg_latency = telemetry_df["network_latency"].mean()
    avg_battery = telemetry_df["battery"].mean()

    system_score = min(
        100,
        round(
            (avg_reward * 0.45)
            + ((100 - avg_latency) * 0.30)
            + (avg_battery * 0.25)
        )
    )

    energy_efficiency = round(avg_battery)

    accuracy = min(
        99,
        round(
            85 + (avg_reward / 10)
        )
    )

    st.markdown(
        '<div class="section-title">🚗 Executive System Summary</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "System Score",
            f"{system_score}%"
        )

    with col2:
        st.metric(
            "Accuracy",
            f"{accuracy}%"
        )

    with col3:
        st.metric(
            "Energy Efficiency",
            f"{energy_efficiency}%"
        )

    with col4:
        st.metric(
            "Avg Latency",
            f"{avg_latency:.0f} ms"
        )

    if avg_latency < 120 and avg_battery > 60:
        st.success(
            "System Status: OPTIMAL | Hybrid Orchestrator Operating Normally"
        )
    elif avg_latency < 170:
        st.warning(
            "System Status: STABLE | Moderate Resource Utilization"
        )
    else:
        st.error(
            "System Status: DEGRADED | High Latency Detected"
        )