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
    issues_df = issues_df.append({"Issue": issue_description, "Severity": severity, 
                                  "Image": issue_image, "Status": "Pending"}, ignore_index=True)
    st.success("Issue submitted successfully!")

# Crowdfunding & Resource Mobilization Section
st.title("Support a Campaign")
campaign_title = st.text_input("Campaign Title")
campaign_description = st.text_area("Campaign Description")
donation_amount = st.number_input("Amount to Donate ($)", min_value=0)
donate_button = st.button("Donate")

if donate_button:
    donations_df = donations_df.append({"User": user_name, "Amount": donation_amount, 
                                        "Campaign": campaign_title}, ignore_index=True)
    user_activities_df = user_activities_df.append({"User": user_name, "Activity": f"Donated {donation_amount} to {campaign_title}", 
                                                    "Points": 10}, ignore_index=True)
    st.success(f"Thank you for donating ${donation_amount} to {campaign_title}!")
    user_score += 10  # Update score for donation

# Humanitarian Credit Score Section
st.sidebar.subheader("Humanitarian Credit Score")
st.sidebar.write(f"Your current score: {user_score}")

# Social Sharing & Engagement Section
st.title("Share a Campaign")
st.markdown("Share your contribution and help spread the word!")
st.button("Share on Facebook")
st.button("Share on Twitter")
st.button("Share on Instagram")

# Admin Panel for Verification (simplified version)
st.title("Admin Panel - Verify Project Progress")
project_to_verify = st.selectbox("Select Project to Verify", issues_df["Issue"].tolist())
verify_button = st.button("Verify Project Progress")

if verify_button:
    st.success(f"Project '{project_to_verify}' verified successfully!")
    issues_df.loc[issues_df["Issue"] == project_to_verify, "Status"] = "Completed"

# Display Issues and Donations
st.subheader("Community Issues")
st.write(issues_df)

st.subheader("Donations")
st.write(donations_df)
