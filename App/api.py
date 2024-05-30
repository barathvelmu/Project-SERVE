from flask import Flask
from flask_cors import CORS
from flask import request
import sqlite3

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
    
""" @app.route('/form', methods = ['GET', 'POST'])
def form(): """