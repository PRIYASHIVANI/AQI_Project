import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# -------------------------------------------------
# HOME / DASHBOARD PAGE
# -------------------------------------------------
st.title("🏠 Project Overview Dashboard")
st.markdown("### Smart AQI Forecasting & Health Alert System")

st.markdown(
    """
    Air pollution is a silent public health emergency. This dashboard gives a **high-level
    overview** of air quality, its health impact, and how this system helps users make
    informed decisions.

    This application aligns with **SDG 3 – Good Health and Well-being** by transforming
    raw AQI numbers into **actionable health intelligence**.
    """
)

# -------------------------------------------------
# AQI CATEGORY INFORMATION
# -------------------------------------------------
st.subheader("🌈 AQI Categories & Meaning")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.success("Good\n\n0–50\n\nAir quality is satisfactory")

with col2:
    st.info("Moderate\n\n51–100\n\nAcceptable but sensitive groups cautious")

with col3:
    st.warning("Poor\n\n101–200\n\nBreathing discomfort")

with col4:
    st.error("Very Poor\n\n201–300\n\nHealth warnings")

with col5:
    st.error("Severe\n\n301+\n\nSerious health effects")

# -------------------------------------------------
# SYSTEM HIGHLIGHTS
# -------------------------------------------------
st.subheader("🚀 System Highlights")

st.markdown(
    """
    - ✅ Uses **Machine Learning (LSTM + Regression)** for AQI forecasting
    - ✅ Integrates **weather and traffic data** to improve accuracy
    - ✅ Provides **health alerts instead of raw numbers**
    - ✅ Designed as a **full-stack data science application**
    """
)

# -------------------------------------------------
# SAMPLE LIVE AQI (DEMO DATA)
# -------------------------------------------------
st.subheader("📍 Sample City AQI Snapshot")

sample_data = pd.DataFrame({
    "City": ["Chennai", "Delhi", "Mumbai", "Bengaluru"],
    "AQI": [82, 245, 136, 65],
    "Category": ["Moderate", "Very Poor", "Poor", "Moderate"]
})

st.dataframe(sample_data, use_container_width=True)

# -------------------------------------------------
# WHY THIS PROJECT MATTERS
# -------------------------------------------------
st.subheader("❤️ Why This Project Matters")

st.markdown(
    """
    Traditional AQI systems:
    - Only show numeric AQI values
    - Do not explain **health consequences**
    - Lack **real-time personalized alerts**

    Our system bridges this gap by combining **AI + public health intelligence**.
    """
)

# -------------------------------------------------
# NAVIGATION HELP
# -------------------------------------------------
st.info(
    "Use the sidebar to explore data, run AQI predictions, and view health alerts."
)
