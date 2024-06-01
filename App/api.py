from flask import Flask
from flask_cors import CORS
from flask import request
import sqlite3
import string
import random
import smtplib
from email.mime.text import MIMEText

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
    except:
        return False

@app.route('/sendcode', methods = ['GET', 'POST'])
def send_code():
    # Get email input
    email = str(request.args.get('email'))

    # Check if email is in S24_Members (count(Email) >= 1)
    con = sqlite3.connect("SERVE.db")
    result = con.execute("SELECT count(Email) FROM S24_Members where Email = '%s'" % (str(email))).fetchall()[0][0]
    con.close()
    if result == 0:
        return {'status': "Please Register or contact Admin - Email not detected in database."}

    # Generate and update password in Password (called code)
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))
    con = sqlite3.connect("SERVE.db")
    result = con.execute("SELECT count(Email) FROM Password where Email = '%s'" % (str(email))).fetchall()[0][0]
    if result == 0: # Email never logged in, add new row
        con.execute("INSERT INTO Password (Email, Code) VALUES ('%s', '%s')" % (email,password))
        con.commit()
        con.close()
    else: # Email in table, update password
        con.execute("UPDATE Password SET code = '%s' WHERE Email = '%s'"%(password, email))
        con.commit()
        con.close()

    # if the email is registered send a custom code
    email = str(request.args.get('email'))
    subject = "Email Subject"
    body = "This is your password: " + password
    sender = "uwservedb@gmail.com"
    recipients = [email]
    password = "jrmbgzrphpeclhaq"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        try:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
            return {'status': "Code Sent! Please Enter Below"}
        except Exception as e:
            return {'status': "Error: " + str(e)}

@app.route('/checkpassword', methods = ['GET', 'POST'])
def check_password():
    password = str(request.args.get('password'))
    con = sqlite3.connect("SERVE.db")
    result = con.execute("SELECT count(Email) FROM Password where Code = '%s'" % (str(password))).fetchall()[0][0]
    con.close()
    if result == 1: # success
        return {'status': 1}
    else: # fail
        return {'status': 0}
