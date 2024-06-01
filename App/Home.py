import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏐", initial_sidebar_state="auto", menu_items=None)

if 'Login' not in st.session_state:
    st.session_state['Login'] = False

st.title("SERVE Student Portal")

st.write("""
    Welcome to the SERVE Student Portal! This page provides insights on the UWaterloo SERVE Club, alongside information on upcoming events and a way to update your information.
""")