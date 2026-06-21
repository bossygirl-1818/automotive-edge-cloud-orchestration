import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Automotive Edge-Cloud Orchestrator",
    layout="wide"
)

st.title(
    "🚗 Self-Adaptive Task Orchestration for the Automotive Edge-Cloud Continuum"
)

st.markdown("---")

# Metrics

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Tasks", "1000")

with col2:
    st.metric("Avg Latency", "46.67 ms")

with col3:
    st.metric("Vehicle Tasks", "386")

with col4:
    st.metric("Edge + Cloud", "614")

st.markdown("---")

st.subheader("Average Latency Comparison")

latency_graph = Image.open(
    "data/latency_comparison.png"
)

st.image(latency_graph)

st.markdown("---")

st.subheader("Task Distribution Comparison")

distribution_graph = Image.open(
    "data/task_distribution.png"
)

st.image(distribution_graph)

st.markdown("---")

st.subheader("Task Offloading Ratio")

offloading_graph = Image.open(
    "data/offloading_ratio.png"
)

st.image(offloading_graph)

st.markdown("---")

st.success(
    "Machine Learning Based Automotive Orchestrator Running Successfully"
)