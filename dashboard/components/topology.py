import streamlit as st


def render_topology(selected_edge="Edge-2", decision="EDGE"):

    html = f"""<div class="compact-topology-box">
<div class="compact-topology-flow">
<span>🚗 Vehicle</span>
<span class="compact-arrow">→</span>
<span>📡 {selected_edge}</span>
<span class="compact-arrow">→</span>
<span>☁️ Cloud</span>
</div>
<div class="compact-topology-decision">
Current Route: <span>{decision}</span>
</div>
</div>"""

    st.markdown(html, unsafe_allow_html=True)