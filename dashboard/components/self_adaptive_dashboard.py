import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


DB_PATH = "data/orchestrator.db"
TABLE_NAME = "self_adaptive_history"


def render_self_adaptive_dashboard():

    st.markdown(
        '<div class="section-title">🔁 Self-Adaptive Control Loop</div>',
        unsafe_allow_html=True
    )

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME}", conn)
    conn.close()

    if df.empty:
        st.warning("No self-adaptive history found. Run: python -m src.self_adaptive_history")
        return

    df["override_status"] = df.apply(
        lambda row: "OVERRIDDEN" if row["rl_decision"] != row["final_decision"] else "ACCEPTED",
        axis=1
    )

    overrides = df[df["override_status"] == "OVERRIDDEN"]
    override_rate = (len(overrides) / len(df)) * 100

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Adaptive Records", len(df))

    with col2:
        st.metric("Overrides", len(overrides))

    with col3:
        st.metric("Override Rate", f"{override_rate:.2f}%")

    with col4:
        st.metric("Most Final Decision", df["final_decision"].mode()[0])

    final_counts = df["final_decision"].value_counts().reset_index()
    final_counts.columns = ["Decision", "Count"]

    fig1 = px.pie(
        final_counts,
        names="Decision",
        values="Count",
        hole=0.58,
        color="Decision",
        color_discrete_map={
            "EDGE": "#38bdf8",
            "VEHICLE": "#22c55e",
            "CLOUD": "#f97316"
        }
    )

    fig1.update_traces(
        textposition="inside",
        textinfo="percent+label",
        textfont=dict(color="white", size=16),
        marker=dict(line=dict(color="#020617", width=4))
    )

    fig1.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        height=500,
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
        annotations=[
            dict(
                text=f"{len(df)}<br>Decisions",
                x=0.5,
                y=0.5,
                font=dict(size=24, color="#38bdf8"),
                showarrow=False
            )
        ]
    )

    st.plotly_chart(fig1, use_container_width=True, key="self_adaptive_final_decision_donut")

    override_counts = df["override_status"].value_counts().reset_index()
    override_counts.columns = ["Status", "Count"]

    fig2 = px.pie(
        override_counts,
        names="Status",
        values="Count",
        hole=0.58,
        color="Status",
        color_discrete_map={
            "ACCEPTED": "#22c55e",
            "OVERRIDDEN": "#ef4444"
        }
    )

    fig2.update_traces(
        textposition="inside",
        textinfo="percent+label",
        textfont=dict(color="white", size=16),
        marker=dict(line=dict(color="#020617", width=4))
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        height=500,
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
        annotations=[
            dict(
                text=f"{len(df)}<br>Records",
                x=0.5,
                y=0.5,
                font=dict(size=24, color="#38bdf8"),
                showarrow=False
            )
        ]
    )

    st.plotly_chart(fig2, use_container_width=True, key="self_adaptive_override_donut")

    reason_counts = df["adaptation_reason"].value_counts().head(10).reset_index()
    reason_counts.columns = ["Adaptation Reason", "Count"]

    fig3 = px.bar(
        reason_counts,
        x="Count",
        y="Adaptation Reason",
        orientation="h",
        title="Top Adaptation Reasons"
    )

    fig3.update_layout(
        template="plotly_dark",
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#ffffff", size=15),
        height=500,
        margin=dict(l=40, r=40, t=70, b=40)
    )

    st.plotly_chart(fig3, use_container_width=True, key="self_adaptive_reason_bar")

    st.markdown(
        '<div class="section-title">Latest Self-Adaptive Decisions</div>',
        unsafe_allow_html=True
    )

    latest_df = df[
        [
            "timestamp",
            "vehicle_id",
            "rl_decision",
            "final_decision",
            "traffic_density",
            "battery",
            "speed",
            "adaptation_reason"
        ]
    ].tail(15)

    st.dataframe(
        latest_df,
        use_container_width=True,
        hide_index=True,
        height=400
    )