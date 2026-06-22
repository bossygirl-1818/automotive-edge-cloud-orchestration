import streamlit as st
from src.db_queries import get_rl_rewards
import plotly.express as px


def render_reward_analytics():

    df = get_rl_rewards()

    total_episodes = len(df)
    avg_reward = df["reward"].mean()
    max_reward = df["reward"].max()
    min_reward = df["reward"].min()

    st.markdown(
        '<div class="section-title">📈 RL Reward Analytics</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Episodes", total_episodes)

    with col2:
        st.metric("Avg Reward", f"{avg_reward:.2f}")

    with col3:
        st.metric("Max Reward", f"{max_reward:.2f}")

    with col4:
        st.metric("Min Reward", f"{min_reward:.2f}")

    fig = px.line(
        df,
        x="episode",
        y="reward",
        markers=False,
        title="DQN Episode Reward Trend"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff"),
        height=420,
        margin=dict(l=30, r=30, t=60, b=30)
    )

    fig.update_traces(
        line=dict(width=4, color="#38bdf8")
    )

    fig.update_xaxes(
        title="Episode",
        gridcolor="#1e293b"
    )

    fig.update_yaxes(
        title="Reward",
        gridcolor="#1e293b"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(
        '<div class="graph-title">Complete RL Reward History</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=500
    )