import streamlit as st


def get_decision_reason(
    task_type,
    latency,
    priority,
    decision,
    edge_delay,
    cloud_delay,
    battery
):

    reasons = []

    reasons.append(f"✓ Task latency = {latency} ms")
    reasons.append(f"✓ Task priority = {priority}")

    if battery < 25:
        reasons.append(f"✓ Battery level is low ({battery:.0f}%)")

    if decision == "VEHICLE":
        reasons.append("✓ Ultra-low latency workload")
        reasons.append("✓ Local processing provides fastest response")
        reasons.append("✓ Network transmission avoided")

    elif decision == "EDGE":
        reasons.append(
            f"✓ Edge latency ({edge_delay:.0f} ms) lower than cloud latency ({cloud_delay:.0f} ms)"
        )
        reasons.append("✓ Medium-latency workload suitable for edge processing")
        reasons.append("✓ Reduced cloud dependency")

    elif decision == "CLOUD":
        reasons.append("✓ High-latency-tolerant workload")
        reasons.append("✓ Cloud provides scalable compute resources")
        reasons.append("✓ Local processing not required")

    return reasons


def render_explainability(
    task_type,
    latency,
    priority,
    decision,
    edge_delay,
    cloud_delay,
    battery
):

    reasons = get_decision_reason(
        task_type,
        latency,
        priority,
        decision,
        edge_delay,
        cloud_delay,
        battery
    )

    st.markdown(
        '<div class="graph-card"><div class="graph-title">🧠 AI Decision Explainability</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Task Type", task_type)
        st.metric("Latency", f"{latency} ms")

    with col2:
        st.metric("Priority", priority)
        st.metric("Decision", decision)

    st.markdown(
        """
        <h3 style="
            color:#ffffff;
            font-size:28px;
            margin-bottom:25px;
        ">
            Decision Reason
        </h3>
        """,
        unsafe_allow_html=True
    )

    for reason in reasons:
        st.markdown(
            f"""
            <div style="
                color:#f8fafc;
                font-size:18px;
                font-weight:600;
                margin-bottom:12px;
            ">
                {reason}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div style="
            background:rgba(34,197,94,0.15);
            border-left:5px solid #22c55e;
            padding:18px;
            border-radius:10px;
            color:#22c55e;
            font-size:24px;
            font-weight:700;
            margin-top:20px;
        ">
            Selected Target: {decision}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)