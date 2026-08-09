import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("best_ridge_model.pkl")


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Score Predictor",
    page_icon="🎓",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------
st.title("🎓 Student Score Prediction System")
st.write("Enter student details to predict the final score.")


# -----------------------------
# Input Fields
# -----------------------------

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

attendance_pct = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

study_hours_per_day = st.number_input(
    "Study Hours Per Day",
    min_value=0.0,
    max_value=24.0,
    value=3.0
)

previous_score = st.number_input(
    "Previous Score",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

assignment_avg = st.number_input(
    "Assignment Average",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

internal_marks = st.number_input(
    "Internal Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

classes_missed = st.number_input(
    "Classes Missed",
    min_value=0,
    value=5
)

extracurricular_level = st.selectbox(
    "Extracurricular Level",
    ["Low", "Medium", "High"]
)

internet_access = st.selectbox(
    "Internet Access",
    ["Yes", "No"]
)

parent_education = st.selectbox(
    "Parent Education",
    [
        "High School",
        "Graduate",
        "Postgraduate"
    ]
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("🔮 Predict Score"):

    input_data = pd.DataFrame([{
        "gender": gender,
        "attendance_pct": attendance_pct,
        "study_hours_per_day": study_hours_per_day,
        "previous_score": previous_score,
        "assignment_avg": assignment_avg,
        "internal_marks": internal_marks,
        "sleep_hours": sleep_hours,
        "classes_missed": classes_missed,
        "extracurricular_level": extracurricular_level,
        "internet_access": internet_access,
        "parent_education": parent_education
    }])

    # Prediction
    prediction = model.predict(input_data)

    predicted_score = prediction[0]

    st.success(
        f"🎯 Predicted Final Score: **{predicted_score:.2f}**"
    )