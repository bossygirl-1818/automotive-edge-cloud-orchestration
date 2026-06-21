import streamlit as st
import pandas as pd
import joblib

from src.task_generator import TaskGenerator
from src.resource_monitor import ResourceMonitor


def render_live_prediction(selected_model_file):

    generator = TaskGenerator()
    monitor = ResourceMonitor()

    model = joblib.load(selected_model_file)

    task = generator.generate_task(1)
    vehicle = monitor.get_vehicle_resources()
    edge = monitor.get_edge_resources()
    cloud = monitor.get_cloud_resources()

    input_data = pd.DataFrame([{
        "vehicle_cpu": vehicle["cpu_usage"],
        "battery": vehicle["battery_level"],
        "vehicle_speed": vehicle["vehicle_speed"],
        "traffic_density": vehicle["traffic_density"],
        "edge_delay": edge["network_delay"],
        "edge_bandwidth": edge["network_bandwidth"],
        "cloud_delay": cloud["network_delay"],
        "cloud_bandwidth": cloud["network_bandwidth"],
        "task_latency": task["latency_requirement"],
        "task_priority": task["task_priority"],
        "task_size": task["task_size"]
    }])

    prediction = model.predict(input_data)[0]

    st.markdown(
        '<div class="graph-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="graph-title">Live ML Offloading Decision</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Task Type", task["task_type"])
        st.metric("Task Priority", task["task_priority"])

    with col2:
        st.metric("Task Latency", f"{task['latency_requirement']} ms")
        st.metric("Task Size", f"{task['task_size']} MB")

    with col3:
        st.metric("Predicted Location", prediction)
        st.metric("Selected Model", selected_model_file.split("/")[-1])

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )