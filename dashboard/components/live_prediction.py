import streamlit as st
import pandas as pd
import joblib

from src.task_generator import TaskGenerator
from src.resource_monitor import ResourceMonitor
from src.task_logger import log_task
import uuid

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
        '<div class="section-title">⚡ Live ML Offloading Decision</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Task", task["task_type"])
        st.metric("Priority", task["task_priority"])
        st.metric("Latency", f"{task['latency_requirement']} ms")

    with col2:
        st.metric("Size", f"{task['task_size']} MB")
        st.metric("Decision", prediction)
        st.metric("Model", selected_model_file.split("/")[-1])

        log_task(
    task_id=str(uuid.uuid4())[:8],
    task_type=task["task_type"],
    priority=task["task_priority"],
    latency=task["latency_requirement"],
    task_size=task["task_size"],
    predicted_location=prediction
)

    return {
        "task_type": task["task_type"],
        "latency": task["latency_requirement"],
        "priority": task["task_priority"],
        "decision": prediction,
        "edge_delay": edge["network_delay"],
        "cloud_delay": cloud["network_delay"],
        "battery": vehicle["battery_level"]
    }