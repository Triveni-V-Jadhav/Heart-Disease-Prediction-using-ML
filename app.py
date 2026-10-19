import streamlit as st
import joblib
import pandas as pd
import base64
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

# ================= LOAD MODEL =================
model = joblib.load("model.pkl")

# ================= BACKGROUND =================
def set_bg():
    with open("bg.jpg", "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
        url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """, unsafe_allow_html=True)

set_bg()

# ================= UI STYLE =================
st.markdown("""
<style>
.title {
    text-align: center;
    color: #ff4b4b;
    font-size: 40px;
    font-weight: bold;
}
.box {
    background-color: white;
    color: black;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}
.section-title {
    color: black;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
}
label {
    color: black !important;
    font-weight: bold;
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    height: 50px;
    width: 100%;
}
.stProgress > div > div > div {
    background-color: #ff4b4b;
}
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown('<div class="title">❤️ Heart Disease Prediction</div>', unsafe_allow_html=True)

# ================= INPUTS =================
st.markdown('<div class="box">', unsafe_allow_html=True)
st.markdown('<div class="section-title">👤 Basic Information</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", 1, 100)
with col2:
    sex = st.selectbox("Gender", ["Male", "Female"])
    sex_val = 1 if sex == "Male" else 0
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="box">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🩺 Health Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    trestbps = st.number_input("Blood Pressure", 80, 200)
with col2:
    chol = st.number_input("Cholesterol", 100, 600)

fbs = st.selectbox("High Blood Sugar?", ["Yes", "No"])
fbs_val = 1 if fbs == "Yes" else 0
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="box">', unsafe_allow_html=True)
st.markdown('<div class="section-title">💓 Heart Condition</div>', unsafe_allow_html=True)

cp_option = st.selectbox("Chest Pain Type", ["No Pain", "Mild", "Moderate", "Severe"])
cp = ["No Pain", "Mild", "Moderate", "Severe"].index(cp_option)

restecg = ["Normal", "Abnormal", "Severe"].index(
    st.selectbox("ECG Result", ["Normal", "Abnormal", "Severe"])
)

thalach = st.number_input("Max Heart Rate", 60, 200)

exang = st.selectbox("Chest Pain During Exercise", ["Yes", "No"])
exang_val = 1 if exang == "Yes" else 0
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="box">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📊 Advanced Parameters</div>', unsafe_allow_html=True)

oldpeak_option = st.selectbox("Stress Level", ["Low", "Medium", "High"])
oldpeak = {"Low": 0.5, "Medium": 1.5, "High": 3.0}[oldpeak_option]

slope = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}[
    st.selectbox("Heart Graph Type", ["Upsloping", "Flat", "Downsloping"])
]

ca = st.selectbox("Blocked Blood Vessels", [0, 1, 2, 3])

thal = {"Normal": 1, "Fixed Defect": 2, "Reversible Defect": 3}[
    st.selectbox("Blood Flow Condition",
                 ["Normal", "Fixed Defect", "Reversible Defect"])
]

st.markdown('</div>', unsafe_allow_html=True)

# ================= PREDICT =================
if st.button("🔍 Predict"):

    input_data = pd.DataFrame([[age, sex_val, cp, trestbps, chol, fbs_val,
                                restecg, thalach, exang_val, oldpeak,
                                slope, ca, thal]],
                              columns=['age','sex','cp','trestbps','chol','fbs',
                                       'restecg','thalach','exang','oldpeak',
                                       'slope','ca','thal'])

    probability = model.predict_proba(input_data)[0][1] * 100

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🩺 Prediction Result</div>', unsafe_allow_html=True)

    if probability > 60:
        st.error(f"🔴 High Risk ({probability:.2f}%)")
        risk = "High Risk"
    elif probability > 30:
        st.warning(f"🟡 Medium Risk ({probability:.2f}%)")
        risk = "Medium Risk"
    else:
        st.success(f"🟢 Low Risk ({probability:.2f}%)")
        risk = "Low Risk"

    st.write(f"📊 Probability: {probability:.2f}%")
    st.subheader("📈 Risk Level")
    st.progress(int(probability))
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= CHART =================
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("📊 Risk Analysis")

    fig, ax = plt.subplots()
    ax.pie([100 - probability, probability],
           labels=["Low Risk", "High Risk"],
           autopct='%1.1f%%')

    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= PDF =================
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Heart Disease Prediction Report", ln=True, align='C')

    pdf.ln(10)

    # Patient
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 8, "Patient Details:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 8, f"Age: {age}", ln=True)
    pdf.cell(200, 8, f"Gender: {sex}", ln=True)

    pdf.ln(5)

    # Health
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 8, "Health Parameters:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 8, f"Blood Pressure: {trestbps}", ln=True)
    pdf.cell(200, 8, f"Cholesterol: {chol}", ln=True)
    pdf.cell(200, 8, f"Blood Sugar: {fbs}", ln=True)
    pdf.cell(200, 8, f"Chest Pain Type: {cp_option}", ln=True)
    pdf.cell(200, 8, f"Max Heart Rate: {thalach}", ln=True)
    pdf.cell(200, 8, f"Stress Level: {oldpeak_option}", ln=True)

    pdf.ln(5)

    # Result
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 8, "Prediction Result:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 8, f"Risk Level: {risk}", ln=True)
    pdf.cell(200, 8, f"Probability: {probability:.2f}%", ln=True)

    pdf.ln(5)

    # Suggestions
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 8, "Health Suggestions:", ln=True)
    pdf.set_font("Arial", size=12)

    if trestbps > 140:
        pdf.cell(200, 8, "- Control blood pressure", ln=True)
    if chol > 240:
        pdf.cell(200, 8, "- Reduce cholesterol intake", ln=True)
    if exang_val == 1:
        pdf.cell(200, 8, "- Avoid heavy exercise", ln=True)
    if oldpeak > 2:
        pdf.cell(200, 8, "- Manage stress", ln=True)

    if probability < 30:
        pdf.cell(200, 8, "- Maintain healthy lifestyle", ln=True)
    else:
        pdf.cell(200, 8, "- Consult a doctor", ln=True)

    pdf.ln(10)

    # Footer
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(200, 8, "Note: This is a machine learning-based prediction.", ln=True)
    pdf.cell(200, 8, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.output("report.pdf")

    with open("report.pdf", "rb") as f:
        st.download_button("📄 Download Report", f, "Heart_Report.pdf")