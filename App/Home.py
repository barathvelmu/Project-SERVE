import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(page_title="Home", page_icon="🏐", initial_sidebar_state="auto", menu_items=None)

if 'Login' not in st.session_state:
    st.session_state['Login'] = False

if 'Email' not in st.session_state:
    st.session_state['Email'] = False

st.title("SERVE Student Portal")

st.write("""
    Welcome to the SERVE Student Portal! This page provides insights on the UWaterloo SERVE Club, alongside information on upcoming events and a way to update your information.
""")

if st.session_state["Login"]:
    show_pages(
        [
            Page("Home.py", "Home"),
            Page("pages/_Register.py", "Update Profile for (%s)" % (st.session_state["Email"])),
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