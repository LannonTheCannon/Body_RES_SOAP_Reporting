# treatment_plan_info.py
# This script will handle all functions related to Treatment plan notes input
# by the doctor as well as storage call to save treatment plan.
#
#=======================================================================================

import streamlit as st
from utils.data_handler import save_treatment_plan_info

def treatment_plan_page():
    st.title("Treatment Plan")

    # Patient Information
    patient_name = st.text_input("Patient Name")
    patient_id = st.text_input("Patient ID")
    diagnosis = st.text_area("Primary Diagnosis")

    # Treatment Duration
    st.subheader("Treatment Duration")
    plan_start_date = st.date_input("Plan Start Date")
    plan_duration = st.selectbox("Estimated Treatment Duration",
                                 ["2 weeks", "4 weeks", "6 weeks", "2 months", "3 months", "6 months", "Ongoing"])

    # Visit Frequency
    st.subheader("Visit Frequency")
    initial_phase = st.selectbox("Initial Phase Frequency",
                                 ["Daily", "3x per week", "2x per week", "1x per week"])
    maintenance_phase = st.selectbox("Maintenance Phase Frequency",
                                     ["1x per week", "1x per 2 weeks", "1x per month", "As needed"])

    # Treatment Modalities
    st.subheader("Recommended Treatments")
    treatment_modalities = st.multiselect("Select Treatment Modalities",
                                          ["Spinal Manipulation", "Extremity Manipulation", "Soft Tissue Therapy",
                                           "Electrical Stimulation", "Ultrasound", "Low-Level Laser Therapy",
                                           "Mechanical Traction", "Therapeutic Exercises", "Kinesio Taping",
                                           "Acupuncture", "Dry Needling", "Nutritional Counseling"])

    # Specific Techniques
    st.subheader("Specific Chiropractic Techniques")
    chiro_techniques = st.multiselect("Select Specific Techniques",
                                      ["Diversified Technique", "Gonstead Technique", "Activator Method",
                                       "Thompson Technique", "Flexion-Distraction", "Sacro-Occipital Technique (SOT)",
                                       "Applied Kinesiology", "Chiropractic Biophysics (CBP)"])

    # Treatment Areas
    st.subheader("Treatment Areas")
    treatment_areas = st.multiselect("Select Areas to be Treated",
                                     ["Cervical Spine", "Thoracic Spine", "Lumbar Spine", "Sacroiliac Joints",
                                      "Shoulders", "Elbows", "Wrists", "Hips", "Knees", "Ankles"])

    # Therapeutic Exercises
    st.subheader("Therapeutic Exercises")
    exercises = st.multiselect("Recommended Exercises",
                               ["Stretching", "Strengthening", "Range of Motion", "Balance Training",
                                "Core Stability", "Posture Correction", "Ergonomic Training"])

    exercise_frequency = st.selectbox("Exercise Frequency",
                                      ["Daily", "Every other day", "3x per week", "2x per week"])

    # Home Care Instructions
    st.subheader("Home Care Instructions")
    home_care = st.text_area("Provide detailed home care instructions for the patient")

    # Treatment Goals
    st.subheader("Treatment Goals")
    short_term_goals = st.text_area("Short-term Goals (2-4 weeks)")
    long_term_goals = st.text_area("Long-term Goals (1-6 months)")

    # Outcome Measures
    st.subheader("Outcome Measures")
    outcome_measures = st.multiselect("Select Outcome Measures to Track Progress",
                                      ["Pain Scale (VAS)", "Oswestry Disability Index (ODI)",
                                       "Neck Disability Index (NDI)",
                                       "Roland-Morris Disability Questionnaire",
                                       "Patient-Specific Functional Scale (PSFS)",
                                       "Range of Motion Measurements", "Muscle Strength Testing"])

    # Precautions and Contraindications
    st.subheader("Precautions and Contraindications")
    precautions = st.text_area("Note any precautions or contraindications for this patient")

    # Lifestyle Modifications
    st.subheader("Lifestyle Modifications")
    lifestyle_changes = st.multiselect("Recommended Lifestyle Changes",
                                       ["Ergonomic Adjustments", "Diet Modifications", "Stress Management",
                                        "Sleep Hygiene", "Increase Physical Activity", "Smoking Cessation"])

    # Referrals and Co-management
    st.subheader("Referrals and Co-management")
    referrals = st.multiselect("Referrals to Other Healthcare Providers",
                               ["None", "Physical Therapist", "Massage Therapist", "Pain Management Specialist",
                                "Orthopedic Surgeon", "Neurologist", "Rheumatologist", "Nutritionist"])

    # Re-evaluation Schedule
    st.subheader("Re-evaluation Schedule")
    reevaluation_frequency = st.selectbox("Re-evaluation Frequency",
                                          ["Every 4 weeks", "Every 6 weeks", "Every 8 weeks", "Every 12 weeks"])

    # Informed Consent
    st.subheader("Informed Consent")
    informed_consent = st.checkbox(
        "Patient has been informed about the treatment plan, potential risks, and expected benefits")

    # Save and Generate Report
    if st.button("Save and Generate Treatment Plan"):
        if informed_consent:
            save_treatment_plan_info(patient_name, patient_id, diagnosis, #Patient Information
                                     plan_start_date, plan_duration, #Treatment Duration
                                     initial_phase, maintenance_phase, # Visit Frequency
                                     treatment_modalities, # Treatment Modalities
                                     chiro_techniques, # Specific Techniques
                                     treatment_areas, # Treatment Areas
                                     exercises, exercise_frequency, # Therapeutic Exercises
                                     home_care, # Home Care Instructions
                                     short_term_goals, long_term_goals, # Treatment Goals
                                     outcome_measures, # Outcome Measures
                                     precautions, # Precautions and Contraindictions
                                     lifestyle_changes, #Lifestyle Modifications
                                     referrals, # Referrals and Co-management
                                     reevaluation_frequency, # Re-evaluation Schedule
                                     informed_consent, # Informed Consent
                                     )
            st.success("Treatment plan saved successfully!")

            # Here you would typically generate a PDF or structured output of the treatment plan
            st.download_button(
                label="Download Treatment Plan",
                data="This is where the actual treatment plan document would be generated",
                file_name="treatment_plan.pdf",
                mime="application/pdf"
            )
        else:
            st.error("Please ensure informed consent is obtained before saving the treatment plan.")

