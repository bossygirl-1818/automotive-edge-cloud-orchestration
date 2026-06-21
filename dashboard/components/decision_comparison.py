import streamlit as st


def render_decision_comparison(ml_decision, dqn_decision):

    agreement = ml_decision == dqn_decision

    if agreement:
        agreement_text = "✅ YES"
        engine = "ML + DQN"
        agreement_bg = "rgba(34,197,94,0.18)"
    else:
        agreement_text = "❌ NO"
        engine = "DQN"
        agreement_bg = "rgba(239,68,68,0.18)"

    st.markdown(
        '<div class="comparison-header">📊 Decision Comparison</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
<div class="comparison-mini-card">
    <div class="comparison-label">ML Decision</div>
    <div class="comparison-value">{ml_decision}</div>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
<div class="comparison-mini-card">
    <div class="comparison-label">DQN Decision</div>
    <div class="comparison-value">{dqn_decision}</div>
</div>
""", unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(f"""
<div class="comparison-status-card" style="background:{agreement_bg};">
    Agreement Score: {agreement_text}
</div>
""", unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
<div class="comparison-engine-card">
    Selected Engine: {engine}
</div>
""", unsafe_allow_html=True)