import streamlit as st
from st_pages import Page, show_pages
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="UW Serve", page_icon="🏐", initial_sidebar_state="auto", menu_items=None)

if 'Login' not in st.session_state:
    st.session_state['Login'] = False

if 'Email' not in st.session_state:
    st.session_state['Email'] = False

st.title("SERVE Student Portal")

st.write("""
    Welcome to the SERVE Student Portal! This page provides insights on the UWaterloo SERVE Club, alongside information on upcoming events and a way to update your information.
""")
st.sidebar.image("logo.png")
st.sidebar.markdown("<h1 style='text-align: center;'>UW SERVE</h1>", unsafe_allow_html=True)
def set_session_tabs():
    if st.session_state["Login"]:
        show_pages(
            [
                Page("Home.py", "Home"),
                Page("pages/_Register.py", "Profile (%s)" % (st.session_state["Email"])),
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