import streamlit as st
import pandas as pd


def render_dqn_explainability(rl_result):

    q_values = rl_result.get("q_values", [0, 0, 0])
    decision = rl_result.get("decision", "UNKNOWN")

    vehicle_q = q_values[0]
    edge_q = q_values[1]
    cloud_q = q_values[2]

    max_q = max(q_values)

    st.markdown(
    """
    <h2 style="
        color:#ffffff;
        font-size:36px;
        font-weight:800;
        margin-bottom:20px;
    ">
        🧠 DQN Decision Explainability
    </h2>
    """,
    unsafe_allow_html=True
)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Vehicle Q-Value", f"{vehicle_q:.2f}")

    with col2:
        st.metric("Edge Q-Value", f"{edge_q:.2f}")

    with col3:
        st.metric("Cloud Q-Value", f"{cloud_q:.2f}")

    st.info(
        f"The DQN agent selected **{decision}** because it produced "
        f"the highest estimated Q-value among Vehicle, Edge, and Cloud."
    )

    st.success(f"Highest Q-Value: {max_q:.2f}")

    ranking_df = pd.DataFrame({
        "Rank": ["🥇", "🥈", "🥉"],
        "Target": ["VEHICLE", "EDGE", "CLOUD"],
        "Q-Value": [vehicle_q, edge_q, cloud_q]
    }).sort_values(
        by="Q-Value",
        ascending=False
    )

    st.markdown(
    """
    <h2 style="
        color:#ffffff;
        font-size:32px;
        font-weight:800;
        margin-top:25px;
        margin-bottom:15px;
    ">
        🏆 Q-Value Ranking
    </h2>
    """,
    unsafe_allow_html=True
)

    st.dataframe(
        ranking_df,
        use_container_width=True,
        hide_index=True
    )