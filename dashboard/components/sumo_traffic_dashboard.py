import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


DB_PATH = "data/orchestrator.db"


def render_chart_card(fig):
    st.markdown('<div class="graph-card">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


def style_donut_chart(fig, center_text):
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        textfont=dict(
            color="white",
            size=16
        ),
        marker=dict(
            line=dict(
                color="#020617",
                width=4
            )
        )
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(
            color="#ffffff",
            size=15
        ),
        height=380,
        showlegend=False,
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        annotations=[
            dict(
                text=center_text,
                x=0.5,
                y=0.5,
                font=dict(
                    size=28,
                    color="#38bdf8"
                ),
                showarrow=False
            )
        ]
    )

    return fig


def style_standard_chart(fig, height=430):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(
            color="#ffffff",
            size=15
        ),
        title=dict(
            font=dict(
                color="#ffffff",
                size=20
            ),
            x=0.02
        ),
        height=height,
        margin=dict(
            l=60,
            r=35,
            t=80,
            b=65
        ),
        showlegend=False
    )

    fig.update_xaxes(
        gridcolor="#1e293b",
        zerolinecolor="#334155",
        title_font=dict(
            color="#ffffff",
            size=15
        ),
        tickfont=dict(
            color="#ffffff",
            size=13
        )
    )

    fig.update_yaxes(
        gridcolor="#1e293b",
        zerolinecolor="#334155",
        title_font=dict(
            color="#ffffff",
            size=15
        ),
        tickfont=dict(
            color="#ffffff",
            size=13
        )
    )

    return fig


def render_sumo_traffic_dashboard():

    st.markdown(
        '<div class="section-title">🚗🚦 SUMO Traffic Intelligence Dashboard</div>',
        unsafe_allow_html=True
    )

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM sumo_orchestration_tasks",
        conn
    )

    conn.close()

    if df.empty:
        st.warning("No SUMO traffic data found.")
        return

    avg_speed = df["speed"].mean()
    max_speed = df["speed"].max()
    min_speed = df["speed"].min()
    avg_battery = df["battery"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Avg Speed", f"{avg_speed:.2f} m/s")

    with col2:
        st.metric("Max Speed", f"{max_speed:.2f} m/s")

    with col3:
        st.metric("Min Speed", f"{min_speed:.2f} m/s")

    with col4:
        st.metric("Avg Battery", f"{avg_battery:.2f}%")

    density_counts = (
        df["traffic_density"]
        .value_counts()
        .reset_index()
    )

    density_counts.columns = [
        "Traffic Density",
        "Count"
    ]

    total_records = density_counts["Count"].sum()

    fig1 = px.pie(
        density_counts,
        names="Traffic Density",
        values="Count",
        hole=0.58,
        color="Traffic Density",
        color_discrete_map={
            "LOW": "#22c55e",
            "MEDIUM": "#facc15",
            "HIGH": "#ef4444"
        }
    )

    fig1 = style_donut_chart(
        fig1,
        f"{total_records}<br>Records"
    )

    render_chart_card(fig1)

    network_counts = (
        df["network_quality"]
        .value_counts()
        .reset_index()
    )

    network_counts.columns = [
        "Network Quality",
        "Count"
    ]

    fig2 = px.bar(
        network_counts,
        x="Network Quality",
        y="Count",
        title="Network Quality Distribution"
    )

    fig2 = style_standard_chart(fig2)

    fig2.update_xaxes(
        title="Network Quality"
    )

    fig2.update_yaxes(
        title="Count"
    )

    render_chart_card(fig2)

    speed_df = (
        df.groupby("step")["speed"]
        .mean()
        .reset_index()
    )

    fig3 = px.line(
        speed_df,
        x="step",
        y="speed",
        title="Average Vehicle Speed Over SUMO Simulation Steps"
    )

    fig3 = style_standard_chart(fig3)

    fig3.update_traces(
        line=dict(
            width=4,
            color="#38bdf8"
        )
    )

    fig3.update_xaxes(
        title="Simulation Step"
    )

    fig3.update_yaxes(
        title="Average Speed (m/s)"
    )

    render_chart_card(fig3)

    vehicle_count_df = (
        df.groupby("step")["vehicle_id"]
        .nunique()
        .reset_index()
    )

    fig4 = px.line(
        vehicle_count_df,
        x="step",
        y="vehicle_id",
        title="Active Vehicle Count Over Time"
    )

    fig4 = style_standard_chart(fig4)

    fig4.update_traces(
        line=dict(
            width=4,
            color="#38bdf8"
        )
    )

    fig4.update_xaxes(
        title="Simulation Step"
    )

    fig4.update_yaxes(
        title="Active Vehicles"
    )

    render_chart_card(fig4)

    st.markdown(
        '<div class="section-title">📋 SUMO Traffic Data</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=350
    )