import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Chiropractic Patient Tracker")

# Patient Information
st.header("Patient Information")
patient_name = st.text_input("Patient Name")
patient_id = st.text_input("Patient ID")
visit_date = st.date_input("Visit Date")
visit_time = st.time_input("Visit Time")

# SOAP Notes
st.header("SOAP Notes")

subjective = st.text_area("Subjective", height=100)
objective = st.text_area("Objective", height=100)
assessment = st.text_area("Assessment", height=100)
plan = st.text_area("Plan", height=100)

# Pain Scale
pain_scale = st.slider("Pain Scale (0-10)", 0, 10, 5)

# Save button
if st.button("Save Visit Data"):
    # Here you would typically save the data to a database
    st.success("Visit data saved successfully!")

# View Progress
st.header("View Patient Progress")
selected_patient = st.selectbox("Select Patient", ["Patient 1", "Patient 2", "Patient 3"])  # This would be populated from your database

# Dummy data for demonstration
data = {
    'Date': ['2024-07-01', '2024-07-15', '2024-07-29'],
    'Pain Scale': [8, 6, 4],
    'Range of Motion (degrees)': [30, 45, 60]
}
df = pd.DataFrame(data)

st.line_chart(df.set_index('Date'))

# Display SOAP notes history
st.subheader("SOAP Notes History")
st.table(df)