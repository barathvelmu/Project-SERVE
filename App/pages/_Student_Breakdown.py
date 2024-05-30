import streamlit as st
import matplotlib.pyplot as plt
import requests
import pandas as pd


st.set_page_config(page_title="SERVE Student Breakdown", page_icon="📈")

st.title("SERVE Breakdown")
st.write(
    """This page shows breakdowns of SERVE by Faculty, Gender and More!"""
)

faculty, gender, year, students = st.tabs(["Faculty Breakdown", "Gender Breakdown", "Year Breakdown", "All Students"])
queries = requests.get("http://127.0.0.1:5000/StudentBreakdown").json()

with faculty:
    st.title("SERVE Members by Faculty - Spring 2024")

    # Convert the data into a DataFrame for better display
    faculty_df = pd.DataFrame(queries['faculty'])
    st.write(faculty_df)

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie([x[0] for x in queries['faculty'].values()], labels=queries['faculty'].keys(), autopct='%1.0f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

with gender:
    st.title("SERVE Members by Gender - Spring 2024")
    
    # Convert the data into a DataFrame for better display
    gender_df = pd.DataFrame(queries['gender'])
    st.write(gender_df)

    # Create the pie chart
    fig2, ax2 = plt.subplots()
    ax2.pie([x[0] for x in queries['gender'].values()], labels=queries['gender'].keys(), autopct='%1.0f%%', startangle=90)
    ax2.axis('equal')
    st.pyplot(fig2)

with year:
    st.title("SERVE Members by Year - Spring 2024")
    
    # Convert the data into a DataFrame for better display
    gender_df = pd.DataFrame(queries['year'])
    st.write(gender_df)

    # Create the pie chart
    fig2, ax2 = plt.subplots()
    ax2.pie([x[0] for x in queries['year'].values()], labels=queries['year'].keys(), autopct='%1.0f%%', startangle=90)
    ax2.axis('equal')
    st.pyplot(fig2)
    
with students:
    st.title("All SERVE Members - Spring 2024")
    
    # Convert the data into a DataFrame for better display
    students_df = pd.DataFrame(queries['students'])
    st.write(students_df)
    