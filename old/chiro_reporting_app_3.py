import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime, timedelta
import random
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(page_title="Body RES Patient Tracker", page_icon="🦴", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: linear-gradient(to right, #f0f0f0, #e6e9f0);
    }
    .main > div {
        padding: 2rem;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .stButton>button {
        color: white;
        background-color: #3498db;
        border-radius: 5px;
    }
    .stSelectbox>div>div>div {
        background-color: #ecf0f1;
    }
    .stTextInput>div>div>input {
        background-color: #ecf0f1;
    }
    .stDataFrame {
        border: 1px solid #bdc3c7;
    }
</style>
""", unsafe_allow_html=True)


# Dummy data for demonstration
@st.cache_data
def load_patient_data(patient):
    # This is dummy data - replace with actual database query
    date_range = pd.date_range(start='2024-01-01', end='2024-03-04', freq='7D')
    num_points = len(date_range)

    return pd.DataFrame({
        'Date': date_range,
        'Pain Level': [7, 6, 6, 5, 5, 4, 3, 3, 2, 2][:num_points],
        'Neck ROM (degrees)': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75][:num_points],
        'Lower Back ROM (degrees)': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65][:num_points],
        'Oswestry Disability Index': [60, 55, 50, 45, 40, 35, 30, 25, 20, 15][:num_points],
        'Treatment Satisfaction': [3, 4, 4, 5, 5, 6, 7, 8, 9, 9][:num_points]
    })

def main():
    st.sidebar.title("🦴 Body RES")
    pages = [
        "Patient Information",
        "SOAP Notes",
        "Treatment Plan",
        "Progress Tracker",
        'Patient Summary'
    ]
    selection = st.sidebar.radio("Go to", pages)

    if selection == "Patient Information":
        patient_info()
    elif selection == "SOAP Notes":
        soap_notes()
    elif selection == "Treatment Plan":
        treatment_plan()
    elif selection == "Progress Tracker":
        progress_tracker()
    elif selection == "Patient Summary":
        patient_summary()


def patient_info():
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
        height = st.number_input("Height (cm)", min_value=0.0, step=1.0)
        weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)

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

    st.subheader("Pain Characteristics")
    pain_frequency = st.selectbox("Pain Frequency", ["Constant", "Intermittent", "Occasional"])
    pain_intensity = st.slider("Pain Intensity (0-10)", 0, 10, 5)
    pain_quality = st.multiselect("Pain Quality", ["Sharp", "Dull", "Aching", "Burning", "Tingling", "Numbness"])

    st.subheader("Consent and Agreements")
    consent = st.checkbox("I consent to chiropractic examination and treatment")
    privacy_agreement = st.checkbox("I have read and agree to the privacy policy")

    if st.button("Save Patient Information"):
        if consent and privacy_agreement:
            st.success("Patient information saved successfully!")
        else:
            st.error("Please provide consent and agree to the privacy policy before saving.")


def soap_notes():
    st.title("SOAP Notes")

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
            height = st.number_input("Height (cm)", min_value=0.0, step=1.0)
            weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)

    st.subheader("Range of Motion (ROM)")
    body_parts = ["Cervical Spine", "Thoracic Spine", "Lumbar Spine", "Shoulders", "Hips"]
    for part in body_parts:
        col1, col2 = st.columns(2)
        with col1:
            st.number_input(f"{part} Flexion (degrees)", 0, 180, 90, key=f"{part}_flexion")
        with col2:
            st.number_input(f"{part} Extension (degrees)", 0, 180, 90, key=f"{part}_extension")

    st.subheader("Orthopedic Tests")
    tests = ["Straight Leg Raise", "Kernig's Sign", "Brudzinski's Sign", "Spurling's Test", "Valsalva Maneuver"]
    for test in tests:
        st.selectbox(f"{test}", ["Positive", "Negative", "Not Performed"], key=f"ortho_{test}")

    st.subheader("Neurological Examination")
    neuro_tests = ["Deep Tendon Reflexes", "Muscle Strength", "Sensation"]
    for test in neuro_tests:
        st.text_area(f"{test} Results", key=f"neuro_{test}")

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
        st.success("SOAP notes saved successfully!")


def treatment_plan():
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


import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
from plotly.subplots import make_subplots


@st.cache_data
def load_patient_data(patient):
    # This is dummy data - replace with actual database query
    date_range = pd.date_range(start='2024-01-01', end='2024-03-04', freq='7D')
    num_points = len(date_range)

    return pd.DataFrame({
        'Date': date_range,
        'Pain Level': [7, 6, 6, 5, 5, 4, 3, 3, 2, 2][:num_points],
        'Neck ROM (degrees)': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75][:num_points],
        'Lower Back ROM (degrees)': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65][:num_points],
        'Oswestry Disability Index': [60, 55, 50, 45, 40, 35, 30, 25, 20, 15][:num_points],
        'Treatment Satisfaction': [3, 4, 4, 5, 5, 6, 7, 8, 9, 9][:num_points]
    })


def progress_tracker():
    st.title("Patient Progress Tracker")

    # Patient Selection
    patient_name = st.selectbox("Select Patient", ["John Doe", "Jane Smith",
                                                   "Alex Johnson"])  # This would be populated from your database

    # Date Range Selection
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date")
    with col2:
        end_date = st.date_input("End Date")

    try:
        df = load_patient_data(patient_name)
        df = df[(df['Date'] >= pd.Timestamp(start_date)) & (df['Date'] <= pd.Timestamp(end_date))]

        if df.empty:
            st.warning("No data available for the selected date range.")
            return

        # Overall Progress Summary
        st.header("Overall Progress Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            initial_pain = df['Pain Level'].iloc[0]
            current_pain = df['Pain Level'].iloc[-1]
            pain_change = initial_pain - current_pain
            st.metric("Pain Level Change", f"{pain_change}", f"{pain_change}")
        with col2:
            initial_odi = df['Oswestry Disability Index'].iloc[0]
            current_odi = df['Oswestry Disability Index'].iloc[-1]
            odi_change = initial_odi - current_odi
            st.metric("ODI Change", f"{odi_change}%", f"{odi_change}%")
        with col3:
            initial_satisfaction = df['Treatment Satisfaction'].iloc[0]
            current_satisfaction = df['Treatment Satisfaction'].iloc[-1]
            satisfaction_change = current_satisfaction - initial_satisfaction
            st.metric("Satisfaction Change", f"{satisfaction_change}", f"{satisfaction_change}")

        # Pain Level Over Time
        st.subheader("Pain Level Over Time")
        pain_chart = alt.Chart(df).mark_line().encode(
            x='Date',
            y='Pain Level',
            tooltip=['Date', 'Pain Level']
        ).properties(width=700, height=300)
        st.altair_chart(pain_chart, use_container_width=True)

        # Range of Motion Progress
        st.subheader("Range of Motion Progress")
        rom_chart = make_subplots(specs=[[{"secondary_y": True}]])
        rom_chart.add_trace(go.Scatter(x=df['Date'], y=df['Neck ROM (degrees)'], name="Neck ROM"), secondary_y=False)
        rom_chart.add_trace(go.Scatter(x=df['Date'], y=df['Lower Back ROM (degrees)'], name="Lower Back ROM"),
                            secondary_y=True)
        rom_chart.update_layout(title_text="Range of Motion Over Time")
        rom_chart.update_xaxes(title_text="Date")
        rom_chart.update_yaxes(title_text="Neck ROM (degrees)", secondary_y=False)
        rom_chart.update_yaxes(title_text="Lower Back ROM (degrees)", secondary_y=True)
        st.plotly_chart(rom_chart, use_container_width=True)

        # Oswestry Disability Index Progress
        st.subheader("Oswestry Disability Index Progress")
        odi_chart = alt.Chart(df).mark_line().encode(
            x='Date',
            y='Oswestry Disability Index',
            tooltip=['Date', 'Oswestry Disability Index']
        ).properties(width=700, height=300)
        st.altair_chart(odi_chart, use_container_width=True)

        # Treatment Satisfaction
        st.subheader("Treatment Satisfaction")
        satisfaction_chart = alt.Chart(df).mark_line().encode(
            x='Date',
            y='Treatment Satisfaction',
            tooltip=['Date', 'Treatment Satisfaction']
        ).properties(width=700, height=300)
        st.altair_chart(satisfaction_chart, use_container_width=True)

        # Body Heat Map
        st.subheader("Pain Location Heat Map")
        # This is a placeholder. In a real app, you'd use a proper heat map library or custom visualization
        st.image("https://via.placeholder.com/400x600.png?text=Body+Heat+Map+Placeholder")

        # Progress Notes
        st.subheader("Progress Notes")
        progress_notes = st.text_area("Add progress notes for this visit")

        # Next Steps
        st.subheader("Next Steps")
        next_steps = st.text_area("Outline next steps in the treatment plan")

        if st.button("Save Progress Update"):
            st.success("Progress update saved successfully!")

        # Option to generate a progress report
        if st.button("Generate Progress Report"):
            st.success("Progress report generated!")
            # Here you would typically generate a PDF report
            st.download_button(
                label="Download Progress Report",
                data="This is where the actual progress report document would be generated",
                file_name="progress_report.pdf",
                mime="application/pdf"
            )

    except Exception as e:
        st.error(f"An error occurred while loading or processing the data: {str(e)}")
        return


def patient_summary():
    st.title("Patient Summary")

    # Simulating patient selection from a database
    patient_name = st.selectbox("Select Patient", ["John Doe", "Jane Smith", "Alex Johnson"])

    # Dummy data for demonstration
    patient_info = {
        "John Doe": {
            "Age": 45,
            "Gender": "Male",
            "Initial Consultation": "2024-01-15",
            "Chief Complaint": "Lower back pain",
            "Total Visits": 12,
            "Last Visit": "2024-07-20"
        },
        "Jane Smith": {
            "Age": 32,
            "Gender": "Female",
            "Initial Consultation": "2024-02-03",
            "Chief Complaint": "Neck stiffness",
            "Total Visits": 8,
            "Last Visit": "2024-07-18"
        },
        "Alex Johnson": {
            "Age": 28,
            "Gender": "Non-binary",
            "Initial Consultation": "2024-03-10",
            "Chief Complaint": "Shoulder pain",
            "Total Visits": 6,
            "Last Visit": "2024-07-22"
        }
    }

    # Display patient information
    if patient_name in patient_info:
        st.header(f"Summary for {patient_name}")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Patient Information")
            for key, value in patient_info[patient_name].items():
                st.write(f"**{key}:** {value}")

        with col2:
            st.subheader("Treatment Progress")
            # Dummy progress data
            progress_data = pd.DataFrame({
                'Metric': ['Pain Level', 'ROM Improvement', 'Patient Satisfaction'],
                'Initial': [8, 0, 5],
                'Current': [3, 40, 9]
            })
            st.dataframe(progress_data)

        # Treatment history chart
        st.subheader("Treatment History")
        start_date = datetime.strptime(patient_info[patient_name]["Initial Consultation"], "%Y-%m-%d")
        end_date = datetime.strptime(patient_info[patient_name]["Last Visit"], "%Y-%m-%d")
        date_range = pd.date_range(start=start_date, end=end_date, freq='W')
        num_weeks = len(date_range)

        # Generate dummy pain levels that match the number of weeks
        pain_levels = [8] + [max(1, int(8 - i * 0.5)) for i in range(1, num_weeks)]
        pain_levels = pain_levels[:num_weeks]  # Ensure it matches the length of date_range

        history_data = pd.DataFrame({
            'Date': date_range,
            'Pain Level': pain_levels
        })

        chart = alt.Chart(history_data).mark_line().encode(
            x='Date',
            y='Pain Level',
            tooltip=['Date', 'Pain Level']
        ).properties(width=700, height=300)
        st.altair_chart(chart, use_container_width=True)

        # Recent SOAP notes
        st.subheader("Recent SOAP Notes")
        soap_notes = [
            {"Date": "2024-07-22", "S": "Patient reports reduced pain", "O": "Improved ROM in lower back",
             "A": "Progressing well", "P": "Continue with current treatment plan"},
            {"Date": "2024-07-15", "S": "Slight increase in pain after gardening", "O": "Mild tenderness in lower back",
             "A": "Minor setback due to overexertion", "P": "Advise on proper body mechanics for gardening"}
        ]
        for note in soap_notes:
            with st.expander(f"SOAP Note - {note['Date']}"):
                st.write(f"**Subjective:** {note['S']}")
                st.write(f"**Objective:** {note['O']}")
                st.write(f"**Assessment:** {note['A']}")
                st.write(f"**Plan:** {note['P']}")

        # Upcoming appointments
        st.subheader("Upcoming Appointments")
        upcoming_appointments = [
            {"Date": "2024-07-29", "Time": "10:00 AM", "Type": "Follow-up"},
            {"Date": "2024-08-12", "Time": "2:30 PM", "Type": "Re-evaluation"}
        ]
        for appt in upcoming_appointments:
            st.write(f"**{appt['Date']} at {appt['Time']}** - {appt['Type']}")

        # Treatment recommendations
        st.subheader("Current Treatment Recommendations")
        st.write("1. Continue with spinal adjustments twice a week")
        st.write("2. Perform prescribed exercises daily")
        st.write("3. Use heat therapy before bed")
        st.write("4. Maintain proper posture during work hours")

        # Generate report button
        if st.button("Generate Comprehensive Patient Report"):
            st.success("Comprehensive patient report generated!")
            st.download_button(
                label="Download Patient Report",
                data="This is where the actual patient report document would be generated",
                file_name=f"{patient_name}_report.pdf",
                mime="application/pdf"
            )

    else:
        st.warning("Please select a patient to view their summary.")

if __name__ == "__main__":
    main()