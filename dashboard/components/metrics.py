import streamlit as st


def render_metrics(total_tasks, selected_accuracy, selected_model):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{total_tasks}</div>
            <div class="metric-label">Total Tasks</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{selected_accuracy:.2f}%</div>
            <div class="metric-label">Selected Model Accuracy</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{selected_model}</div>
            <div class="metric-label">Active ML Model</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">61.4%</div>
            <div class="metric-label">Offloading Ratio</div>
        </div>
        """, unsafe_allow_html=True)