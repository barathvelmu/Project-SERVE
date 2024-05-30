import streamlit as st
from api import form_submit
from email_validator import validate_email

st.set_page_config(page_title="Form", page_icon="📈")
st.title("SERVE Member Information Form")
st.write("Register as a member here!")

def allFieldsCompleted(email, full_name, firstname, student_id, gender, year_of_study, faculty, level_of_play, ottawa_trip_interest):
    if (email and full_name and firstname and lastname 
              and student_id and gender and year_of_study 
              and faculty and level_of_play and ottawa_trip_interest): 
        return True
    else: 
        return False

# DID NOT HANDLE "EvaledLEVEL", "execinitial1", "execinitial2" yet
with st.form("Form", clear_on_submit=False):
    email = st.text_input("Email")
    full_name = st.text_input("Full Name")
    firstname = st.text_input("Firstname")
    lastname = st.text_input("Lastname")
    student_id = st.number_input("Student Id", step=1, value = None) # Step = 1 used to make integer input only
    gender = st.selectbox("What is your gender?", ["Male", "Female", "Other"], index = None)
    year_of_study = st.selectbox("What is your year of study?", ["1st year", "2nd year", "3rd year", "4th year", "5th year", "Alumni", "Graduate Student"], index = None)
    faculty = st.selectbox("What faculty are you part of?", ["Engineering", "Science", "Health", "Mathematics", "Environment", "Arts"], index = None)
    level_of_play = st.selectbox("What is your level of play?", ["Level 1", "Level 2", "Level 3", "Level 4"], index = None)
    ottawa_trip_interest = st.selectbox("Are you willing to go to Ottawa?", ["Yes", "No"], index = None)

    if st.form_submit_button("Submit"):
        if allFieldsCompleted(email, full_name, firstname, student_id, gender, year_of_study, faculty, level_of_play, ottawa_trip_interest):
            if len(str(int(student_id))) == 8:
                try: 
                    validate_email(email)
                    if form_submit(email, full_name, firstname, student_id, gender, year_of_study, faculty, level_of_play, ottawa_trip_interest):
                        st.success("Your student information has been updated!")
                    else: 
                        st.error("Update Failed. Please contact an administrator.")
                except Exception as e:
                    st.error(f"Email format is invalid. ERROR: '{e}'.")
            else: 
                st.error("Student number is invalid. Please enter the 8-digit number.")
        else:
            st.error("Please complete all fields.")
                


