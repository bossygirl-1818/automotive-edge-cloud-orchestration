import os
import pandas as pd
import streamlit as st
import plotly.express as px


FORECAST_FILE = "data/predictive_traffic_forecast.csv"


def render_predictive_traffic_dashboard():

    st.markdown(
        '<div class="section-title">🔮 Predictive Traffic Intelligence</div>',
        unsafe_allow_html=True
    )

    if not os.path.exists(FORECAST_FILE):
        st.warning("Prediction forecast not found. Run: python -m src.predictive_traffic_engine")
        return

    df = pd.read_csv(FORECAST_FILE)
    row = df.iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Congestion Score", row["predicted_congestion_score"])

    with col2:
        st.metric("Edge Load", f"{row['predicted_edge_load']}%")

    with col3:
        st.metric("Cloud Latency", f"{row['predicted_cloud_latency']} ms")

    with col4:
        st.metric("Battery Drain", f"{row['predicted_battery_drain']}%")
    risk_df = pd.DataFrame({
        "Forecast Area": [
            "Traffic Congestion",
            "Edge Load",
            "Cloud Latency",
            "Battery Drain"
        ],
        "Predicted Score": [
            row["predicted_congestion_score"],
            row["predicted_edge_load"],
            row["predicted_cloud_latency"],
            row["predicted_battery_drain"]
        ],
        "Risk Level": [
            row["predicted_congestion_level"],
            row["predicted_edge_risk"],
            row["predicted_cloud_risk"],
            row["predicted_battery_risk"]
        ],
        "Operational Meaning": [
            "Road traffic may become congested",
            "Edge node may face medium processing pressure",
            "Cloud response time may increase",
            "Vehicle battery usage may rise"
        ]
    })

    def risk_badge(level):
        if level == "HIGH":
            return "🔴 HIGH"
        if level == "MEDIUM":
            return "🟡 MEDIUM"
        return "🟢 LOW"

    risk_df["Risk Level"] = risk_df["Risk Level"].apply(risk_badge)

    st.markdown(
        '<div class="section-title">Forecast Risk Assessment Table</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        risk_df,
        use_container_width=True,
        hide_index=True,
        height=260
    )