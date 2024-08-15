# main.py
# This script will be the primary Streamlit app file. It will import and call functions from
# other modules.
#
#============================================================================================

import streamlit as st
from src.patient_info import patient_info_page
from src.soap_info import soap_notes_page
from src.treatment_plan_info import treatment_plan_page
from src.progress_tracker_info import progress_tracker_page

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
        patient_info_page()
    elif selection == "SOAP Notes":
        soap_notes_page()
    elif selection == "Treatment Plan":
        treatment_plan_page()
    elif selection == "Progress Tracker":
        progress_tracker_page()
    elif selection == "Patient Summary":
        patient_summary()

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
