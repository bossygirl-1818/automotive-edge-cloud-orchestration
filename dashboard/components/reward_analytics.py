import streamlit as st
import pandas as pd
import plotly.express as px


def render_reward_analytics():

    reward_file = "data/rl_reward_history.csv"

    df = pd.read_csv(reward_file)

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
        st.metric("Max Reward", max_reward)

    with col4:
        st.metric("Min Reward", min_reward)

    fig = px.line(
        df,
        x="episode",
        y="reward",
        markers=True,
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
        line=dict(width=4),
        marker=dict(size=7)
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

    st.dataframe(
        df.tail(10),
        use_container_width=True,
        hide_index=True
    )