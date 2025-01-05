import streamlit as st
import pandas as pd

# Mock database for storing reports, donations, and users
issues_df = pd.DataFrame(columns=["Issue", "Severity", "Image", "Status"])
donations_df = pd.DataFrame(columns=["User", "Amount", "Campaign"])
user_activities_df = pd.DataFrame(columns=["User", "Activity", "Points"])

# Sidebar for user profile and Humanitarian Credit Score
st.sidebar.header("User Profile")
user_name = st.sidebar.text_input("Enter your name")
user_score = 0  # Initialize humanitarian score

# Problem Identification & Grading Section
st.title("Report a Community Issue")
issue_description = st.text_area("Describe the Issue")
severity = st.selectbox("Select Severity", ["Minor", "Moderate", "Severe"])
issue_image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
submit_report = st.button("Submit Report")

if submit_report:
    new_issue = pd.DataFrame([{"Issue": issue_description, "Severity": severity, 
                               "Image": issue_image, "Status": "Pending"}])
    issues_df = pd.concat([issues_df, new_issue], ignore_index=True)
    st.
