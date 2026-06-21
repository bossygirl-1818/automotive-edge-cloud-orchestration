import streamlit as st


def get_hybrid_decision(ml_decision, dqn_decision):

    if ml_decision == dqn_decision:
        final_decision = ml_decision
        reason = "ML and DQN agree on the same offloading target."
        confidence = "High"

    else:
        final_decision = dqn_decision
        reason = "DQN selected as final engine because it adapts using reward-based learning."
        confidence = "Adaptive"

    return final_decision, reason, confidence


def render_hybrid_orchestrator(ml_decision, dqn_decision):

    final_decision, reason, confidence = get_hybrid_decision(
        ml_decision,
        dqn_decision
    )

    st.markdown(
        '<div class="section-title">🤖 Hybrid Orchestrator Decision</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ML Decision", ml_decision)

    with col2:
        st.metric("DQN Decision", dqn_decision)

    with col3:
        st.metric("Final Decision", final_decision)

    if confidence == "High":
        st.success(f"Confidence: {confidence} | {reason}")
    else:
        st.warning(f"Confidence: {confidence} | {reason}")

    return {
        "final_decision": final_decision,
        "reason": reason,
        "confidence": confidence
    }