import sqlite3
import streamlit as st


DB_PATH = "data/orchestrator.db"


def get_count(table_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]

    conn.close()
    return count


def render_database_status():

    st.markdown(
        '<div class="section-title">🗄️ Database Status</div>',
        unsafe_allow_html=True
    )

    telemetry_count = get_count("telemetry")
    reward_count = get_count("rl_rewards")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Telemetry Records", telemetry_count)

    with col2:
        st.metric("RL Reward Records", reward_count)

    with col3:
        st.metric("Database", "SQLite Active")