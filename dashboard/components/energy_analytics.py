import streamlit as st
import plotly.express as px

from src.db_queries import get_telemetry


def render_energy_analytics():

    df = get_telemetry()

    avg_battery = df["battery"].mean()
    max_battery = df["battery"].max()
    min_battery = df["battery"].min()

    energy_efficiency = (
    df["battery"].mean() / df["battery"].max()
) * 100

    st.markdown(
        '<div class="section-title">🔋 Energy Analytics</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Avg Battery", f"{avg_battery:.2f}%")

    with col2:
        st.metric("Max Battery", f"{max_battery:.0f}%")

    with col3:
        st.metric("Min Battery", f"{min_battery:.0f}%")

    with col4:
        st.metric("Energy Efficiency", f"{energy_efficiency:.2f}%")

    fig = px.line(
        df,
        x="episode",
        y="battery",
        markers=False,
        title="Battery Consumption Trend"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff"),
        height=460,
        showlegend=False,
        margin=dict(l=30, r=30, t=50, b=30)
    )

    fig.update_traces(
        line=dict(
            width=4,
            color="#38bdf8"
        )
    )

    fig.update_xaxes(
        title="Episode",
        gridcolor="#1e293b"
    )

    fig.update_yaxes(
        title="Battery Level (%)",
        gridcolor="#1e293b"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )