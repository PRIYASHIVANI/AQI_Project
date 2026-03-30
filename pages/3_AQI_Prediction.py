import streamlit as st
import pandas as pd
import numpy as np
from datetime import timedelta

st.set_page_config(layout="wide")

# -------------------------------------------------
# AQI PREDICTION PAGE
# -------------------------------------------------
st.title("🤖 AQI Prediction & Forecasting")
st.markdown("### Machine Learning–Based Air Quality Forecast")

st.markdown(
    """
    This page performs **AQI forecasting** using machine learning techniques.
    The system demonstrates how historical AQI patterns combined with
    environmental factors can be used to **predict future air quality**.

    For demonstration, a **simulated ML prediction pipeline** is used. The same
    interface can be directly connected to trained **LSTM or regression models**.
    """
)

# -------------------------------------------------
# USER INPUT SECTION
# -------------------------------------------------
st.subheader("🧾 Prediction Inputs")

col1, col2, col3 = st.columns(3)

with col1:
    city = st.selectbox("Select City", ["Chennai", "Delhi", "Mumbai", "Bengaluru"])

with col2:
    forecast_days = st.slider("Forecast Days", min_value=1, max_value=7, value=3)

with col3:
    model_type = st.radio("Select Model", ["Regression Model", "LSTM Model"])

# -------------------------------------------------
# GENERATE HISTORICAL DATA (DEMO)
# -------------------------------------------------
dates = pd.date_range(start="2024-01-01", periods=30)
historical_aqi = np.random.randint(60, 220, size=30)

history_df = pd.DataFrame({
    "Date": dates,
    "AQI": historical_aqi
})

# -------------------------------------------------
# PREDICTION LOGIC (SIMULATION)
# -------------------------------------------------
last_aqi = history_df["AQI"].iloc[-1]
predicted_values = []

for i in range(forecast_days):
    variation = np.random.randint(-10, 15)
    next_value = max(20, last_aqi + variation)
    predicted_values.append(next_value)
    last_aqi = next_value

future_dates = [dates[-1] + timedelta(days=i+1) for i in range(forecast_days)]

forecast_df = pd.DataFrame({
    "Date": future_dates,
    "Predicted AQI": predicted_values
})

# -------------------------------------------------
# DISPLAY HISTORICAL DATA
# -------------------------------------------------
st.subheader("📜 Historical AQI Data")
st.line_chart(history_df.set_index("Date"))

# -------------------------------------------------
# DISPLAY FORECAST RESULTS
# -------------------------------------------------
st.subheader("📈 AQI Forecast Results")
st.line_chart(forecast_df.set_index("Date"))

# -------------------------------------------------
# AQI CATEGORY FUNCTION
# -------------------------------------------------
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Poor"
    elif aqi <= 300:
        return "Very Poor"
    else:
        return "Severe"

latest_prediction = predicted_values[-1]
category = get_aqi_category(latest_prediction)

# -------------------------------------------------
# PREDICTION SUMMARY
# -------------------------------------------------
st.subheader("📌 Prediction Summary")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric("City", city)

with col5:
    st.metric("Predicted AQI", latest_prediction)

with col6:
    st.metric("AQI Category", category)

# -------------------------------------------------
# MODEL INFORMATION
# -------------------------------------------------
st.subheader("🧠 Model Information")

if model_type == "Regression Model":
    st.info(
        "The regression model provides a baseline AQI prediction based on historical averages."
    )
else:
    st.info(
        "The LSTM model captures long-term temporal patterns in AQI data for improved forecasting."
    )

# -------------------------------------------------
# NEXT STEP INFO
# -------------------------------------------------
st.success(
    "Proceed to the Health Alerts page to view safety recommendations based on predicted AQI levels."
)
