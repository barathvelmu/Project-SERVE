import streamlit as st
import matplotlib.pyplot as plt
import requests
import pandas as pd
from Home import set_session_tabs
from st_pages import Page, show_pages, hide_pages

#hide_pages(["Home"])
#st.set_page_config(page_title="Students", page_icon="🏐")
st.sidebar.image("logo.png")
st.sidebar.markdown("<h1 style='text-align: center;'>UW SERVE</h1>", unsafe_allow_html=True)
st.title("SERVE Breakdown")

if 'Login' not in st.session_state:
    st.session_state['Login'] = False

if 'Email' not in st.session_state:
    st.session_state['Email'] = False

if st.session_state["Login"]:
    
    st.write("This page shows breakdowns of SERVE by Faculty, Gender and More!")
    faculty, gender, year, students = st.tabs(["Faculty Breakdown", "Gender Breakdown", "Level Breakdown", "All Students"])
    queries = requests.get("http://127.0.0.1:5000/StudentBreakdown").json()

    with faculty:
        st.title("SERVE Members by Faculty - Spring 2024")

        # Convert the data into a DataFrame for better display
        faculty_df = pd.DataFrame(queries['faculty'])
        st.write(faculty_df)

        # Create the pie chart
        fig1, ax1 = plt.subplots()
        fig1.set_facecolor('darkgrey')
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
        fig2.set_facecolor('darkgrey')
        ax2.pie([x[0] for x in queries['gender'].values()], labels=queries['gender'].keys(), autopct='%1.0f%%', startangle=90)
        ax2.axis('equal')
        st.pyplot(fig2)

    with year:
        st.title("SERVE Members by Level - Spring 2024")
        
        # Convert the data into a DataFrame for better display
        gender_df = pd.DataFrame(queries['year'])
        st.write(gender_df)

        # Create the pie chart
        fig3, ax3 = plt.subplots()
        fig3.set_facecolor('darkgrey')
        ax3.pie([x[0] for x in queries['year'].values()], labels=queries['year'].keys(), autopct='%1.0f%%', startangle=90)
        ax3.axis('equal')
        st.pyplot(fig3)
        
    with students:
        st.title("All SERVE Members - Spring 2024")
        
        # Convert the data into a DataFrame for better display
        students_df = pd.DataFrame(queries['students'])
        st.dataframe(students_df[["Name", "Faculty", "Gender", "Level"]])
else:
    st.warning("Please Login to see this page")


set_session_tabs()