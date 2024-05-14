import streamlit as st
import matplotlib.pyplot as plt
import requests
import pandas as pd

st.title("SERVE Members by Faculty - Spring 2024")

response = requests.get("http://127.0.0.1:5000/test")

# Print the response
response_json = response.json()
st.write(pd.DataFrame(response_json))
fig1, ax1 = plt.subplots()
ax1.pie([x[0] for x in response_json.values()], labels=response_json.keys(), autopct='%1.00f%%',startangle=90)
ax1.axis('equal')
st.pyplot(fig1)