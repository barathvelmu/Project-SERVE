import streamlit as st
from st_pages import Page, show_pages, hide_pages

hide_pages(["Home"])

if 'Login' not in st.session_state:
    st.session_state['Login'] = False

if 'Email' not in st.session_state:
    st.session_state['Email'] = False

def set_session_tabs():
    
    if st.session_state["Login"]:
        show_pages(
            [
                Page("pages/_Home_Page.py", "Home Page"),
                Page("pages/_Register.py", "Profile (%s)" % (st.session_state["Email"])),
                Page("pages/_Tournaments.py", "Tournaments"),
                Page("pages/_Student_Breakdown.py", "Student Breakdown"),
            ]
        )
    else:
        show_pages(
            [
                Page("pages/_Home_Page.py", "Home Page"),
                Page("pages/_Login.py", "Login"),
                Page("pages/_Register.py", "Register"),
                Page("pages/_Tournaments.py", "Tournaments"),
                Page("pages/_Student_Breakdown.py", "Student Breakdown"),
            ]
        )
        hide_pages(["Home"])