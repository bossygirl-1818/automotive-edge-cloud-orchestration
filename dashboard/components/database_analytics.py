import streamlit as st
import sqlite3


def render_database_analytics():

    conn = sqlite3.connect(
        "data/orchestrator.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM tasks"
    )
    task_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM decisions"
    )
    decision_count = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM telemetry
        """
    )
    telemetry_count = cursor.fetchone()[0]

    conn.close()

    st.markdown(
        '<div class="section-title">🗄 Database Analytics</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Tasks Logged",
            task_count
        )

    with col2:
        st.metric(
            "Decisions Logged",
            decision_count
        )

    with col3:
        st.metric(
            "Telemetry Records",
            telemetry_count
        )