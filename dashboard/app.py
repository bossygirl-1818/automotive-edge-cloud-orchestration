import streamlit as st
import pandas as pd

from components.explainability import render_explainability
from components.dqn_explainability import render_dqn_explainability
from components.decision_comparison import render_decision_comparison
from components.rl_decision import render_rl_decision
from components.edge_selection import render_edge_selection
from components.topology import render_topology
from streamlit_autorefresh import st_autorefresh
from components.live_prediction import render_live_prediction
from components.decision_history import render_decision_history
from components.task_queue import render_task_queue
from components.load_css import load_css
from components.sidebar import render_sidebar
from components.metrics import render_metrics
from components.graphs import render_graph_tabs
from components.gauges import render_gauges
from components.hybrid_orchestrator import render_hybrid_orchestrator
from components.dqn_reward import render_dqn_reward
from components.reward_analytics import render_reward_analytics
from components.decision_analytics import render_decision_analytics
from components.latency_analytics import render_latency_analytics
from components.energy_analytics import render_energy_analytics
from components.benchmark_comparison import render_benchmark_comparison
from components.offloading_distribution import render_offloading_distribution
from components.system_report import render_system_report
from components.executive_summary import render_executive_summary


st.set_page_config(
    page_title="Automotive Edge-Cloud Orchestrator",
    page_icon="🚗",
    layout="wide"
)

st_autorefresh(
    interval=5000,
    key="dashboard_refresh"
)

st.markdown(
    f"<style>{load_css('dashboard/styles/dashboard.css')}</style>",
    unsafe_allow_html=True
)

model_df = pd.read_csv("data/model_comparison.csv")

model_list = model_df["model"].tolist()

total_tasks, selected_model = render_sidebar(model_list)

selected_row = model_df[model_df["model"] == selected_model].iloc[0]

selected_accuracy = selected_row["accuracy"] * 100
selected_model_file = selected_row["model_file"]

st.markdown(
    '<div class="main-title">Self-Adaptive Task Orchestration Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Automotive Edge–Cloud Continuum | ML-Based Dynamic Workload Offloading</div>',
    unsafe_allow_html=True
)

render_metrics(
    total_tasks,
    selected_accuracy,
    selected_model
)

st.markdown(
    '<h2 style="color:white;">🚗 Live Resource Monitoring</h2>',
    unsafe_allow_html=True
)

render_gauges()

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(f"""
<div class="graph-card">
    <div class="graph-title">Active Model Details</div>
    <p style="color:#cbd5e1; font-size:16px;">
    Selected Model:
    <b style="color:#38bdf8;">{selected_model}</b><br>
    Accuracy:
    <b style="color:#38bdf8;">{selected_accuracy:.2f}%</b><br>
    Model File:
    <b style="color:#38bdf8;">{selected_model_file}</b>
    </p>
</div>
""", unsafe_allow_html=True)

live_decision = render_live_prediction(selected_model_file)
render_task_queue(selected_model_file)

rl_result = render_rl_decision()

agreement = (
    live_decision["decision"] ==
    rl_result["decision"]
)

render_decision_comparison(
    live_decision["decision"],
    rl_result["decision"]
)

hybrid_result = render_hybrid_orchestrator(
    live_decision["decision"],
    rl_result["decision"]
)
render_dqn_reward(rl_result)
render_dqn_explainability(rl_result)
from components.reward_analytics import render_reward_analytics

if agreement:
    st.success(
        f"✅ ML and DQN agree: {live_decision['decision']}"
    )
else:
    st.warning(
        f"⚠ ML = {live_decision['decision']} | "
        f"DQN = {rl_result['decision']}"
    )

render_explainability(
    live_decision["task_type"],
    live_decision["latency"],
    live_decision["priority"],
    live_decision["decision"],
    live_decision["edge_delay"],
    live_decision["cloud_delay"],
    live_decision["battery"]
)


best_edge = render_edge_selection()
render_topology(
    selected_edge=best_edge,
    decision=live_decision["decision"]
)
render_reward_analytics()
render_decision_analytics()
render_latency_analytics()
render_energy_analytics()
render_benchmark_comparison()
render_offloading_distribution()
render_graph_tabs()
render_decision_history()
render_system_report()
render_executive_summary()


st.markdown("""
<div class="success-box">
✅ Interactive Multi-Model Automotive Edge-Cloud Orchestrator Running Successfully
</div>
""", unsafe_allow_html=True)