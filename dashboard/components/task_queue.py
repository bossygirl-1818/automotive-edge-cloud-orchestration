import streamlit as st
import pandas as pd
import joblib

from src.task_generator import TaskGenerator
from src.resource_monitor import ResourceMonitor


def render_task_queue(selected_model_file, num_tasks=6):

    generator = TaskGenerator()
    monitor = ResourceMonitor()
    model = joblib.load(selected_model_file)

    rows = []

    for i in range(1, num_tasks + 1):

        task = generator.generate_task(i)

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

        rows.append({
            "Task": task["task_id"],
            "Type": task["task_type"],
            "Priority": task["task_priority"],
            "Route": prediction
        })

    df = pd.DataFrame(rows)

    st.markdown(
        '<div class="section-title">📋 Real-Time Task Queue</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=260
    )

    st.info(f"⚡ {len(df)} Tasks Currently Waiting For Scheduling")