import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components


def render_graph_tabs():
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "📊 Model Comparison",
            "⚡ Latency Analysis",
            "🌐 Task Distribution",
            "📡 Offloading Ratio",
            "🧠 DQN Rewards",
            "🏆 Strategy Comparison"
        ]
    )

    with tab1:
        render_model_comparison()

    with tab2:
        render_latency_comparison()

    with tab3:
        render_task_distribution()

    with tab4:
        render_offloading_ratio()

    with tab5:
        render_dqn_reward_curve()

    with tab6:
        render_strategy_comparison()


def chart_layout(fig):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",

        font=dict(
            color="#ffffff",
            size=16
        ),

        title=dict(
            font=dict(
                color="#ffffff",
                size=24
            ),
            x=0.02
        ),

        margin=dict(
            l=50,
            r=40,
            t=70,
            b=50
        ),

        height=500,

        legend=dict(
            font=dict(
                color="#ffffff",
                size=14
            )
        )
    )

    fig.update_xaxes(
        tickfont=dict(
            color="#ffffff",
            size=14
        ),
        title_font=dict(
            color="#38bdf8",
            size=18
        ),
        gridcolor="#1e293b"
    )

    fig.update_yaxes(
        tickfont=dict(
            color="#ffffff",
            size=14
        ),
        title_font=dict(
            color="#38bdf8",
            size=18
        ),
        gridcolor="#1e293b"
    )

    return fig


def render_model_comparison():
    df = pd.read_csv("data/model_comparison.csv")
    df["accuracy_percent"] = df["accuracy"] * 100

    fig = px.bar(
        df,
        x="model",
        y="accuracy_percent",
        text="accuracy_percent",
        title="ML Model Accuracy Comparison"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_yaxes(
        title_text="Accuracy (%)",
        range=[95, 100.5]
    )

    fig.update_xaxes(title_text="Model")

    st.plotly_chart(
        chart_layout(fig),
        use_container_width=True
    )


def render_latency_comparison():
    df = pd.DataFrame({
        "Strategy": ["Adaptive", "ML", "Deep RL"],
        "Average Latency": [46.65, 46.69, 44.80]
    })

    fig = px.bar(
        df,
        x="Strategy",
        y="Average Latency",
        text="Average Latency",
        title="Average Latency Comparison"
    )

    fig.update_traces(
        texttemplate="%{text:.2f} ms",
        textposition="outside"
    )

    fig.update_yaxes(title_text="Latency (ms)")
    fig.update_xaxes(title_text="Strategy")

    st.plotly_chart(
        chart_layout(fig),
        use_container_width=True
    )


def render_task_distribution():
    df = pd.DataFrame({
        "Execution Location": ["Vehicle", "Edge", "Cloud"],
        "Tasks": [386, 361, 253]
    })

    fig = px.bar(
        df,
        x="Execution Location",
        y="Tasks",
        text="Tasks",
        title="Task Distribution Across Vehicle, Edge, and Cloud"
    )

    fig.update_traces(textposition="outside")
    fig.update_yaxes(title_text="Number of Tasks")

    st.plotly_chart(
        chart_layout(fig),
        use_container_width=True
    )


def render_offloading_ratio():
    df = pd.DataFrame({
        "Category": ["Vehicle Processing", "Offloaded Processing"],
        "Percentage": [38.6, 61.4]
    })

    fig = px.pie(
        df,
        names="Category",
        values="Percentage",
        title="Task Offloading Ratio",
        hole=0.45
    )

    fig.update_layout(showlegend=False)

    st.plotly_chart(
        chart_layout(fig),
        use_container_width=True
    )

    st.markdown("""
    <div style="display:flex; gap:30px; margin-top:-5px; margin-bottom:25px; flex-wrap:wrap;">
        <div style="color:white; font-weight:700; font-size:16px;">
            <span style="color:#6366f1;">●</span> Offloaded Processing
        </div>
        <div style="color:white; font-weight:700; font-size:16px;">
            <span style="color:#f97316;">●</span> Vehicle Processing
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_dqn_reward_curve():
    st.markdown(
        '<div class="graph-title">Deep RL Training Reward Curve</div>',
        unsafe_allow_html=True
    )

    with open(
        "data/dqn_reward_curve.html",
        "r",
        encoding="utf-8"
    ) as file:
        reward_html = file.read()

    components.html(
        reward_html,
        height=550,
        scrolling=True
    )


def render_strategy_comparison():
    df = pd.read_csv("data/strategy_comparison.csv")

    fig = px.bar(
        df,
        x="strategy",
        y="average_reward",
        text="average_reward",
        title="Rule-Based vs ML-Based vs Deep RL Reward Comparison"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside",
        marker_color=["#6366f1", "#f97316", "#22c55e"]
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        title=dict(
            text="Rule-Based vs ML-Based vs Deep RL Reward Comparison",
            font=dict(size=24, color="#ffffff"),
            x=0.02
        ),
        margin=dict(l=60, r=40, t=80, b=80),
        height=520,
        showlegend=False
    )

    fig.update_xaxes(
        title_text="Strategy",
        tickfont=dict(color="#ffffff", size=14),
        title_font=dict(color="#ffffff", size=16)
    )

    fig.update_yaxes(
        title_text="Average Reward",
        tickfont=dict(color="#ffffff", size=14),
        title_font=dict(color="#ffffff", size=16),
        gridcolor="#334155"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("""
    <div style="display:flex; gap:30px; margin-top:-5px; margin-bottom:25px; flex-wrap:wrap;">
        <div style="color:white; font-weight:700; font-size:16px;">
            <span style="color:#6366f1;">●</span> Rule-Based Orchestrator
        </div>
        <div style="color:white; font-weight:700; font-size:16px;">
            <span style="color:#f97316;">●</span> Machine Learning Orchestrator
        </div>
        <div style="color:white; font-weight:700; font-size:16px;">
            <span style="color:#22c55e;">●</span> Deep Reinforcement Learning Orchestrator
        </div>
    </div>
    """, unsafe_allow_html=True)