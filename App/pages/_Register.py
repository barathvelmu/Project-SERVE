import streamlit as st
from api import form_submit
from email_validator import validate_email
from Home import set_session_tabs
from st_pages import Page, show_pages, hide_pages

#hide_pages(["Home"])
#st.set_page_config(page_title="Form", page_icon="🏐")
st.sidebar.image("logo.png")
st.sidebar.markdown("<h1 style='text-align: center;'>UW SERVE</h1>", unsafe_allow_html=True)    
st.title("SERVE Member Form")

if 'Login' not in st.session_state:
    st.session_state['Login'] = False

if 'Email' not in st.session_state:
    st.session_state['Email'] = False

if 'Exec' not in st.session_state:
    st.session_state['Exec'] = False
    
def allFieldsCompleted(email, firstname, lastname, student_id, gender, faculty, level_of_play):
    if (email and firstname and lastname 
              and student_id and gender 
              and faculty and level_of_play): 
        return True
    else: 
        return False


# DID NOT HANDLE "EvaledLEVEL", "execinitial1", "execinitial2" yet
if st.session_state["Login"]:
    st.write("Edit your user information here!")
else:
    st.write("Register as a member here!")

with st.form("Form", clear_on_submit=False):
    logged_in = False
    if st.session_state["Login"]:
        logged_in = True
        email = st.session_state["Email"]
        st.code(st.session_state["Email"], language="markdown")
    else:
        email = st.text_input("Email")

    firstname = st.text_input("Firstname")
    lastname = st.text_input("Lastname")
    student_id = st.number_input("Student Id", step=1, value = None) # Step = 1 used to make integer input only
    gender = st.selectbox("What is your gender?", ["Male", "Female", "Other"], index = None)
    # year_of_study = st.selectbox("What is your year of study?", ["1st year", "2nd year", "3rd year", "4th year", "5th year", "Alumni", "Graduate Student"], index = None)
    faculty = st.selectbox("What faculty are you part of?", ["Engineering", "Science", "Health", "Mathematics", "Environment", "Arts"], index = None)
    level_of_play = st.selectbox("What is your level of play? (OPTIONAL)", ["1", "2", "3", "4"], index = None)

    if st.form_submit_button("Submit"):
        if logged_in: # Update Info
            try:
                if len(str(int(student_id))) == 8:
                    try: 
                        validate_email(email)
                        if form_submit(email.lower(), firstname, lastname, student_id, gender, faculty, level_of_play):
                                st.success("Your student information has been updated!")
                        else: 
                            st.error("Update Failed. Please contact an administrator.")
                    except Exception as e:
                        st.error(f"Email format is invalid.")
                else: 
                    st.error("Student number is invalid. Please enter the 8-digit number.")
            except:
                st.error("Please fill in all fields")
        else: # Add new account
            if allFieldsCompleted(email, firstname, lastname, student_id, gender, faculty, level_of_play):
                if len(str(int(student_id))) == 8:
                    try: 
                        validate_email(email)
                        if form_submit(email.lower(), firstname, lastname, student_id, gender, faculty, level_of_play):
                            st.success("Your student information has been added! Please log in through the Login tab.")
                        else: 
                            st.error("Update Failed. Please contact an administrator.")
                    except Exception as e:
                        st.error(f"Email format is invalid.")
                else: 
                    st.error("Student number is invalid. Please enter the 8-digit number.")
            else:
                st.error("Please complete all fields.")

            
set_session_tabs()