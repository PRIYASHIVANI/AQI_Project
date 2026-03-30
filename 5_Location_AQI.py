import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# -------------------------------------------------
# LOCATION-BASED AQI MONITORING PAGE
# -------------------------------------------------
st.title("📍 Location-Based AQI Monitoring")
st.markdown("### City-wise Air Quality Status & Alerts")

st.markdown(
    """
    This page simulates **real-time, location-based AQI monitoring**.
    Users can select their city to view the **current AQI level**, associated
    **health risks**, and **safety recommendations**.

    Although Streamlit does not support native GPS, this module demonstrates
    how a **GPS-enabled mobile app** would function in real-world deployment.
    """
)

# -------------------------------------------------
# CITY SELECTION
# -------------------------------------------------
st.subheader("🏙️ Select Your Location")

city = st.selectbox(
    "Choose City",
    ["Chennai", "Delhi", "Mumbai", "Bengaluru", "Hyderabad", "Kolkata"]
)

# -------------------------------------------------
# SIMULATED LIVE AQI DATA
# -------------------------------------------------
np.random.seed(len(city))
current_aqi = np.random.randint(40, 320)

# -------------------------------------------------
# AQI CATEGORY LOGIC
# -------------------------------------------------
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good", "🟢"
    elif aqi <= 100:
        return "Moderate", "🟡"
    elif aqi <= 200:
        return "Poor", "🟠"
    elif aqi <= 300:
        return "Very Poor", "🔴"
    else:
        return "Severe", "☠️"

category, icon = get_aqi_category(current_aqi)

# -------------------------------------------------
# DISPLAY CURRENT AQI STATUS
# -------------------------------------------------
st.subheader("📊 Current AQI Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("City", city)

with col2:
    st.metric("Current AQI", current_aqi)

with col3:
    st.metric("AQI Category", f"{icon} {category}")

# -------------------------------------------------
# HEALTH ALERT MESSAGE
# -------------------------------------------------
st.subheader("🚨 Health Alert")

if category == "Good":
    st.success("Air quality is good. Enjoy your outdoor activities safely.")
elif category == "Moderate":
    st.info("Sensitive individuals should limit prolonged outdoor exertion.")
elif category == "Poor":
    st.warning("Avoid outdoor exercise. Wearing a mask is recommended.")
elif category == "Very Poor":
    st.error("Limit outdoor exposure. Use N95 masks if necessary.")
else:
    st.error("Severe air pollution detected. Stay indoors and avoid travel.")

# -------------------------------------------------
# SIMULATED ALERT HISTORY
# -------------------------------------------------
st.subheader("🕒 Recent AQI History (Last 7 Days)")

history_dates = pd.date_range(end=pd.Timestamp.today(), periods=7)
history_aqi = np.random.randint(60, 260, size=7)

history_df = pd.DataFrame({
    "Date": history_dates,
    "AQI": history_aqi
})

st.line_chart(history_df.set_index("Date"))

# -------------------------------------------------
# GPS & MOBILE APP NOTE
# -------------------------------------------------
st.subheader("📱 Mobile App Integration Concept")

st.markdown(
    """
    In a mobile deployment:
    - GPS automatically detects user location
    - AQI data is fetched in real time
    - Push notifications alert users when AQI becomes unsafe

    This Streamlit module acts as a **functional prototype** of that system.
    """
)

# -------------------------------------------------
# PROJECT COMPLETION NOTE
# -------------------------------------------------
st.success(
    "You have explored all modules of the Smart AQI Forecasting & Health Alert System."
)
