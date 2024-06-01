import streamlit as st
import requests

st.set_page_config(page_title="Login", page_icon="🏐")
st.title("SERVE Member Login")

with st.form("Form", clear_on_submit=False):
    email = st.text_input("Email")
    if st.form_submit_button("Send Code"):
        res = requests.get("http://127.0.0.1:5000/sendcode?email="+email).json()
        st.write(res["status"])

with st.form("Password", clear_on_submit=False):
    password = st.text_input("Code (Sent To Email)")
    if st.form_submit_button("Login with Code"):
        res = requests.get("http://127.0.0.1:5000/checkpassword?password="+password).json()

        if res["status"] == 1:
            st.session_state["Login"] = True
            st.write("Login Successful! App will log out on refresh.")
        else:
            st.write("Error. Please try again.")

# https://myaccount.google.com/u/3/apppasswords
# CS338DATABASE!
