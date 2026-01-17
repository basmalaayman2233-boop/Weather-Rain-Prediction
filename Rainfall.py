import streamlit as st
import pickle
import numpy as np

rf_model = pickle.load(open("RandomForestClassifier_model.pkl", "rb"))
log_model = pickle.load(open("logistic_model.pkl", "rb"))

st.title( "Rainfall Prediction App")
st.write("Enter the weather values ​​and predict whether it will rain today.")

model_choice = st.selectbox(
    "Choose the model type:",
    ["Random Forest", "Logistic Regression"]
)

pressure = st.number_input("Pressure (hPa):", min_value=900.0, max_value=1100.0, step=0.5)
dewpoint = st.number_input("Dew Point (°C):", min_value=-10.0, max_value=35.0, step=0.5)
humidity = st.number_input("Humidity (%):", min_value=0.0, max_value=100.0, step=1.0)
cloud = st.number_input("Cloud Cover (oktas):", min_value=0.0, max_value=8.0, step=1.0)
rainfall = st.number_input("Previous Day Rainfall (mm):", min_value=0.0, max_value=300.0, step=0.1)
sunshine = st.number_input("Sunshine Duration (hours):", min_value=0.0, max_value=15.0, step=0.1)
windspeed = st.number_input("Wind Speed (km/h):", min_value=0.0, max_value=50.0, step=0.5)

input_data = np.array([[pressure, dewpoint, humidity, cloud, rainfall, sunshine, windspeed]])

if st.button("Predict Rainfall"):
    if model_choice == "Random Forest":
        prediction = rf_model.predict(input_data)[0]
    else:
        prediction = log_model.predict(input_data)[0]

    if prediction == 1:
        st.success("It will RAIN today!")
    else:
        st.info("No rain expected today.")
