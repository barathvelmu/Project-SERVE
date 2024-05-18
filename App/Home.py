import streamlit as st
import matplotlib.pyplot as plt
import requests
import pandas as pd

st.set_page_config(page_title=None, page_icon=None, initial_sidebar_state="auto", menu_items=None)

st.title("SERVE Student Portal")

st.write("""
    Welcome to the SERVE Student Portal! This page provides insights on the UWaterloo SERVE Club, alongside information on upcoming events and a way to update your information.
""")