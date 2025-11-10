# -------------------------------------------------------
# 🎬 YouTube Ad Revenue Prediction - Streamlit Dashboard
# -------------------------------------------------------
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
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
st.sidebar.title("🧭 Theme Selection")
theme = st.sidebar.selectbox(
    "🎨 Choose a Theme",
    ["🌙 Dark Mode","🌞 Light Mode",  "🌅 Sunset", "🧊 Aqua", "🌸 Rose"]
)

# ----------------------------------------------
# COLOR SETTINGS BASED ON THEME
# ----------------------------------------------
if "Light" in theme:
    bg_color = "#f5f7fa"
    text_color = "#131617"
    card_bg = "#ffffff"
    gradient = "linear-gradient(90deg, #36D1DC, #5B86E5)"
elif "Dark" in theme:
    bg_color = "#0e1117"
    text_color = "#ffffff"
    card_bg = "rgba(255,255,255,0.08)"
    gradient = "linear-gradient(90deg, #141E30, #243B55)"
elif "Sunset" in theme:
    bg_color = "#ff9966"
    text_color = "#020101"
    card_bg = "rgba(255,255,255,0.2)"
    gradient = "linear-gradient(90deg, #ff5f6d, #ffc371)"
elif "Aqua" in theme:
    bg_color = "#d9faff"
    text_color = "#020303"
    card_bg = "#c4e9f2"
    gradient = "linear-gradient(90deg, #1CB5E0, #000851)"
elif "Rose" in theme:
    bg_color = "#ffe6f7"
    text_color = "#4a004e"
    card_bg = "#ffffff"
    gradient = "linear-gradient(90deg, #ff9a9e, #fad0c4)"

# ----------------------------------------------
# ANIMATED BACKGROUND
# ----------------------------------------------
st.markdown("""
<style>
#particles-js {
  position: fixed;
  width: 100%;
  height: 100%;
  background: transparent;
  z-index: -1;
  top: 0;
  left: 0;
}
</style>

<div id="particles-js"></div>

<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
<script>
particlesJS('particles-js',
  {
    "particles": {
      "number": {"value": 60},
      "size": {"value": 3},
      "move": {"speed": 2},
      "line_linked": {"enable": true, "color": "#ffffff"},
      "color": {"value": "#00ffff"}
    },
    "interactivity": {
      "events": {
        "onhover": {"enable": true, "mode": "repulse"}
      }
    }
  });
</script>
""", unsafe_allow_html=True)

# ----------------------------------------------
# CUSTOM STYLES (GLOW EFFECTS INCLUDED)
# ----------------------------------------------
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: {bg_color};
    color: {text_color};
    transition: all 0.5s ease-in-out;
    font-family: 'Poppins', sans-serif;
}}

@keyframes glow {{
  0% {{ text-shadow: 0 0 5px #1fddff, 0 0 10px #1fddff, 0 0 20px #1fddff; }}
  50% {{ text-shadow: 0 0 15px #ff4b1f, 0 0 25px #ff4b1f, 0 0 40px #ff4b1f; }}
  100% {{ text-shadow: 0 0 5px #1fddff, 0 0 10px #1fddff, 0 0 20px #1fddff; }}
}}

.glow {{
    animation: glow 2s ease-in-out infinite alternate;
}}

.gradient-header {{
    background: {gradient};
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    color: white;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
    animation: float 3s ease-in-out infinite;
}}

@keyframes float {{
  0% {{ transform: translatey(0px); }}
  50% {{ transform: translatey(-10px); }}
  100% {{ transform: translatey(0px); }}
}}

div[data-testid="stExpander"] > div:first-child p {{
    font-weight: bold;
    font-size: 18px;
    color: {text_color};
    animation: glow 3s ease-in-out infinite;
}}

div[data-testid="stExpander"] {{
    background-color: {card_bg};
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    transition: 0.3s ease-in-out;
}}
div[data-testid="stExpander"]:hover {{
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(0,255,255,0.4);
}}

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
    animation: glow 2s ease-in-out infinite alternate;
}}
div.stButton > button:hover {{
    transform: scale(1.05);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.6);
}}

.result-box {{
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    border: 3px solid;
    border-image-slice: 1;
    border-image-source: linear-gradient(90deg, #1fddff, #ff4b1f);
    padding: 35px;
    text-align: center;
    margin-top: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
    animation: borderMove 4s linear infinite;
}}
@keyframes borderMove {{
  0% {{ border-image-source: linear-gradient(90deg, #1fddff, #ff4b1f); }}
  50% {{ border-image-source: linear-gradient(90deg, #ff4b1f, #1fddff); }}
  100% {{ border-image-source: linear-gradient(90deg, #1fddff, #ff4b1f); }}
}}

.result-title {{
    color: #ff6a00;
    font-size: 28px;
    font-weight: bold;
    animation: glow 2s infinite alternate;
}}
.result-value {{
    color: #1fddff;
    font-size: 52px;
    font-weight: bold;
    animation: glow 1.5s infinite alternate;
}}

.footer {{
    text-align:center;
    color:#bbb;
    margin-top:40px;
    font-size:16px;
    animation: glow 3s infinite alternate;
}}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------
# HEADER
# ----------------------------------------------
st.markdown("""
<div class="gradient-header">
    <h1 class="glow">🎥 YouTube Ad Revenue Predictor 💰</h1>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------------------------
# INPUT SECTION
# ----------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("🎯 Basic Video Info", expanded=True):
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
ad_revenue_per_view = 0

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
# PREDICTION + VISUAL METRICS
# ----------------------------------------------
if st.button("🚀 Predict Revenue", key="predict_button"):
    prediction = model.predict(input_data)[0]
    prediction = max(0, prediction)

    colA, colB, colC = st.columns(3)
    with colA:
        fig1 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=engagement_rate * 100,
            title={'text': "Engagement Rate (%)"},
            gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#00ccff"}}
        ))
        st.plotly_chart(fig1, use_container_width=True)
    with colB:
        fig2 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=views_per_subscriber,
            title={'text': "Views/Subscriber"},
            gauge={'axis': {'range': [0, 20]}, 'bar': {'color': "#ff9f43"}}
        ))
        st.plotly_chart(fig2, use_container_width=True)
    with colC:
        fig3 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prediction,
            title={'text': "Predicted Revenue ($)"},
            gauge={'axis': {'range': [0, prediction * 2]}, 'bar': {'color': "#1fddff"}}
        ))
        st.plotly_chart(fig3, use_container_width=True)

    st.markdown(f"""
        <div class="result-box">
            <div class="result-title">💵 Estimated Ad Revenue</div>
            <div class="result-value">${prediction:,.2f}</div>
            <p style="color:lightgray;">(Based on provided metrics)</p>
        </div>
    """, unsafe_allow_html=True)

    st.balloons()

# ----------------------------------------------
# SIDEBAR STATS
# ----------------------------------------------
st.sidebar.markdown(f"""
### 📊 Quick Stats
- 🔥 Engagement Rate: **{engagement_rate*100:.2f}%**
- 👥 Views/Sub: **{views_per_subscriber:.2f}**
- ⏱️ Watch/View: **{watch_time_per_view:.2f} min**
""")

# ----------------------------------------------
# FOOTER
# ----------------------------------------------
st.markdown("""
<div class="footer glow">
    Built with 🧠 using <b>Streamlit</b> | Designed by <b>Sudhakar M</b><br>
    <small>© 2025 YouTube Revenue Predictor</small>
</div>
""", unsafe_allow_html=True)
