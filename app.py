import streamlit as st
import sqlite3
from db import init_db, register_user, login_user, get_user_profile, update_user_profile, save_recommendation, get_recommendations, save_chat_interaction, get_chat_history
from health_recommendations import generate_health_plan
from symptom_chatbot import get_chatbot_response
from notifications import send_email_notification
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize database
init_db()

# Session state for user
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'guest_mode' not in st.session_state:
    st.session_state.guest_mode = False
if 'guest_profile' not in st.session_state:
    st.session_state.guest_profile = None

st.title("Smart Health Assistant")

# Sidebar for navigation
page = st.sidebar.selectbox("Navigate", ["Home", "Register", "Login", "Profile", "Health Plan", "Symptom Checker", "Notifications", "History", "Logout"])

if page == "Home":
    st.write("Welcome to Smart Health Assistant. Please register or login to get personalized health advice. Or use guest mode.")
    if st.button("Guest Mode"):
        st.session_state.guest_mode = True
        st.session_state.guest_profile = None  # Reset guest profile
        # Prompt for guest details
        with st.form("guest_form"):
            age = st.number_input("Age", min_value=20, max_value=100)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            medical_condition = st.text_area("Medical Condition (optional)")
            if st.form_submit_button("Submit"):
                st.session_state.guest_profile = {"age": age, "gender": gender, "medical_condition": medical_condition}
                st.success("Guest mode activated. Redirecting to Symptom Checker...")
                # Redirect to Symptom Checker
                st.session_state.page = "Symptom Checker"  # Set the page in session state
                st.rerun()

elif page == "Register":
    st.subheader("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=20, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    health_history = st.text_area("Basic Health History")
    if st.button("Register"):
        success, message = register_user(username, password, email, age, gender, health_history)
        st.write(message)
        if success:
            st.success("Registered successfully. Please login.")

elif page == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user_id = login_user(username, password)
        if user_id:
            st.session_state.user_id = user_id
            st.session_state.profile = get_user_profile(user_id)
            st.session_state.guest_mode = False
            st.success("Logged in successfully.")
            st.rerun()
        else:
            st.error("Invalid credentials.")

elif page == "Profile":
    if st.session_state.user_id or st.session_state.guest_mode:
        st.subheader("Profile")
        if st.session_state.guest_mode and st.session_state.guest_profile:
            profile = st.session_state.guest_profile
            age = st.number_input("Age (Guest)", value=profile['age'], min_value=20, max_value=100)
            gender = st.selectbox("Gender (Guest)", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(profile['gender']))
            medical_condition = st.text_area("Medical Condition (Guest)", value=profile['medical_condition'])
            st.session_state.guest_profile = {"age": age, "gender": gender, "medical_condition": medical_condition}
        else:
            profile = st.session_state.profile
            age = st.number_input("Age", value=profile['age'], min_value=20, max_value=100)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(profile['gender']))
            health_history = st.text_area("Basic Health History", value=profile['health_history'])
            if st.button("Update Profile"):
                update_user_profile(st.session_state.user_id, age, gender, health_history)
                st.session_state.profile = get_user_profile(st.session_state.user_id)
                st.success("Profile updated.")
    else:
        st.warning("Please login or use guest mode.")

elif page == "Health Plan":
    if st.session_state.user_id or (st.session_state.guest_mode and st.session_state.guest_profile):
        st.subheader("Personalized Health Plan")
        profile = st.session_state.profile if st.session_state.user_id else st.session_state.guest_profile
        if profile:
            plan = generate_health_plan(profile['age'], profile['gender'])
            st.write("**Screenings:**", plan['screenings'])
            st.write("**Exercise Plan:**", plan['exercise'])
            st.write("**Vitamin Suggestions:**", plan['vitamins'])
            st.write("**Meal Planning:**", plan['meals'])
            if st.session_state.user_id and st.button("Save Plan"):
                save_recommendation(st.session_state.user_id, "Health Plan", str(plan))
                st.success("Plan saved.")
        else:
            st.warning("Please provide your profile details first.")
    else:
        st.warning("Please login or use guest mode with profile details.")

elif page == "Symptom Checker":
    if st.session_state.user_id or (st.session_state.guest_mode and st.session_state.guest_profile):
        st.subheader("Symptom Checker Chatbot")
        profile = st.session_state.profile if st.session_state.user_id else st.session_state.guest_profile
        if profile:
            symptoms = st.text_area("Describe your symptoms")
            if st.button("Get Advice"):
                response = get_chatbot_response(symptoms)
                st.write("Chatbot Response:", response)
                if st.session_state.user_id:
                    save_chat_interaction(st.session_state.user_id, symptoms, response)
        else:
            st.warning("Please provide your profile details first.")
    else:
        st.warning("Please login or use guest mode with profile details.")

elif page == "Notifications":
    if st.session_state.user_id:
        st.subheader("Notifications")
        message = st.text_input("Notification Message (for testing)")
        if st.button("Send Email Reminder"):
            profile = st.session_state.profile
            send_email_notification(profile['email'], "Health Reminder", message)
            st.success("Email sent.")
    elif st.session_state.guest_mode:
        st.warning("Notifications not available in guest mode.")
    else:
        st.warning("Please login.")

elif page == "History":
    if st.session_state.user_id:
        st.subheader("History")
        st.write("**Recommendations History:**")
        recs = get_recommendations(st.session_state.user_id)
        for rec in recs:
            st.write(f"{rec['date']}: {rec['type']} - {rec['content']}")
        
        st.write("**Chat History:**")
        chats = get_chat_history(st.session_state.user_id)
        for chat in chats:
            st.write(f"{chat['date']}: User: {chat['message']} - Bot: {chat['response']}")
    elif st.session_state.guest_mode:
        st.warning("History not available in guest mode.")
    else:
        st.warning("Please login.")

elif page == "Logout":
    st.session_state.user_id = None
    st.session_state.guest_mode = False
    st.session_state.guest_profile = None
    st.session_state.profile = None
    st.success("Logged out.")
    st.rerun()