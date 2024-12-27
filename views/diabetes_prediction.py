import streamlit as st
import joblib
import numpy as np

def predict_diabetes(gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c, blood_glucose_level):
    data = np.array([[gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c, blood_glucose_level]])
    model = joblib.load("./models/new_model.pkl")
    prediction = model.predict(data)
    return prediction

st.title("Diabetes Predictor")
with st.form("diabetes_prediction_form", clear_on_submit=True):
    gender = st.selectbox("Gender", ("Male", "Female"), index=None)
    age = st.number_input("Age", min_value=0, max_value=120)
    hype_value = st.selectbox("Hypertension", ("Yes", "No"), index=None)
    if (hype_value == "Yes"):
        hypertension = 1
    else:
        hypertension = 0
    heart_value = st.selectbox("Heart Disease", ("Yes", "No"), index=None)
    if (heart_value == "Yes"):
        heart_disease = 1
    else:
        heart_disease = 0
    smoking_history = st.selectbox("Smoking History", ("ever","not current", "former", "current", "never", "No Info"), index=None)
    bmi = st.number_input("BMI", min_value=0, max_value=100)
    hba1c = st.number_input("HbA1c", min_value=0, max_value=20)
    blood_glucose_level = st.number_input("Blood Glucose Level", min_value=0, max_value=500)
    submit_button = st.form_submit_button("Predict Diabetes")

    if submit_button:
        prediction = predict_diabetes(gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c, blood_glucose_level)
        if prediction[0] == 1:
            st.write("The model predicts that you have diabetes.")
        else:
            st.write("The model predicts that you don't have diabetes.")

st.divider()
st.subheader("About the Project")
st.write(
    """
    This project is a simple diabetes predictor that uses a machine learning model to predict whether a person has diabetes or not. 
    """)
st.write("""
        - I have used the diabetes prediction dataset (https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) from Kaggle for training the model.
        - First I did some exploratory data analysis on the dataset to understand the data.
        - Then I trained some machine learning models on the dataset and selected the best model which is Random Forest Classifier.
        - Here is the github link for the notebook:  
         """)