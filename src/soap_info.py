# soap_info.py
# This script will handle all functions related to SOAP notes input by the doctor and storage
#
#=======================================================================================

import streamlit as st
from utils.data_handler import save_soap_info

def soap_notes_page():
    st.title("SOAP Notes")
    patient_id = st.text_input("Patient ID")
    visit_date = st.date_input("Visit Date")

    # Subjective
    st.header("Subjective")

    chief_complaint = st.text_area("Chief Complaint", help="Patient's main reason for visit")

    pain_location = st.multiselect("Pain Location",
                                   ["Neck", "Upper Back", "Middle Back", "Lower Back", "Shoulders", "Hips", "Knees",
                                    "Ankles", "Wrists", "Elbows"])

    pain_characteristics = st.multiselect("Pain Characteristics",
                                          ["Sharp", "Dull", "Aching", "Burning", "Tingling", "Numbness", "Throbbing",
                                           "Shooting", "Stabbing"])

    pain_level = st.slider("Pain Level (0-10)", 0, 10, 5)

    pain_frequency = st.select_slider("Pain Frequency",
                                      options=["Constant", "Nearly Constant", "Intermittent", "Occasional", "Rare"])

    aggravating_factors = st.multiselect("Aggravating Factors",
                                         ["Sitting", "Standing", "Walking", "Lifting", "Bending", "Twisting",
                                          "Lying down", "Stress", "Weather changes"])

    relieving_factors = st.multiselect("Relieving Factors",
                                       ["Rest", "Ice", "Heat", "Stretching", "Exercise", "Medication", "Massage"])

    affected_activities = st.multiselect("Affected Daily Activities",
                                         ["Work", "Sleep", "Exercise", "Household Chores", "Social Activities",
                                          "Driving", "Personal Care"])

    associated_symptoms = st.multiselect("Associated Symptoms",
                                         ["Headache", "Dizziness", "Nausea", "Weakness", "Fatigue", "Stiffness",
                                          "Muscle spasms"])

    # Objective
    st.header("Objective")

    vital_signs = st.checkbox("Record Vital Signs")
    if vital_signs:
        col1, col2, col3 = st.columns(3)
        with col1:
            blood_pressure = st.text_input("Blood Pressure (mmHg)")
            heart_rate = st.number_input("Heart Rate (bpm)", min_value=0, max_value=200)
        with col2:
            respiratory_rate = st.number_input("Respiratory Rate (breaths/min)", min_value=0, max_value=60)
            temperature = st.number_input("Temperature (°C)", min_value=35.0, max_value=42.0, step=0.1)
        with col3:
            height_ft = st.number_input("Height (ft)", min_value=0, step=1)
            height_in = st.number_input("Height (in)", min_value=0, step=1)
            weight_lbs = st.number_input("Weight (lbs)", min_value=0, step=1)

    st.subheader("Range of Motion (ROM)")
    body_parts = ["Cervical_Spine", "Thoracic_Spine", "Lumbar_Spine", "Shoulders", "Hips"]
    for part in body_parts:
        col1, col2 = st.columns(2)
        with col1:
            st.number_input(f"{part} Flexion (degrees)", 0, 180, 90, key=f"{part.lower()}_flexion")
        with col2:
            st.number_input(f"{part} Extension (degrees)", 0, 180, 90, key=f"{part.lower()}_extension")

    st.subheader("Orthopedic Tests")
    tests = ["Straight_Leg_Raise", "Kernig_Sign", "Brudzinski_Sign", "Spurling_Test", "Valsalva_Maneuver"]
    for test in tests:
        st.selectbox(f"{test}", ["Positive", "Negative", "Not Performed"], key=f"ortho_{test.lower()}")

    st.subheader("Neurological Examination")
    neuro_tests = ["Deep_Tendon_Reflexes", "Muscle_Strength", "Sensation"]
    for test in neuro_tests:
        st.text_area(f"{test} Results", key=f"neuro_{test.lower()}")

    st.subheader("Palpation Findings")
    palpation = st.text_area("Palpation Findings")

    # Assessment
    st.header("Assessment")

    diagnosis = st.text_area("Diagnosis")

    differential_diagnosis = st.text_area("Differential Diagnosis")

    prognosis = st.select_slider("Prognosis",
                                 options=["Poor", "Fair", "Good", "Very Good", "Excellent"])

    # Plan
    st.header("Plan")

    treatment_provided = st.multiselect("Treatment Provided",
                                        ["Spinal Manipulation", "Soft Tissue Therapy", "Electrical Stimulation",
                                         "Ultrasound", "Exercise Prescription", "Hot/Cold Therapy"])

    treatment_frequency = st.selectbox("Recommended Treatment Frequency",
                                       ["1x per week", "2x per week", "3x per week", "As needed"])

    treatment_duration = st.selectbox("Recommended Treatment Duration",
                                      ["2 weeks", "4 weeks", "6 weeks", "8 weeks", "12 weeks", "Ongoing"])

    home_care_instructions = st.text_area("Home Care Instructions")

    follow_up = st.date_input("Follow-up Appointment")

    referrals = st.multiselect("Referrals",
                               ["None", "X-ray", "MRI", "CT Scan", "Blood Work", "Specialist Consultation"])

    if st.button("Save SOAP Notes"):
        save_soap_info(patient_id, visit_date, 
            chief_complaint, pain_location, pain_characteristics, pain_level,  # Subjective
            pain_frequency, aggravating_factors, relieving_factors, affected_activities,
            associated_symptoms,
            vital_signs, blood_pressure, heart_rate, respiratory_rate,  # Objective
            temperature, height_ft, height_in, weight_lbs,
            st.session_state.cervical_spine_flexion, st.session_state.cervical_spine_extension,  # Range of Motion Stats
            st.session_state.thoracic_spine_flexion, st.session_state.thoracic_spine_extension,
            st.session_state.lumbar_spine_flexion, st.session_state.lumbar_spine_extension,
            st.session_state.shoulders_flexion, st.session_state.shoulders_extension,
            st.session_state.hips_flexion, st.session_state.hips_extension,
            st.session_state.ortho_straight_leg_raise, st.session_state.ortho_kernig_sign, st.session_state.ortho_brudzinski_sign,  # Orthopedic Tests
            st.session_state.ortho_spurling_test, st.session_state.ortho_valsalva_maneuver,
            st.session_state.neuro_deep_tendon_reflexes, st.session_state.neuro_muscle_strength, st.session_state.neuro_sensation,  # Neurological Examination
            palpation,  # Palpation Findings
            diagnosis, differential_diagnosis, prognosis,  # Assessment
            treatment_provided, treatment_frequency, treatment_duration,  # Plan
            home_care_instructions, follow_up, referrals  # These were missing
        )
        st.success("SOAP notes saved successfully!")

