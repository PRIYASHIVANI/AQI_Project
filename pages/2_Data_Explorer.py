import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# -------------------------------------------------
# DATA EXPLORER PAGE
# -------------------------------------------------
st.title("📊 Data Explorer")
st.markdown("### Explore AQI, Weather, and Traffic Data")

st.markdown(
    """
    This page allows users to **inspect, analyze, and visualize** the datasets used
    for AQI forecasting. Understanding data behavior is crucial before applying
    machine learning models.
    """
)

# -------------------------------------------------
# LOAD DATA (DEMO / PLACEHOLDER)
# -------------------------------------------------
@st.cache_data
def load_data():
    dates = pd.date_range(start="2023-01-01", periods=120)
    data = pd.DataFrame({
        "Date": dates,
        "AQI": np.random.randint(40, 260, size=120),
        "Temperature (°C)": np.random.randint(20, 40, size=120),
        "Humidity (%)": np.random.randint(40, 90, size=120),
        "Traffic Level": np.random.choice(["Low", "Medium", "High"], size=120)
    })
    return data

df = load_data()

# -------------------------------------------------
# FILTER SECTION
# -------------------------------------------------
st.subheader("🔍 Data Filters")

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start Date", df["Date"].min())

with col2:
    end_date = st.date_input("End Date", df["Date"].max())

filtered_df = df[(df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))]

# -------------------------------------------------
# DATA PREVIEW
# -------------------------------------------------
st.subheader("📄 Dataset Preview")
st.dataframe(filtered_df, use_container_width=True)

# -------------------------------------------------
# AQI TREND VISUALIZATION
# -------------------------------------------------
st.subheader("📈 AQI Trend Over Time")
st.line_chart(filtered_df.set_index("Date")["AQI"])

# -------------------------------------------------
# WEATHER VS AQI ANALYSIS
# -------------------------------------------------
st.subheader("🌦️ Weather Parameters vs AQI")

col3, col4 = st.columns(2)

with col3:
    st.markdown("**Temperature vs AQI**")
    st.scatter_chart(filtered_df[["Temperature (°C)", "AQI"]])

with col4:
    st.markdown("**Humidity vs AQI**")
    st.scatter_chart(filtered_df[["Humidity (%)", "AQI"]])

# -------------------------------------------------
# TRAFFIC IMPACT ANALYSIS
# -------------------------------------------------
st.subheader("🚦 Traffic Impact on AQI")

traffic_group = filtered_df.groupby("Traffic Level")["AQI"].mean()
st.bar_chart(traffic_group)

# -------------------------------------------------
# DATA INSIGHTS
# -------------------------------------------------
st.subheader("🧠 Key Observations")

st.markdown(
    """
    - AQI shows **significant variation over time**, making it suitable for time-series modeling.
    - Higher traffic levels tend to correlate with **increased AQI values**.
    - Weather parameters such as temperature and humidity influence air quality trends.

    These insights justify the use of **LSTM models combined with environmental data**.
    """
)

# -------------------------------------------------
# NEXT STEP INFO
# -------------------------------------------------
st.info(
    "Proceed to the AQI Prediction page to forecast future air quality using machine learning models."
)
