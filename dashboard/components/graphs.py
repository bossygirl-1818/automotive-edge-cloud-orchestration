import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components


def render_graph_tabs():
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📊 Model Comparison",
            "⚡ Latency Analysis",
            "🌐 Task Distribution",
            "📡 Offloading Ratio",
            "🧠 DQN Rewards"
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


def chart_layout(fig):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#f8fafc"),
        margin=dict(l=30, r=30, t=50, b=30),
        height=450
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
        title="Accuracy (%)",
        range=[95, 100.5]
    )

    fig.update_xaxes(title="Model")

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

    fig.update_yaxes(title="Latency (ms)")
    fig.update_xaxes(title="Strategy")

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
    fig.update_yaxes(title="Number of Tasks")

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

    st.plotly_chart(
        chart_layout(fig),
        use_container_width=True
    )


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