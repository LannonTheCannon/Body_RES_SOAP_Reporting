# patient_info.py
# This script will handle all functions related to patient information input and storage
#
#=======================================================================================

import streamlit as st
from utils.data_handler import save_patient_info

def patient_info_page():
    st.title("Patient Information")

    col1, col2 = st.columns(2)
    with col1:
        patient_name = st.text_input("Patient Name")
        patient_id = st.text_input("Patient ID")
        dob = st.date_input("Date of Birth")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        contact_number = st.text_input("Contact Number")
        email = st.text_input("Email Address")

    with col2:
        visit_date = st.date_input("Visit Date")
        visit_time = st.time_input("Visit Time")
        occupation = st.text_input("Occupation")
        height_ft = st.number_input('Height (feet)', min_value=0.0, step=1.0)
        height_in = st.number_input('Height (inches)', min_value=0.0, step=1.0)
        weight_lbs = st.number_input("Weight (lbs)", min_value=0.0, step=1.0)

    st.subheader("Emergency Contact")
    emergency_name = st.text_input("Emergency Contact Name")
    emergency_relation = st.text_input("Relationship to Patient")
    emergency_number = st.text_input("Emergency Contact Number")

    st.subheader("Medical History")
    medical_history = st.text_area("Any relevant medical history or conditions")
    current_medications = st.text_area("Current Medications")
    allergies = st.text_area("Known Allergies")

    st.subheader("Lifestyle Factors")
    exercise_frequency = st.selectbox("Exercise Frequency",
                                      ["None", "1-2 times/week", "3-4 times/week", "5+ times/week"])
    exercise_types = st.multiselect("Types of Exercise",
                                    ["Walking", "Running", "Swimming", "Weightlifting", "Yoga", "Other"])
    sleep_hours = st.slider("Average Hours of Sleep per Night", 0, 12, 7)
    stress_level = st.slider("Stress Level (0-10)", 0, 10, 5)

    st.subheader("Previous Chiropractic Care")
    previous_chiro = st.radio("Have you received chiropractic care before?", ["Yes", "No"])
    if previous_chiro == "Yes":
        previous_chiro_details = st.text_area("Please provide details of previous chiropractic care")

    st.subheader("Current Complaint")
    primary_complaint = st.text_area("Primary reason for visit")
    pain_onset = st.date_input("When did the pain/discomfort start?")
    pain_cause = st.text_input("What caused the pain/discomfort? (if known)")
    
    # Pain Characteristics and Frequency 

    st.subheader("Pain Characteristics")

    st.markdown("""
    <style>
        .stSelectbox {
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        pain_intensity_sharp = st.slider("Sharp Pain Intensity (0-10)", 0, 10, 1, key='slider_sharpness')
        pain_intensity_shooting = st.slider("Shooting Pain Intensity (0-10)", 0, 10, 1, key='slider_shooting')
        pain_intensity_aching = st.slider("Aching Pain Intensity (0-10)", 0, 10, 1, key='slider_aching')
        pain_intensity_burning = st.slider("Burning Pain Intensity (0-10)", 0, 10, 1, key='slider_burning')
        pain_intensity_tingling = st.slider("Tingling Pain Intensity (0-10)", 0, 10, 1, key='slider_tingling')
        pain_intensity_numbness = st.slider("Numbness Pain Intensity (0-10)", 0, 10, 1, key='slider_numbness')

    with col2:
        pain_freq_sharp = st.selectbox("Sharpness Frequency", ['Constant', 'Intermittent', 'Occasional'], key='select_sharp')
        pain_freq_shooting = st.selectbox("Sharpness Frequency", ['Constant', 'Intermittent', 'Occasional'], key='select_shooting')
        pain_freq_aching = st.selectbox("Sharpness Frequency", ['Constant', 'Intermittent', 'Occasional'], key='select_aching')
        pain_freq_burning = st.selectbox("Sharpness Frequency", ['Constant', 'Intermittent', 'Occasional'], key='select_burning')
        pain_freq_tingling = st.selectbox("Sharpness Frequency", ['Constant', 'Intermittent', 'Occasional'], key='select_tingling')
        pain_freq_numbness = st.selectbox("Sharpness Frequency", ['Constant', 'Intermittent', 'Occasional'], key='select_numbness')

    st.subheader("Consent and Agreements")
    consent = st.checkbox("I consent to chiropractic examination and treatment")
    privacy_agreement = st.checkbox("I have read and agree to the privacy policy")

    if st.button("Save Patient Information"):
        if consent and privacy_agreement:
            save_patient_info(patient_name, patient_id, dob, gender, # First Time Patient Inforation 
                              contact_number, email, visit_date, visit_time,
                              occupation, height_ft, height_in, weight_lbs,
                              emergency_name, emergency_relation, emergency_number, # Emergency contact information
                              medical_history, current_medications, allergies, # Medical History
                              exercise_frequency, exercise_types, sleep_hours, stress_level, # Lifestyle Factors
                              previous_chiro, # Previous Chiropractic Care
                              primary_complaint, pain_onset, pain_cause, # Current Complaint
                              pain_intensity_sharp, pain_intensity_shooting, pain_intensity_aching, # Pain Characteristics
                              pain_intensity_burning, pain_intensity_tingling, pain_intensity_numbness,
                              pain_freq_sharp, pain_freq_shooting, pain_freq_aching,
                              pain_freq_burning, pain_freq_tingling, pain_freq_numbness,
                              consent, privacy_agreement) # Consent and Agreements
            st.success("Patient information saved successfully!")
            
        else:
            st.error("Please provide consent and agree to the privacy policy before saving.") 
