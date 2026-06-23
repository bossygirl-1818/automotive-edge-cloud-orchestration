import streamlit as st
import pandas as pd

from streamlit_autorefresh import st_autorefresh
from src.db_logger import log_decision
from components.load_css import load_css
from components.sidebar import render_sidebar
from components.metrics import render_metrics
from components.live_prediction import render_live_prediction
from components.task_queue import render_task_queue
from components.rl_decision import render_rl_decision
from components.decision_comparison import render_decision_comparison
from components.hybrid_orchestrator import render_hybrid_orchestrator
from components.gauges import render_gauges
from components.dqn_reward import render_dqn_reward
from components.dqn_explainability import render_dqn_explainability
from components.explainability import render_explainability
from components.edge_selection import render_edge_selection
from components.topology import render_topology
from components.reward_analytics import render_reward_analytics
from components.dqn_learning_curve import render_dqn_learning_curve
from components.decision_analytics import render_decision_analytics
from components.latency_analytics import render_latency_analytics
from components.energy_analytics import render_energy_analytics
from components.benchmark_comparison import render_benchmark_comparison
from components.offloading_distribution import render_offloading_distribution
from components.graphs import render_graph_tabs
from components.decision_history import render_decision_history
from components.system_report import render_system_report
from components.executive_summary import render_executive_summary
from components.database_status import render_database_status
from components.database_analytics import render_database_analytics
from components.digital_twin_dashboard import render_digital_twin_dashboard
from components.fleet_dashboard import render_fleet_dashboard
from components.sumo_dashboard import render_sumo_dashboard
from components.sumo_traffic_dashboard import render_sumo_traffic_dashboard
from components.advanced_traffic_dashboard import render_advanced_traffic_dashboard
from components.db_decision_history import render_db_decision_history
from components.pdf_report import render_pdf_report


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
    '<div class="sub-title">Automotive Edge–Cloud Continuum | ML + DQN Hybrid Workload Offloading</div>',
    unsafe_allow_html=True
)

# 1. Executive Metrics
render_metrics(
    total_tasks,
    selected_accuracy,
    selected_model
)

st.markdown("<br>", unsafe_allow_html=True)

# 2. Active Model Details
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

# 3. Live ML Decision
live_decision = render_live_prediction(selected_model_file)

# 4. Real-Time Task Queue
render_task_queue(selected_model_file)

# 5. DQN Decision
rl_result = render_rl_decision()

# 6. Decision Comparison
render_decision_comparison(
    live_decision["decision"],
    rl_result["decision"]
)

# 7. Hybrid Final Decision
hybrid_result = render_hybrid_orchestrator(
    live_decision["decision"],
    rl_result["decision"]
)

log_decision(
    ml_decision=live_decision["decision"],
    dqn_decision=rl_result["decision"],
    hybrid_decision=hybrid_result["final_decision"],
    selected_engine=hybrid_result["reason"]
)
# 8. Live Resource Monitoring
st.markdown(
    '<div class="section-title">🚗 Live Resource Monitoring</div>',
    unsafe_allow_html=True
)

render_gauges(
    hybrid_result["final_decision"]
)

# 9. DQN Reward + Explainability
render_dqn_reward(rl_result)
render_dqn_explainability(rl_result)

# 10. ML Explainability
render_explainability(
    live_decision["task_type"],
    live_decision["latency"],
    live_decision["priority"],
    live_decision["decision"],
    live_decision["edge_delay"],
    live_decision["cloud_delay"],
    live_decision["battery"]
)

# 11. Edge Selection + Topology
best_edge = render_edge_selection()

render_topology(
    selected_edge=best_edge,
    decision=hybrid_result["final_decision"]
)

# 12. RL Analytics
render_reward_analytics()
render_dqn_learning_curve()
render_decision_analytics()

# 13. System Performance Analytics
render_latency_analytics()
render_energy_analytics()
render_benchmark_comparison()
render_offloading_distribution()

# 14. Digital Twin + Fleet Simulation
render_digital_twin_dashboard()
render_fleet_dashboard()
render_sumo_dashboard()
render_sumo_traffic_dashboard()

# 15. Extra Graphs + History
render_graph_tabs()
render_decision_history()

# 16. Reports
render_system_report()
render_executive_summary()
render_database_status()
render_database_analytics()
render_advanced_traffic_dashboard()
render_db_decision_history()
render_pdf_report()

st.markdown("""
<div class="success-box">
✅ Interactive Multi-Model Automotive Edge-Cloud Orchestrator Running Successfully
</div>
""", unsafe_allow_html=True)