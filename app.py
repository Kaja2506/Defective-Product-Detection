import streamlit as st
import joblib
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Defective Product Prediction",
    page_icon="🏭",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#eef2ff,#dbeafe,#f8fafc);
}

/* Title */
.title{
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#1e3a8a;
    margin-top:10px;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:#475569;
    margin-bottom:30px;
}

/* Labels */
label{
    font-size:18px !important;
    font-weight:600 !important;
    color:#1e293b !important;
}

/* Number Input */
.stNumberInput input{
    border-radius:10px;
    border:2px solid #2563eb;
    font-size:17px;
}

/* Button */
.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    border:none;
    background:#2563eb;
    color:white;
    font-size:20px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1d4ed8;
}

/* Success */
.success-box{
    background:#dcfce7;
    color:#166534;
    padding:20px;
    border-radius:12px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

/* Error */
.error-box{
    background:#fee2e2;
    color:#991b1b;
    padding:20px;
    border-radius:12px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

/* Footer */
.footer{
    text-align:center;
    margin-top:40px;
    color:gray;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    '<div class="title">🏭 Defective Product Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Powered Manufacturing Quality Inspection</div>',
    unsafe_allow_html=True
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model.pkl")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📋 About")

st.sidebar.info("""
This application predicts whether a manufactured product is:

✅ Non Defective

❌ Defective

Enter all values and click **Predict Product Quality**.
""")

# ---------------- INPUTS ----------------
col1, col2 = st.columns(2)

with col1:

    temperature = st.number_input(
        "🌡️ Machine Temperature (°C)",
        min_value=0.0,
        value=80.0,
        help="Enter machine operating temperature"
    )

    pressure = st.number_input(
        "⚙️ Operating Pressure (Bar)",
        min_value=0.0,
        value=90.0,
        help="Enter operating pressure"
    )

    sensor1 = st.number_input(
        "📡 Sensor A Reading",
        value=100.0,
        help="Primary sensor reading"
    )

with col2:

    sensor2 = st.number_input(
        "📡 Sensor B Reading",
        value=1.0,
        help="Secondary sensor reading"
    )

    sensor3 = st.number_input(
        "📡 Sensor C Reading",
        value=0.5,
        help="Additional sensor reading"
    )

    operator = st.number_input(
        "👨‍🏭 Operator Experience (Years)",
        min_value=0.0,
        value=1.0,
        help="Years of operator experience"
    )

st.write("")

# ---------------- BUTTON ----------------
if st.button("🚀 Predict Product Quality"):

    x = np.array([[
        temperature,
        pressure,
        sensor1,
        sensor2,
        sensor3,
        operator
    ]])

    prediction = model.predict(x)

    st.markdown("## 📊 Prediction Result")

    if prediction[0] == 1:

        st.markdown("""
        <div class="error-box">
        ❌ DEFECTIVE PRODUCT
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="success-box">
        ✅ NON DEFECTIVE PRODUCT
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
Developed using ❤️ Python • Streamlit • Machine Learning
</div>
""", unsafe_allow_html=True)