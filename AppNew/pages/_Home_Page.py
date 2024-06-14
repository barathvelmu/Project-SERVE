import streamlit as st
from st_pages import Page, show_pages, hide_pages
from Home import set_session_tabs

hide_pages(["hide me!"])
st.sidebar.image("logo.png")
st.sidebar.markdown("<h1 style='text-align: center;'>UW SERVE</h1>", unsafe_allow_html=True)

st.title("SERVE Student Portal")

st.write("""
    Welcome to the SERVE Student Portal! This page provides insights on the UWaterloo SERVE Club, alongside information on upcoming events and a way to update your information.
""")