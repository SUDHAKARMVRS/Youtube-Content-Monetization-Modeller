# -------------------------------------------------------
# 🎬 YouTube Ad Revenue Prediction - Streamlit Dashboard
# -------------------------------------------------------
import streamlit as st
import pandas as pd
import joblib
from datetime import date

# Load trained model
model = joblib.load("best_youtube_model.pkl")

# ----------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------
st.set_page_config(
    page_title="YouTube Ad Revenue Predictor",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------
# SIDEBAR THEME TOGGLE
# ----------------------------------------------
# Sidebar Theme Selector
st.sidebar.title("🧭 Theme Selection")
theme = st.sidebar.selectbox(
    "🎨 Choose a Theme",
    ["🌞 Light Mode", "🌙 Dark Mode", "🌅 Sunset", "🧊 Aqua", "🌸 Rose"]
)


# ----------------------------------------------
# COLOR SETTINGS BASED ON THEME
# ----------------------------------------------
if "Light" in theme:
    bg_color = "#f5f7fa"
    text_color = "#FAF9F9"
    card_bg = "#131617"
    gradient = "linear-gradient(90deg, #36D1DC, #5B86E5)"  # Blue gradient
    particle_color = "#111111"
    line_color = "rgba(0,0,0,0.25)"

elif "Dark" in theme:
    bg_color = "#0e1117"
    text_color = "#ffffff"
    card_bg = "rgba(255,255,255,0.08)"
    gradient = "linear-gradient(90deg, #141E30, #243B55)"  # Deep navy gradient
    particle_color = "#ffffff"
    line_color = "rgba(255,255,255,0.15)"

elif "Sunset" in theme:
    bg_color = "#ff9966"
    text_color = "#020101"
    card_bg = "rgba(255,255,255,0.2)"
    gradient = "linear-gradient(90deg, #ff5f6d, #ffc371)"  # Pink-orange blend
    particle_color = "#ffffff"
    line_color = "rgba(255,255,255,0.3)"

elif "Aqua" in theme:
    bg_color = "#d9faff"
    text_color = "#020303"
    card_bg = "#45779d"
    gradient = "linear-gradient(90deg, #1CB5E0, #000851)"  # Aqua blue
    particle_color = "#003366"
    line_color = "rgba(0,51,102,0.25)"

elif "Rose" in theme:
    bg_color = "#ffe6f7"
    text_color = "#4a004e"
    card_bg = "#ffffff"
    gradient = "linear-gradient(90deg, #ff9a9e, #fad0c4)"  # Rose-pink blend
    particle_color = "#4a004e"
    line_color = "rgba(74,0,78,0.25)"


# ----------------------------------------------
# CUSTOM DYNAMIC CSS
# ----------------------------------------------

st.markdown(f"""
<style>
/* Background */
[data-testid="stAppViewContainer"] {{
    background: {bg_color};
    color: {text_color};
    transition: all 0.5s ease-in-out;
}}

/* Header */
.gradient-header {{
    background: {gradient};
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    color: white;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}}

/* Expander Styling */
div[data-testid="stExpander"] {{
    background-color: {card_bg};
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}}

/* Predict Button */
div.stButton > button {{
    background: linear-gradient(90deg, #ff4b1f, #1fddff);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 30px;
    font-size: 18px;
    font-weight: 600;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
    transition: 0.3s ease-in-out;
}}
div.stButton > button:hover {{
    transform: scale(1.05);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.6);
}}

/* Result Box (Glassmorphism) */
.result-box {{
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.2);
    padding: 35px;
    text-align: center;
    margin-top: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}}
.result-title {{
    color: #ff6a00;
    font-size: 28px;
    font-weight: bold;
}}
.result-value {{
    color: #1fddff;
    font-size: 52px;
    font-weight: bold;
}}

/* Footer */
.footer {{
    text-align:center;
    color:#bbb;
    margin-top:40px;
    font-size:16px;
}}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------
# HEADER
# ----------------------------------------------
st.markdown("""
<div class="gradient-header">
    <h1>🎥 YouTube Ad Revenue Predictor 💰</h1>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<style>
.gradient-header {
    background-color: #121212;
    text-align: center;
    padding: 25px;
    border-radius: 15px;
    font-family: 'Poppins', sans-serif;
}
.gradient-header h1 {
    color: #00ffff;
    font-size: 2.2rem;
    text-shadow: 0 0 15px #00ffff;
}
</style>

<div class="gradient-header">
    <h1>💡 Enter Details - Predict Revenue 💰</h1>
</div>
""", unsafe_allow_html=True)
st.markdown("-----")

# ----------------------------------------------
# INPUT SECTION
# ----------------------------------------------
# ----------------------------------------------
# INPUT SECTION
# ----------------------------------------------
col1, col2 ,col3 = st.columns(3)

with col1:
    with st.expander("🎯 Basic Video Info ", expanded=True):
        views = st.number_input("Views 👀", min_value=0, value=10000)
        likes = st.number_input("Likes 🔥", min_value=0, value=500)
        comments = st.number_input("Comments 💬", min_value=0, value=200)


with col2:
    with st.expander("📈 Engagement Metrics", expanded=True):
        watch_time = st.number_input("Watch Time (minutes) ⏱️", min_value=0, value=20000)
        subscribers = st.number_input("Subscribers 🧑‍🤝‍🧑", min_value=0, value=10000)

with col3:
    with st.expander("⚙️ Additional Info", expanded=True):
        video_length = st.number_input("Video Length (minutes) 🎞️", min_value=1, value=15)
        category = st.selectbox("Category 🎓", ["Education", "Entertainment", "Tech", "Gaming"])
        device = st.selectbox("Device 💻", ["Mobile", "Desktop", "Tablet"])
        country = st.selectbox("Country 🌍", ["US", "India", "UK", "Canada"])
        date_input = st.date_input("Date 📅", value=date.today())
        year, month, day_of_week = date_input.year, date_input.month, date_input.weekday()


# ----------------------------------------------
# FEATURE ENGINEERING
# ----------------------------------------------
engagement_rate = (likes + comments) / views if views > 0 else 0
watch_time_per_view = watch_time / views if views > 0 else 0
views_per_subscriber = views / subscribers if subscribers > 0 else 0
subscribers_per_view = subscribers / views if views > 0 else 0
ad_revenue_per_view = 0  # placeholder

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
    "engagement_rate": engagement_rate,
    "watch_time_per_view": watch_time_per_view,
    "views_per_subscriber": views_per_subscriber,
    "subscribers_per_view": subscribers_per_view,
    "ad_revenue_per_view": ad_revenue_per_view,
    "year": year,
    "month": month,
    "day_of_week": day_of_week
}])

# ----------------------------------------------
# PREDICTION SECTION
# ----------------------------------------------
if st.button("🚀 Predict Revenue", key="predict_button"):
    prediction = model.predict(input_data)[0]
    prediction = max(0, prediction)
    st.markdown(f"""
        <div class="result-box">
            <div class="result-title">💵 Estimated Ad Revenue</div>
            <div class="result-value">${prediction:,.2f}</div>
            <p style="color:lightgray;">(Based on provided metrics)</p>
        </div>
    """, unsafe_allow_html=True)
st.balloons()

# ----------------------------------------------
# FOOTER
# ----------------------------------------------
st.markdown("""
<div class="footer">
    Built with 🧠 using <b>Streamlit</b> | Designed by <b>Sudhakar M</b><br>
    <small>© 2025 YouTube Revenue Predictor</small>
</div>
""", unsafe_allow_html=True)
