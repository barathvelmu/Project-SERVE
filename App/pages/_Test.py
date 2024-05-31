import streamlit as st
from api import form_submit
import requests

st.set_page_config(page_title="Login", page_icon="📈")
st.title("SERVE Member Login")

with st.form("Form", clear_on_submit=False):
    email = st.text_input("Email")
    if st.form_submit_button("Submit"):
        res = requests.get("http://127.0.0.1:5000/sendcode?email="+email).json()
        st.write(res)

        

# https://myaccount.google.com/u/3/apppasswords
# CS338DATABASE!
