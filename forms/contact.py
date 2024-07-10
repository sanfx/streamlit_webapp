# Python Standard imports
import re

# Third Party imports
import streamlit as st
import requests

WEBHOOK_URL = st.secrets['WEBHOOK_URL']

def is_valid_email(email):
    # a very basic pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Type your message")
        submit_button = st.form_submit_button("Send")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email service is not setup. Please try again later", icon="🤖")
                st.stop()

            if not name:
                st.error("Please provide your name", icon="ℹ")
                st.stop()

            if not email:
                st.error("Please provide your email address.", icon="📨")
                st.stop()

            if not is_valid_email(email):
                st.error("Please provide a valid email address.", icon="💌")
                st.stop()
            
            if not message:
                st.error("Please provide a message.", icon="📃")
                st.stop()
            

            # Process the data payload and send it to the specified webook URL
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Your message has been sent successfully! 🎉", icon="🚀")
            else:
                st.error("There was an error sending the message.", icon="😨")
