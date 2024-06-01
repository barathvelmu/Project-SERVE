import streamlit as st
import requests
from st_pages import Page, show_pages

st.set_page_config(page_title="Login", page_icon="🏐")
st.title("SERVE Member Login")

if 'Login' not in st.session_state:
    st.session_state['Login'] = False

if 'Email' not in st.session_state:
    st.session_state['Email'] = False

with st.form("Form", clear_on_submit=False):
    email = st.text_input("Email")
    if st.form_submit_button("Send Code"):
        res = requests.get("http://127.0.0.1:5000/sendcode?email="+email).json()
        st.write(res["status"])

    password = st.text_input("Code (Sent To Email)")
    if st.form_submit_button("Login with Code"):
        res = requests.get("http://127.0.0.1:5000/checkpassword?password="+password).json()

        if res["status"] == 1:
            st.session_state["Login"] = True
            st.session_state["Email"] = email
            st.write("Login Successful! App will log out on refresh.")
        else:
            st.write("Error. Please try again.")


if st.session_state["Login"]:
    show_pages(
        [
            Page("Home.py", "Home"),
            Page("pages/_Register.py", "Update Profile"),
            Page("pages/_Student_Breakdown.py", "Student Breakdown"),
        ]
    )
else:
    show_pages(
        [
            Page("Home.py", "Home"),
            Page("pages/_Login.py", "Login"),
            Page("pages/_Register.py", "Register"),
            Page("pages/_Student_Breakdown.py", "Student Breakdown"),
        ]
    )
# https://myaccount.google.com/u/3/apppasswords
# CS338DATABASE!
