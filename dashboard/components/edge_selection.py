import streamlit as st
import pandas as pd

from src.edge_selector import get_edge_servers, select_best_edge


def render_edge_selection():

    edges = get_edge_servers()
    best_edge = select_best_edge(edges)

    st.markdown(
        '<div class="section-title">🏆 Multi-Edge Server Selection</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    for col, edge in zip([col1, col2, col3], edges):
        with col:
            selected = edge["name"] == best_edge["name"]
            if selected:
                 st.markdown(
        f"""
        <div class="edge-selected-badge">
            🏆 {edge['name']} SELECTED
        </div>
        """,
        unsafe_allow_html=True
    )
            else:
                 st.markdown(
        f"""
        <div class="edge-available-badge">
            {edge['name']} AVAILABLE
        </div>
        """,
        unsafe_allow_html=True
    )

            

            st.metric("Latency", f"{edge['latency']} ms")
            st.metric("CPU Usage", f"{edge['cpu']}%")
            st.metric("Bandwidth", f"{edge['bandwidth']} Mbps")
            st.metric("Edge Selection Score", f"{edge['score']:.1f}")

            st.progress(min(edge["score"] / 100, 1.0))
            st.caption(f"Selection Score: {edge['score']:.1f}")

    ranking_df = pd.DataFrame(edges)

    ranking_df = ranking_df[
        ["name", "latency", "cpu", "bandwidth", "score"]
    ].sort_values(
        by="score",
        ascending=False
    )

    ranking_df.insert(0, "Rank", ["🥇", "🥈", "🥉"])

    ranking_df = ranking_df.rename(
        columns={
            "name": "Edge Server",
            "latency": "Latency (ms)",
            "cpu": "CPU Load (%)",
            "bandwidth": "Bandwidth (Mbps)",
            "score": "Orchestration Score"
        }
    )

    st.markdown(
        '<div class="section-title">📊 Edge Server Ranking</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        ranking_df,
        use_container_width=True,
        hide_index=True
    )

    formula_html = f"""<div class="edge-formula-box">
<div class="edge-formula-title">⚡ Edge Selection Formula</div>
<div class="edge-formula-text">
50% Latency Efficiency<br>
30% Bandwidth Capacity<br>
20% CPU Availability
</div>
<div class="edge-formula-highlight">Higher Score = Better Edge Candidate</div>
</div>"""

    st.markdown(formula_html, unsafe_allow_html=True)

    result_html = f"""<div class="edge-result-box">
<div class="edge-result-title">🏆 Selected Edge Server: {best_edge['name']}</div>
<div class="edge-result-score">⚡ Orchestration Score: {best_edge['score']:.1f}</div>
<div class="edge-result-reason">
Reason: Highest orchestration score based on latency, bandwidth and CPU utilization.
</div>
</div>"""

    st.markdown(result_html, unsafe_allow_html=True)