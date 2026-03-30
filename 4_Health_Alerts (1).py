import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# -------------------------------------------------
# HEALTH ALERTS PAGE
# -------------------------------------------------
st.title("🚨 Health Alerts & Recommendations")
st.markdown("### AQI-Based Health Risk Assessment")

st.markdown(
    """
    This module converts **predicted AQI values into meaningful health advice**.
    Instead of showing only pollution numbers, the system provides **actionable
    recommendations** to help users protect their health.
    """
)

# -------------------------------------------------
# USER INPUT
# -------------------------------------------------
st.subheader("🧾 Input AQI Value")

col1, col2 = st.columns(2)

with col1:
    city = st.selectbox("Select City", ["Chennai", "Delhi", "Mumbai", "Bengaluru"])

with col2:
    aqi_value = st.slider("AQI Value", min_value=0, max_value=500, value=120)

# -------------------------------------------------
# AQI CATEGORY & HEALTH LOGIC
# -------------------------------------------------
def get_health_alert(aqi):
    if aqi <= 50:
        return "Good", "🟢 Air quality is excellent. Safe for all activities.", "success"
    elif aqi <= 100:
        return "Moderate", "🟡 Sensitive individuals should limit prolonged outdoor exertion.", "info"
    elif aqi <= 200:
        return "Poor", "🟠 Avoid outdoor exercise. Consider wearing a mask.", "warning"
    elif aqi <= 300:
        return "Very Poor", "🔴 Limit outdoor exposure. Use N95 masks if necessary.", "error"
    else:
        return "Severe", "☠️ Stay indoors. Outdoor activities are strongly discouraged.", "error"

category, message, level = get_health_alert(aqi_value)

# -------------------------------------------------
# DISPLAY ALERT
# -------------------------------------------------
st.subheader("📢 Health Alert")

if level == "success":
    st.success(f"**{category}** – {message}")
elif level == "info":
    st.info(f"**{category}** – {message}")
elif level == "warning":
    st.warning(f"**{category}** – {message}")
else:
    st.error(f"**{category}** – {message}")

# -------------------------------------------------
# DETAILED HEALTH RECOMMENDATIONS
# -------------------------------------------------
st.subheader("🩺 Detailed Health Recommendations")

recommendations = {
    "Good": [
        "Enjoy outdoor activities",
        "Ideal conditions for exercise",
        "No health risk"
    ],
    "Moderate": [
        "People with asthma should be cautious",
        "Reduce prolonged outdoor exposure",
        "Monitor symptoms"
    ],
    "Poor": [
        "Wear a mask outdoors",
        "Avoid jogging or cycling",
        "Children and elderly should stay indoors"
    ],
    "Very Poor": [
        "Use N95 masks",
        "Avoid outdoor travel",
        "Increase indoor air filtration"
    ],
    "Severe": [
        "Stay indoors",
        "Seek medical help if breathing issues occur",
        "Use air purifiers"
    ]
}

for rec in recommendations[category]:
    st.write(f"• {rec}")

# -------------------------------------------------
# HEALTH IMPACT NOTE
# -------------------------------------------------
st.subheader("❤️ Why Health Alerts Matter")

st.markdown(
    """
    Prolonged exposure to polluted air can cause:
    - Respiratory diseases
    - Cardiovascular problems
    - Reduced lung function

    This system helps **prevent health risks through early warnings**.
    """
)

# -------------------------------------------------
# NEXT STEP INFO
# -------------------------------------------------
st.info(
    "Proceed to the Location AQI page for city-wise monitoring and alerts."
)
