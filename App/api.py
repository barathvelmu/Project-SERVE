from flask import Flask
from flask_cors import CORS
from flask import request
import sqlite3
import streamlit as st

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return """You aren't supposed to be here.
    
    
    Leave."""

@app.route('/StudentBreakdown', methods = ['GET', 'POST'])
def test():
    con = sqlite3.connect("SERVE.db")

    # Students by Faculty
    res = con.execute("SELECT Faculty, count(*) from S24_Members group by Faculty")
    results_faculty = {}
    for row in res:
        results_faculty[row[0]] = [row[1]]

    # Students by Gender
    res = con.execute("SELECT Gender, count(*) from S24_Members group by Gender")
    results_gender= {}
    for row in res:
        results_gender[row[0]] = [row[1]]

    # Students by Year
    res = con.execute("SELECT YearOfStudy, count(*) from S24_Members group by YearOfStudy")
    results_year= {}
    for row in res:
        results_year[row[0]] = [row[1]]
        
    # All Students
    con.row_factory = sqlite3.Row
    res = con.execute("SELECT * FROM S24_Members")
    rows = res.fetchall() # obtain all of the rows from query
    results_all = []
    for row in rows:
        results_all.append(dict(row))
        
    con.close()

    return {
        'faculty': results_faculty, 
        'gender': results_gender, 
        'year': results_year,
        'students': results_all}
    
# @app.route('/form', methods = ['GET', 'POST'])
def form_submit(email, full_name, firstname, student_id, gender, year_of_study, faculty, level_of_play, ottawa_trip_interest):
    con = sqlite3.connect("SERVE.db")
    try:
        con.execute("INSERT INTO S24_Members (Email, Name, Firstname, StudentNumber, Gender, YearofStudy, Faculty, LevelofPlay, OttawaVNLTripInterest, Completiontime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, strftime('%m/%d/%Y', 'now'))", 
            (email, full_name, firstname, student_id, gender, year_of_study, faculty, level_of_play, ottawa_trip_interest))
        con.commit()
        return True
    except Exception as e: 
        st.error(f"Error: {e}")
        return False