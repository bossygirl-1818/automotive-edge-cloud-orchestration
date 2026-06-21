import streamlit as st


def render_sidebar(model_list):
    with st.sidebar:
        st.markdown("## 🚗 Orchestrator Control")

        total_tasks = st.slider(
            "Number of Tasks",
            1000,
            10000,
            10000,
            step=1000
        )

        selected_model = st.selectbox(
            "Selected ML Model",
            model_list
        )

        st.markdown("### System Status")
        st.success("ML Model Loaded")
        st.info("Dashboard Active")
        st.warning("Simulation Mode")

    return total_tasks, selected_model