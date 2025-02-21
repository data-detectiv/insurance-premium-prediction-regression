import streamlit as st
from prediction_helper import predict
def main():
    st.title("Health Insurance Cost Predictor",)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, step=1)
        genetical_risk = st.number_input("Genetical Risk", min_value=0, step=1)
        employment_status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'])
        insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])
    
    with col2:
        num_dependants = st.number_input("Number of Dependants", min_value=0, step=1)
        gender = st.selectbox("Gender", ['Male', 'Female'])
        region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
        medical_history = st.selectbox("Medical History", ['Diabetes', 'High blood pressure', 'No Disease',
                                                            'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
                                                            'High blood pressure & Heart disease', 'Diabetes & Thyroid',
                                                            'Diabetes & Heart disease'])
    
    with col3:
        income = st.number_input("Income in Lakhs", min_value=0, step=1)
        marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])
        bmi_category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])
        smoking_status = st.selectbox("Smoking Status", ['No Smoking', 'Regular', 'Occasional'])
    
    input_dict = {
        'Age': age,
        'Number of Dependants': num_dependants,
        'Income in Lakhs': income,
        'Genetical Risk': genetical_risk,
        'Gender': gender,
        'Marital Status': marital_status,
        'Employment Status': employment_status,
        'Region': region,
        'BMI Category': bmi_category,
        'Insurance Plan': insurance_plan,
        'Medical History': medical_history,
        'Smoking Status': smoking_status
    }
        
    if st.button("Predict"):
        prediction = predict(input_dict)
        st.success(f"Predicted Premium: {prediction}")

if __name__ == "__main__":
    main()
    
