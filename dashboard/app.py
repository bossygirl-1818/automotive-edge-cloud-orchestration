import streamlit as st
import pandas as pd

from streamlit_autorefresh import st_autorefresh
from src.db_logger import log_decision

from components.load_css import load_css
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
from components.digital_twin_layer_dashboard import render_digital_twin_layer_dashboard
from components.db_decision_history import render_db_decision_history
from components.traffic_rl_dashboard import render_traffic_rl_dashboard
from components.predictive_forecast_history_dashboard import render_predictive_forecast_history_dashboard
from components.predictive_traffic_dashboard import render_predictive_traffic_dashboard
from components.explainable_orchestrator_dashboard import render_explainable_orchestrator_dashboard
from components.self_adaptive_dashboard import render_self_adaptive_dashboard
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


@st.cache_data
def load_model_data():
    return pd.read_csv("data/model_comparison.csv")


model_df = load_model_data()
model_list = model_df["model"].tolist()


def render_header():
    st.markdown(
        '<div class="main-title">Self-Adaptive Automotive Edge-Cloud Orchestration Platform</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">Digital Twin + Reinforcement Learning + Predictive Intelligence + XAI + Self-Adaptive Control</div>',
        unsafe_allow_html=True
    )


def render_sidebar_navigation():
    st.sidebar.markdown("## 🚗 Navigation")

    page = st.sidebar.radio(
        "Select Dashboard Module",
        [
            "🏠 Overview",
            "🚗 Core Orchestrator",
            "🧠 RL Intelligence",
            "🚦 SUMO Traffic",
            "📊 Advanced Traffic",
            "🏙️ Digital Twin",
            "🔮 Predictive Intelligence",
            "📈 Forecast History",
            "🧠 Explainable AI",
            "🔁 Self-Adaptive Control",
            "🗄️ Database & Reports",
            "📡 Monitoring Links"
        ]
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### System Stack")
    st.sidebar.markdown("""
    - Vehicle Layer  
    - Edge Layer  
    - Cloud Layer  
    - SUMO Traffic  
    - RL Agent  
    - Digital Twin  
    - Predictive Engine  
    - XAI Layer  
    - Self-Adaptive Controller  
    - Prometheus + Grafana  
    """)

    return page


def render_model_selector():
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ML Model Configuration")

    selected_model = st.sidebar.selectbox(
        "Select ML Model",
        model_list
    )

    total_tasks = st.sidebar.slider(
        "Number of Tasks",
        min_value=10,
        max_value=1000,
        value=100,
        step=10
    )

    selected_row = model_df[model_df["model"] == selected_model].iloc[0]

    return (
        total_tasks,
        selected_model,
        selected_row["accuracy"] * 100,
        selected_row["model_file"]
    )


def render_overview_page(total_tasks, selected_accuracy, selected_model):
    st.markdown(
        '<div class="section-title">🏠 Platform Overview</div>',
        unsafe_allow_html=True
    )

    render_metrics(
        total_tasks,
        selected_accuracy,
        selected_model
    )

    st.markdown("""
    <div class="graph-card">
        <div class="graph-title">System Overview</div>
        <p style="color:#cbd5e1; font-size:16px; line-height:1.7;">
        This platform demonstrates a self-adaptive automotive edge-cloud orchestration system.
        It combines traffic simulation, reinforcement learning, digital twin state modeling,
        predictive traffic intelligence, explainable AI, and real-time monitoring.
        </p>
    </div>
    """, unsafe_allow_html=True)

    render_executive_summary()


def render_core_orchestrator_page(total_tasks, selected_accuracy, selected_model, selected_model_file):
    st.markdown(
        '<div class="section-title">🚗 Core Edge-Cloud Orchestrator</div>',
        unsafe_allow_html=True
    )

    render_metrics(
        total_tasks,
        selected_accuracy,
        selected_model
    )

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

    render_decision_comparison(
        live_decision["decision"],
        rl_result["decision"]
    )

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

    st.markdown(
        '<div class="section-title">🚗 Live Resource Monitoring</div>',
        unsafe_allow_html=True
    )

    render_gauges(
        hybrid_result["final_decision"]
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
        decision=hybrid_result["final_decision"]
    )


def render_rl_intelligence_page():
    st.markdown(
        '<div class="section-title">🧠 RL Intelligence Layer</div>',
        unsafe_allow_html=True
    )

    rl_result = render_rl_decision()

    render_dqn_reward(rl_result)
    render_dqn_explainability(rl_result)
    render_reward_analytics()
    render_dqn_learning_curve()
    render_decision_analytics()
    render_traffic_rl_dashboard()


def render_sumo_page():
    st.markdown(
        '<div class="section-title">🚦 SUMO Traffic Simulation</div>',
        unsafe_allow_html=True
    )

    render_sumo_dashboard()
    render_sumo_traffic_dashboard()


def render_advanced_traffic_page():
    st.markdown(
        '<div class="section-title">📊 Advanced Traffic Orchestration</div>',
        unsafe_allow_html=True
    )

    render_advanced_traffic_dashboard()
    render_latency_analytics()
    render_energy_analytics()
    render_benchmark_comparison()
    render_offloading_distribution()


def render_digital_twin_page():
    st.markdown(
        '<div class="section-title">🏙️ Digital Twin Layer</div>',
        unsafe_allow_html=True
    )

    render_digital_twin_dashboard()
    render_fleet_dashboard()
    render_digital_twin_layer_dashboard()


def render_predictive_page():
    st.markdown(
        '<div class="section-title">🔮 Predictive Intelligence</div>',
        unsafe_allow_html=True
    )

    render_predictive_traffic_dashboard()


def render_forecast_history_page():
    st.markdown(
        '<div class="section-title">📈 Forecast History Analytics</div>',
        unsafe_allow_html=True
    )

    render_predictive_forecast_history_dashboard()


def render_xai_page():
    st.markdown(
        '<div class="section-title">🧠 Explainable AI Layer</div>',
        unsafe_allow_html=True
    )

    render_explainable_orchestrator_dashboard()


def render_self_adaptive_page():
    st.markdown(
        '<div class="section-title">🔁 Self-Adaptive Control Loop</div>',
        unsafe_allow_html=True
    )

    render_self_adaptive_dashboard()


def render_database_reports_page():
    st.markdown(
        '<div class="section-title">🗄️ Database, Reports & History</div>',
        unsafe_allow_html=True
    )

    render_database_status()
    render_database_analytics()
    render_db_decision_history()
    render_decision_history()
    render_graph_tabs()
    render_system_report()
    render_pdf_report()


def render_monitoring_links_page():
    st.markdown(
        '<div class="section-title">📡 Monitoring Links</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="graph-card">
        <div class="graph-title">External Monitoring Stack</div>
        <p style="color:#cbd5e1; font-size:16px; line-height:1.8;">
        Grafana and Prometheus run as separate monitoring services.
        Use this page during demos to quickly open live observability tools.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.link_button(
            "Open Grafana Dashboard",
            "http://localhost:3000"
        )

        st.link_button(
            "Open Prometheus Targets",
            "http://localhost:9090/targets"
        )

    with col2:
        st.link_button(
            "Core Metrics Exporter",
            "http://localhost:8000/metrics"
        )

        st.link_button(
            "Self-Adaptive Metrics Exporter",
            "http://localhost:8008/metrics"
        )

    st.markdown("""
    <div class="graph-card">
        <div class="graph-title">Exporter Ports</div>
        <p style="color:#cbd5e1; font-size:15px; line-height:1.8;">
        8000 - Core Orchestrator<br>
        8001 - SUMO Traffic<br>
        8002 - Advanced Traffic<br>
        8003 - Traffic RL<br>
        8004 - Digital Twin<br>
        8005 - Predictive Traffic<br>
        8006 - Forecast History<br>
        8007 - Explainable AI<br>
        8008 - Self-Adaptive Controller
        </p>
    </div>
    """, unsafe_allow_html=True)


render_header()

page = render_sidebar_navigation()

(
    total_tasks,
    selected_model,
    selected_accuracy,
    selected_model_file
) = render_model_selector()

if page == "🏠 Overview":
    render_overview_page(
        total_tasks,
        selected_accuracy,
        selected_model
    )

elif page == "🚗 Core Orchestrator":
    render_core_orchestrator_page(
        total_tasks,
        selected_accuracy,
        selected_model,
        selected_model_file
    )

elif page == "🧠 RL Intelligence":
    render_rl_intelligence_page()

elif page == "🚦 SUMO Traffic":
    render_sumo_page()

elif page == "📊 Advanced Traffic":
    render_advanced_traffic_page()

elif page == "🏙️ Digital Twin":
    render_digital_twin_page()

elif page == "🔮 Predictive Intelligence":
    render_predictive_page()

elif page == "📈 Forecast History":
    render_forecast_history_page()

elif page == "🧠 Explainable AI":
    render_xai_page()

elif page == "🔁 Self-Adaptive Control":
    render_self_adaptive_page()

elif page == "🗄️ Database & Reports":
    render_database_reports_page()

elif page == "📡 Monitoring Links":
    render_monitoring_links_page()

st.markdown("""
<div class="success-box">
✅ Self-Adaptive Automotive Edge-Cloud Orchestration Platform Running Successfully
</div>
""", unsafe_allow_html=True)