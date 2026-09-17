# ------------------------------------------------
# IMPORTS
# ------------------------------------------------
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="Healeaf Dashboard",
    page_icon="🌿",
    layout="wide"
)

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/healeaf_dataset.csv")

df = load_data()

# ------------------------------------------------
# FIX NEGATIVE VALUES
# ------------------------------------------------
df["Mental_Health_Score"] = df["Mental_Health_Score"].clip(lower=0)

# ------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------
st.markdown("""
<style>

.stApp {
    background-color: #f6fbf7;
}

section[data-testid="stSidebar"] {
    background-color: #eef7ee;
    border-right: 1px solid #dce8dc;
}

h1, h2, h3 {
    color: #1b5e20;
    font-family: sans-serif;
}

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 700;
    color: #145a32;
    margin-top: 10px;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: #555;
    font-size: 20px;
    margin-bottom: 30px;
}

.metric-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    border: 1px solid #ecf0ec;
}

.metric-title {
    color: #555;
    font-size: 18px;
    margin-bottom: 10px;
}

.metric-value {
    color: #2e7d32;
    font-size: 40px;
    font-weight: bold;
}

.metric-sub {
    color: #888;
    font-size: 14px;
}

.login-box {
    background-color: #eaf5ea;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 20px;
}

.sidebar-note {
    background-color: #e8f5e9;
    padding: 15px;
    border-radius: 12px;
    color: #2e7d32;
    font-size: 15px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2917/2917995.png",
    width=70
)

st.sidebar.markdown(
    "<h1 style='color:#2e7d32;'>Healeaf</h1>",
    unsafe_allow_html=True
)

# ------------------------------------------------
# LOGIN
# ------------------------------------------------
st.sidebar.subheader("Login")

role = st.sidebar.selectbox(
    "Login As",
    ["Student", "Counselor", "Admin"]
)

st.sidebar.markdown("""
<div class='login-box'>
<b>Demo Credentials</b><br><br>
Username: <b>admin</b><br>
Password: <b>1234</b>
</div>
""", unsafe_allow_html=True)

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.sidebar.button("Login"):

    if username == "admin" and password == "1234":
        st.session_state.logged_in = True

    else:
        st.sidebar.error("Invalid Username or Password")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

if not st.session_state.logged_in:
    st.warning("Please login to access dashboard")
    st.stop()

# ------------------------------------------------
# NAVIGATION MENU
# ------------------------------------------------
page = st.sidebar.radio(
    "🌿 Navigation",
    [
        "🏠 Dashboard",
        "📊 Institution Analytics",
        "🤖 AI Assistant",
        "🌍 About Healeaf"
    ]
)

# ------------------------------------------------
# FILTER
# ------------------------------------------------
st.sidebar.markdown("---")

st.sidebar.subheader("Filter Students")

selected_gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + list(df["Gender"].unique())
)

if selected_gender != "All":
    df = df[df["Gender"] == selected_gender]

# ------------------------------------------------
# SIDEBAR PREMIUM FEATURES
# ------------------------------------------------
st.sidebar.markdown("""
<div class='sidebar-note'>

🌟 <b>Premium Features</b><br><br>

✔ AI Stress Prediction<br>
✔ Burnout Detection<br>
✔ Counselor Alerts<br>
✔ Institution Analytics<br>
✔ Wellness Intelligence<br>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# DASHBOARD PAGE
# ------------------------------------------------
if page == "🏠 Dashboard":

    # ------------------------------------------------
    # HEADER
    # ------------------------------------------------
    st.markdown("""
    <div class='main-title'>
    🌿 Healeaf Mental Wellness Dashboard 🌿
    </div>

    <div class='sub-title'>
    AI-Powered Student Wellness Analytics Platform<br>
    Analyze stress, mental wellness, academic pressure,
    and lifestyle patterns using data analytics and AI.
    </div>
    """, unsafe_allow_html=True)

    # ------------------------------------------------
    # STARTUP IMPACT METRICS
    # ------------------------------------------------
    st.markdown("## 🌟 Healeaf Impact")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("Students Monitored", "1,250")

    with m2:
        st.metric("High Risk Cases", "48")

    with m3:
        st.metric("Institutions", "6")

    with m4:
        st.metric("Wellness Improvement", "32%")

    # ------------------------------------------------
    # METRICS
    # ------------------------------------------------
    average_stress = round(df["Stress_Level"].mean(), 2)
    average_sleep = round(df["Sleep_Hours"].mean(), 2)
    average_score = round(df["Mental_Health_Score"].mean(), 2)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-title'>🧠 Average Stress</div>
            <div class='metric-value'>{average_stress}</div>
            <div class='metric-sub'>Out of 10</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-title'>😴 Average Sleep</div>
            <div class='metric-value'>{average_sleep}</div>
            <div class='metric-sub'>Hours</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-title'>😊 Mental Health Score</div>
            <div class='metric-value'>{average_score}</div>
            <div class='metric-sub'>Out of 100</div>
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------
    # DATASET PREVIEW
    # ------------------------------------------------
    st.subheader("📋 Dataset Preview")

    st.dataframe(df, use_container_width=True)

    # ------------------------------------------------
    # DOWNLOAD DATASET
    # ------------------------------------------------
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "📥 Download Dataset",
        csv,
        "healeaf_data.csv",
        "text/csv"
    )

    # ------------------------------------------------
    # CHARTS
    # ------------------------------------------------
    col4, col5 = st.columns([1, 1], gap="large")

    with col4:

        st.markdown("### 📊 Mood Distribution")

        fig1 = px.pie(
            df,
            names="Mood",
            hole=0.55,
            color_discrete_sequence=px.colors.sequential.Greens
        )

        st.plotly_chart(fig1, use_container_width=True)

    with col5:

        st.markdown("### 😴 Sleep vs Stress")

        df["Bubble_Size"] = abs(df["Mental_Health_Score"])

        fig2 = px.scatter(
            df,
            x="Sleep_Hours",
            y="Stress_Level",
            color="Gender",
            size="Bubble_Size",
            hover_data=["Mood"],
            size_max=30
        )

        st.plotly_chart(fig2, use_container_width=True)

    # ------------------------------------------------
    # SECOND ROW CHARTS
    # ------------------------------------------------
    col6, col7 = st.columns(2)

    with col6:

        st.subheader("📚 Academic Pressure")

        pressure = df["Academic_Pressure"].value_counts().reset_index()

        pressure.columns = ["Pressure", "Count"]

        fig3 = px.bar(
            pressure,
            x="Pressure",
            y="Count",
            color="Pressure"
        )

        st.plotly_chart(fig3, use_container_width=True)

    with col7:

        st.subheader("📱 Screen Time vs Stress")

        fig4 = px.scatter(
            df,
            x="Screen_Time",
            y="Stress_Level",
            color="Mood"
        )

        st.plotly_chart(fig4, use_container_width=True)

    # ------------------------------------------------
    # CORRELATION HEATMAP
    # ------------------------------------------------
    st.subheader("📈 Wellness Correlation Analysis")

    corr = df.corr(numeric_only=True)

    fig_corr = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig_corr, use_container_width=True)

    # ------------------------------------------------
    # RISK DETECTION
    # ------------------------------------------------
    st.subheader("🚨 Mental Health Risk Detection")

    def detect_risk(score):

        if score >= 70:
            return "Low Risk"

        elif score >= 40:
            return "Medium Risk"

        else:
            return "High Risk"

    df["Risk_Level"] = df["Mental_Health_Score"].apply(detect_risk)

    risk_fig = px.pie(
        df,
        names="Risk_Level",
        hole=0.4
    )

    st.plotly_chart(risk_fig, use_container_width=True)

    # ------------------------------------------------
    # MACHINE LEARNING MODEL
    # ------------------------------------------------
    st.subheader("🤖 AI Stress Prediction")

    X = df[
        [
            "Study_Hours",
            "Sleep_Hours",
            "Screen_Time",
            "Physical_Activity",
            "Social_Interaction"
        ]
    ]

    y = df["Stress_Level"]

    model = LinearRegression()

    model.fit(X, y)

    pred = model.predict(X)

    score = r2_score(y, pred)

    st.write("📊 Model Accuracy:", round(score, 2))

    col8, col9, col10 = st.columns(3)

    with col8:
        study_hours = st.slider("Study Hours", 1, 10, 5)
        sleep_hours = st.slider("Sleep Hours", 1, 10, 6)

    with col9:
        screen_time = st.slider("Screen Time", 1, 12, 5)
        physical_activity = st.slider("Physical Activity", 0, 5, 2)

    with col10:
        social_interaction = st.slider("Social Interaction", 0, 5, 2)

    if st.button("Predict Stress Level"):

        input_data = pd.DataFrame([{
            "Study_Hours": study_hours,
            "Sleep_Hours": sleep_hours,
            "Screen_Time": screen_time,
            "Physical_Activity": physical_activity,
            "Social_Interaction": social_interaction
        }])

        prediction = model.predict(input_data)

        predicted_stress = round(prediction[0], 2)

        st.success(f"Predicted Stress Level: {predicted_stress}")

        if predicted_stress >= 8:

            st.error("🔥 High Stress Risk")
            st.error("🚨 Counselor Alert Triggered")

        elif predicted_stress >= 5:

            st.warning("⚠️ Moderate Stress Risk")

        else:

            st.success("✅ Low Stress Risk")

        # ------------------------------------------------
        # RECOMMENDATIONS
        # ------------------------------------------------
        st.subheader("🌿 Personalized Wellness Recommendations")

        if predicted_stress >= 8:

            st.error("⚠️ High Stress Detected")

            st.write("• Increase sleep hours")
            st.write("• Reduce screen time")
            st.write("• Practice meditation")
            st.write("• Take regular study breaks")

        elif predicted_stress >= 5:

            st.warning("⚠️ Moderate Stress Detected")

            st.write("• Maintain healthy sleep schedule")
            st.write("• Increase physical activity")
            st.write("• Spend time socially")

        else:

            st.success("✅ Healthy Stress Level")

            st.write("Keep maintaining your healthy lifestyle!")

        # ------------------------------------------------
        # BURNOUT DETECTION
        # ------------------------------------------------
        st.subheader("🔥 Burnout Risk Detection")

        burnout_score = (
            study_hours * 2
            + predicted_stress
            + screen_time
            - sleep_hours
        )

        if burnout_score >= 20:

            st.error("🔥 High Burnout Risk")

        elif burnout_score >= 12:

            st.warning("⚠️ Moderate Burnout Risk")

        else:

            st.success("✅ Low Burnout Risk")

    # ------------------------------------------------
    # FOOTER
    # ------------------------------------------------
    st.markdown("""
    ---
    <div style='text-align:center; color:gray;'>

    🌿 <b>Healeaf</b> • AI-Powered Wellness Intelligence Platform <br>

    Empowering institutions through predictive mental wellness analytics.

    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------
# INSTITUTION ANALYTICS PAGE
# ------------------------------------------------
elif page == "📊 Institution Analytics":

    st.title("📊 Institution Analytics")

    st.metric("Students Monitored", "1,250")
    st.metric("High Risk Cases", "48")
    st.metric("Institutions", "6")

    department_data = pd.DataFrame({
        "Department": ["CSE", "ECE", "ME", "CE"],
        "Stress": [7.2, 6.5, 5.8, 6.9]
    })

    fig = px.bar(
        department_data,
        x="Department",
        y="Stress",
        color="Department"
    )

    st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------
# AI ASSISTANT PAGE
# ------------------------------------------------
elif page == "🤖 AI Assistant":

    st.title("🤖 Healeaf AI Assistant")

    user_question = st.text_input(
        "Ask wellness-related questions"
    )

    if user_question:

        st.success(
            "AI Recommendation: Maintain healthy sleep, reduce screen time, and stay socially active."
        )

# ------------------------------------------------
# ABOUT PAGE
# ------------------------------------------------
elif page == "🌍 About Healeaf":

    st.title("🌍 About Healeaf")

    st.markdown("""

    ## 🌿 What is Healeaf?

    Healeaf is an AI-powered student wellness platform
    designed to help institutions monitor mental health,
    detect burnout risks, and provide early intervention
    through predictive analytics and AI.

    ## 🚀 Our Mission

    To improve student wellbeing through technology,
    analytics, and intelligent wellness systems.

    ## 🎯 Features

    ✔ AI Stress Prediction  
    ✔ Burnout Detection  
    ✔ Counselor Alerts  
    ✔ Institution Analytics  
    ✔ Wellness Recommendations

    """)

