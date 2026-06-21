import streamlit as st

from src.RL_Files.rl_simulator import get_rl_decision


def render_rl_decision():

    result = get_rl_decision()

    st.markdown(
        '<div class="section-title">🧠 DQN Orchestrator Decision</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Decision",
            result["decision"]
        )

        st.metric(
            "Task Latency",
            f"{result['task_latency']} ms"
        )

    with col2:
        st.metric(
            "Battery",
            f"{result['battery']:.1f}%"
        )

        st.metric(
            "Edge Delay",
            f"{result['edge_delay']:.1f} ms"
        )

    return result
