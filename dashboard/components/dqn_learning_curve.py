import streamlit as st
import plotly.express as px

from src.db_queries import get_rl_rewards


def render_dqn_learning_curve():

    df = get_rl_rewards()

    df["moving_avg_reward"] = (
        df["reward"]
        .rolling(window=10, min_periods=1)
        .mean()
    )

    st.markdown(
        '<div class="section-title">📈 DQN Learning Curve</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Episodes Trained",
            len(df)
        )

    with col2:
        st.metric(
            "Latest Reward",
            f"{df['reward'].iloc[-1]:.2f}"
        )

    with col3:
        st.metric(
            "Best Reward",
            f"{df['reward'].max():.2f}"
        )

    fig = px.line(
        df,
        x="episode",
        y=["reward", "moving_avg_reward"],
        markers=True,
        title="DQN Training Reward Progress"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(
            color="#ffffff",
            size=15
        ),
        height=450,
        margin=dict(
            l=30,
            r=30,
            t=60,
            b=30
        ),
        legend=dict(
            title_text="",
            font=dict(color="#ffffff"),
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
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
        df,
        use_container_width=True,
        hide_index=True,
        height=400
    )