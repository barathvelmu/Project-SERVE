import streamlit as st
from st_pages import Page, show_pages, hide_pages
from Home import set_session_tabs

hide_pages(["hide me!"])

if 'Login' not in st.session_state:
    st.session_state['Login'] = False

if 'Email' not in st.session_state:
    st.session_state['Email'] = False


