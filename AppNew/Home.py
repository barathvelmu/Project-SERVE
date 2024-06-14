import streamlit as st
from st_pages import Page, show_pages, hide_pages

def set_session_tabs():
    
    if st.session_state["Login"]:
        show_pages(
            [
                Page("Tabs.py", "hide me!"),
                Page("pages/_Home_Page.py", "Home"),
                Page("pages/_Register.py", "Profile (%s)" % (st.session_state["Email"])),
                Page("pages/_Student_Breakdown.py", "Student Breakdown"),
            ]
        )
        hide_pages(["Tabs.py"])
    else:
        show_pages(
            [
                Page("Tabs.py", "hide me!"),
                Page("pages/_Home_Page.py", "Home"),
                Page("pages/_Login.py", "Login"),
                Page("pages/_Register.py", "Register"),
                Page("pages/_Student_Breakdown.py", "Student Breakdown"),
            ]
        )
        hide_pages(["hide me!"])