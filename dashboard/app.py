import streamlit as st
import pandas as pd

from components.edge_selection import render_edge_selection
from components.explainability import render_explainability
from streamlit_autorefresh import st_autorefresh
from components.live_prediction import render_live_prediction
from components.decision_history import render_decision_history
from components.task_queue import render_task_queue
from components.load_css import load_css
from components.sidebar import render_sidebar
from components.metrics import render_metrics
from components.graphs import render_graph_tabs
from components.gauges import render_gauges


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

render_explainability(
    live_decision["task_type"],
    live_decision["latency"],
    live_decision["priority"],
    live_decision["decision"],
    live_decision["edge_delay"],
    live_decision["cloud_delay"],
    live_decision["battery"]
)

render_edge_selection()
render_task_queue(selected_model_file)
render_decision_history()

render_graph_tabs()

st.markdown("""
<div class="success-box">
✅ Interactive Multi-Model Automotive Edge-Cloud Orchestrator Running Successfully
</div>
""", unsafe_allow_html=True)