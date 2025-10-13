# Modified app.py
import streamlit as st
import sqlite3
from db import init_db, register_user, login_user, get_user_profile, update_user_profile, save_recommendation, get_recommendations, save_chat_interaction, get_chat_history, change_password
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

if st.session_state.guest_mode:
    if st.session_state.guest_profile is None:
        # Prompt for guest details
        st.subheader("Guest Mode - Enter Your Details")
        with st.form("guest_form"):
            age = st.number_input("Age", min_value=20, max_value=100)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            health_condition = st.text_area("Health Condition (optional)")
            if st.form_submit_button("Submit"):
                st.session_state.guest_profile = {"age": age, "gender": gender, "health_condition": health_condition}
                st.success("Details submitted. Redirecting to Symptom Checker...")
                st.rerun()
    else:
        # Only render Symptom Checker for guest
        st.subheader("Symptom Checker Chatbot")
        symptoms = st.text_area("Describe your symptoms")
        if st.button("Get Advice"):
            response = get_chatbot_response(symptoms)
            st.write("Chatbot Response:", response)
        # Button to exit guest mode
        if st.button("Exit Guest Mode"):
            st.session_state.guest_mode = False
            st.session_state.guest_profile = None
            st.rerun()
else:
    # Sidebar for navigation in non-guest mode
    page_options = ["Home", "Register", "Login"]
    if st.session_state.user_id:
        page_options += ["Profile", "Health Plan", "Symptom Checker", "Notifications", "History", "Logout"]
    page = st.sidebar.selectbox("Navigate", page_options)

    if page == "Home":
        st.write("Welcome to Smart Health Assistant. Please register or login to get personalized health advice. Or use guest mode.")
        if st.button("Guest Mode"):
            st.session_state.guest_mode = True
            st.session_state.guest_profile = None
            st.rerun()

    elif page == "Register":
        st.subheader("Register")
        username = st.text_input("Username")
        full_name = st.text_input("Full Name")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        age = st.number_input("Age", min_value=20, max_value=100)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        health_history = st.text_area("Basic Health History")
        if st.button("Register"):
            success, message = register_user(username, password, email, age, gender, health_history, full_name)
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
                st.success("Login successful! Welcome back.")
                st.rerun()
            else:
                st.error("Invalid credentials.")

    elif page == "Profile":
        if st.session_state.user_id:
            st.subheader("Profile")
            profile = st.session_state.profile
            full_name = st.text_input("Full Name", value=profile['full_name'])
            age = st.number_input("Age", value=profile['age'], min_value=20, max_value=100)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(profile['gender']))
            health_history = st.text_area("Basic Health History", value=profile['health_history'])
            if st.button("Update Profile"):
                update_user_profile(st.session_state.user_id, age, gender, health_history, full_name)
                st.session_state.profile = get_user_profile(st.session_state.user_id)
                st.success("Profile updated.")

            st.subheader("Change Password")
            current_password = st.text_input("Current Password", type="password")
            new_password = st.text_input("New Password", type="password")
            if st.button("Update Password"):
                if current_password and new_password:
                    success = change_password(st.session_state.user_id, current_password, new_password)
                    if success:
                        st.success("Password updated successfully.")
                    else:
                        st.error("Current password is incorrect.")
                else:
                    st.warning("Please provide both current and new passwords.")
        else:
            st.warning("Please login.")

    elif page == "Health Plan":
        if st.session_state.user_id:
            st.subheader("Personalized Health Plan")
            profile = st.session_state.profile
            plan = generate_health_plan(profile['age'], profile['gender'])
            st.write("**Screenings:**", plan['screenings'])
            st.write("**Exercise Plan:**", plan['exercise'])
            st.write("**Vitamin Suggestions:**", plan['vitamins'])
            st.write("**Meal Planning:**", plan['meals'])
            if st.button("Save Plan"):
                save_recommendation(st.session_state.user_id, "Health Plan", str(plan))
                st.success("Plan saved.")
        else:
            st.warning("Please login.")

    elif page == "Symptom Checker":
        if st.session_state.user_id:
            st.subheader("Symptom Checker Chatbot")
            profile = st.session_state.profile
            symptoms = st.text_area("Describe your symptoms")
            if st.button("Get Advice"):
                response = get_chatbot_response(symptoms)
                st.write("Chatbot Response:", response)
                save_chat_interaction(st.session_state.user_id, symptoms, response)
        else:
            st.warning("Please login.")

    elif page == "Notifications":
        if st.session_state.user_id:
            st.subheader("Notifications")
            message = st.text_input("Notification Message (for testing)")
            if st.button("Send Email Reminder"):
                profile = st.session_state.profile
                send_email_notification(profile['email'], "Health Reminder", message)
                st.success("Email sent.")
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
        else:
            st.warning("Please login.")

    elif page == "Logout":
        st.session_state.user_id = None
        st.session_state.profile = None
        st.success("Logged out.")
        st.rerun()