import sqlite3
import pandas as pd
import streamlit as st


def render_db_decision_history():

    conn = sqlite3.connect("data/orchestrator.db")

    df = pd.read_sql_query(
        """
        SELECT
            id,
            ml_decision,
            dqn_decision,
            hybrid_decision,
            selected_engine,
            timestamp
        FROM decisions
        ORDER BY id DESC
        LIMIT 10
        """,
        conn
    )

    conn.close()

    st.markdown(
        '<div class="section-title">🗄️ Database Decision History</div>',
        unsafe_allow_html=True
    )

    if df.empty:
        st.warning("No decisions logged yet.")
    else:
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )