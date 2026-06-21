import streamlit as st


def render_executive_summary():

    st.markdown(
        '<div class="section-title">🚗 Executive System Summary</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("System Score", "94%")

    with col2:
        st.metric("Accuracy", "97%")

    with col3:
        st.metric("Energy Efficiency", "78%")

    with col4:
        st.metric("Avg Latency", "60 ms")

    st.success(
        "System Status: OPTIMAL | Hybrid Orchestrator Operating Normally"
    )