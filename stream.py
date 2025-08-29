# -----------------------------
# YouTube Ad Revenue Prediction - Streamlit App
# -----------------------------
import streamlit as st
import pandas as pd
import joblib

# Load trained model (pipeline saved from youtube.py)
model = joblib.load("lasso_youtube_model.pkl")

st.title("📺 YouTube Ad Revenue Predictor")
st.write("Enter video details to predict estimated ad revenue:")

# 1. User Inputs
views = st.number_input(":blue[Views 👁️]", min_value=0, value=10000)
likes = st.number_input("Likes 👍", min_value=0, value=500)
comments = st.number_input("Comments 💬", min_value=0, value=200)
watch_time = st.number_input("Watch Time (minutes) ⏱️", min_value=0, value=20000)
video_length = st.number_input("Video Length (minutes) 🎬", min_value=1, value=15)
subscribers = st.number_input("Subscribers 👥", min_value=0, value=10000)

category = st.selectbox("Category 🗂️", ["Education", "Gaming", "Music", "Vlogs", "Tech", "Other"])
device = st.selectbox("Device 📱", ["Mobile", "Desktop", "Tablet", "TV"])
country = st.selectbox("Country 🌍", ["US", "IN", "UK", "CA", "AU", "Others"])

date = pd.to_datetime(st.date_input("Upload Date 🗓️"))
year, month, day_of_week = date.year, date.month, date.weekday()

# 2. Prepare Input DataFrame
input_data = pd.DataFrame([{
    "views": views,
    "likes": likes,
    "comments": comments,
    "watch_time_minutes": watch_time,
    "video_length_minutes": video_length,
    "subscribers": subscribers,
    "category": category,
    "device": device,
    "country": country,
    "year": year,
    "month": month,
    "day_of_week": day_of_week
}])

# 3. Predict
if st.button("Predict Revenue"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Ad Revenue: ${prediction:.2f}")
