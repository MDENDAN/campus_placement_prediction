import streamlit as st
import pandas as pd
from model import load_model, predict
import time

# Load your trained model (make sure the model file 'svm_model_OPT.pkl' is in the same directory)
# status_model_filename = 'model\status\svm_model_OPT.pkl'
status_model = load_model('model/status/DT_model.joblib')

# salary_model_filename = 'model/salary/random_forest_regression_model.joblib'
salary_model = load_model('model/salary/random_forest_regression_model.joblib')

# Create a Streamlit web app
st.title('Campus Recruitment Prediction')
st.write('This app predicts campus recruitment status and salary based on selected features.')
st.markdown("""
<style>
.big-font {
    font-size:33px !important;
    font-weight: bold;
}

.medium{
    font-size:28px !important;
    font-weight: bold;    
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">Enter your name</p>', unsafe_allow_html=True)
name = st.text_input("")
# Define input fields for user input
user_input_container = st.container()

with user_input_container:
    st.markdown('<p class="medium">Please Enter correct details</p>',unsafe_allow_html=True)

    # Gender
    gender = st.selectbox('Select Gender', ['Male', 'Female'])

    # Group SSC Details
    st.subheader('SSC Details')
    col1, col2 = st.columns(2)
    with col1:
        ssc_p = st.number_input('Enter Percentage', min_value=0.0, max_value=100.0, key='ssc_p')
    with col2:
        ssc_b = st.selectbox('Select Board', ['Central', 'Others'], key='ssc_b')

    # Group HSC Details
    st.subheader('HSC Details')
    col1, col2, col_3 = st.columns(3)
    with col1:
        hsc_p = st.number_input('Enter Percentage', min_value=0.0, max_value=100.0, key='hsc_p')
    with col2:
        hsc_b = st.selectbox('Select Board', ['Central', 'Others'], key='hsc_b')
    with col_3:
        hsc_s = st.selectbox('Select HSC Stream', ['Science', 'Commerce', 'Arts'])

    # Group Degree Details
    st.subheader('Degree Details')
    col1, col2 = st.columns(2)
    with col1:
        degree_p = st.number_input('Enter Percentage', min_value=0.0, max_value=100.0, key='degree_p')
    with col2:
        degree_t = st.selectbox('Select Type', ['Comm&Mgmt', 'Sci&Tech', 'Others'], key='degree_t')

        # Work Experience
    workex = st.selectbox('Work Experience', ['Yes', 'No'])

    # E-test Percentage
    etest_p = st.number_input('Enter E-test Percentage', min_value=0.0, max_value=100.0)

    # Specialization
    specialisation = st.selectbox('Select Specialization', ['Mkt&HR', 'Mkt&Fin'])

    # MBA Percentage
    mba_p = st.number_input('Enter MBA Percentage', min_value=0.0, max_value=100.0)

if degree_t == 'Others':
    degree_t = 'Others1'

# Create a dictionary with user inputs
user_input = {
    'gender': gender,
    'ssc_p': ssc_p,
    'ssc_b': ssc_b,
    'hsc_p': hsc_p,
    'hsc_b': hsc_b,
    'hsc_s': hsc_s,
    'degree_t':degree_t,
    'workex': workex,
    'etest_p': etest_p,
    'specialisation': specialisation,
    'mba_p': mba_p,
    'degree_p': degree_p,

}

# Define a function to preprocess user input
def preprocess_user_input(input_data):
    # Create a dictionary to map user input to label-encoded values for categorical features
    label_encoding_mapping = {
        'Male': 0,
        'Female': 1,
        'Central': 0,
        'Others': 1,
        'Science': 0,
        'Commerce': 1,
        'Arts': 2,
        'Yes': 1,
        'No': 0,
        'Mkt&HR': 0,
        'Mkt&Fin': 1,
        'Comm&Mgmt':0,
        'Sci&Tech':1, 
        'Others1':2
    }

    # Label encode categorical features
    for feature in ['gender', 'ssc_b', 'hsc_b', 'hsc_s', 'degree_t','workex', 'specialisation']:
        input_data[feature] = label_encoding_mapping.get(input_data[feature])

    return input_data

# Create a button to make predictions
if st.button("Make Prediction"):
    # Preprocess user input
    preprocessed_input = preprocess_user_input(user_input)

    # Extract the values from the dictionary
    input_values = list(preprocessed_input.values())

    # Call the make_prediction function with the input values
    recruitment_status = predict(status_model, [input_values])
    if recruitment_status==1:
        # Calculate salary only if status is "Placed"
        salary_prediction = predict(salary_model,[input_values])
        rounded_salary = round(salary_prediction / 1000) * 1000
        lower_range = rounded_salary - 1000
        upper_range = rounded_salary + 1000
        st.balloons()
        succes = st.success(f"🎉Congratulations! {name} has high chances of getting PLACED! 🎉")
        time.sleep(3)
        succes.empty()
        # Display the prediction
        st.write("Result Predicted: SUCCESSFULL")

        st.write(f"Salary Prediction: {lower_range} to {upper_range}")
    else:
        st.write("Result Predicted: NOT SUCCESSFULL")
        st.write("😔 Sorry, you are not placed.")
else:
    # Display a neutral message when the button is not clicked
    st.write("Click the 'Make Prediction' button to check your placement status.")
