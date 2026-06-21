import streamlit as st
from PIL import Image


def render_graph_tabs():
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📊 Model Comparison",
            "⚡ Latency Analysis",
            "🌐 Task Distribution",
            "📡 Offloading Ratio"
        ]
    )

    with tab1:
        render_graph_card(
            "ML Model Accuracy Comparison",
            "data/model_comparison.png",
            900
        )

    with tab2:
        render_graph_card(
            "Average Latency Comparison",
            "data/latency_comparison.png",
            900
        )

    with tab3:
        render_graph_card(
            "Vehicle vs Edge vs Cloud Task Distribution",
            "data/task_distribution.png",
            900
        )

    with tab4:
        render_graph_card(
            "Task Offloading Ratio",
            "data/offloading_ratio.png",
            700
        )


def render_graph_card(title, image_path, width):
    st.markdown('<div class="graph-card">', unsafe_allow_html=True)

    st.markdown(
        f'<div class="graph-title">{title}</div>',
        unsafe_allow_html=True
    )

    st.image(Image.open(image_path), width=width)

    st.markdown('</div>', unsafe_allow_html=True)