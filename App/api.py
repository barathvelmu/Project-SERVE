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
    con = sqlite3.connect("SERVE_PROD.db")

    # Students by Faculty
    res = con.execute("""select Faculty, count(*)
        from Member
        inner join Member_Valid_For_Term
        on Member.Email = Member_Valid_For_Term.Email
        where Member_Valid_For_Term.Tcode = "S2024"
        group by Faculty""")
    results_faculty = {}
    for row in res:
        results_faculty[row[0]] = [row[1]]

    # Students by Gender
    res = con.execute("""
    select Gender, count(*)
    from Member
    inner join Member_Valid_For_Term
    on Member.Email = Member_Valid_For_Term.Email
    where Member_Valid_For_Term.Tcode = "S2024"
    group by Gender
    """)
    results_gender= {}
    for row in res:
        results_gender[row[0]] = [row[1]]

    # Students by Level
    res = con.execute("""
    select coalesce(Level, "Not Assigned") as Assigned_Level, count(*)
    from Member
    inner join Member_Valid_For_Term
    on Member.Email = Member_Valid_For_Term.Email
    where Member_Valid_For_Term.Tcode = "S2024"
    group by Assigned_Level
    """)
    results_year= {}
    for row in res:
        results_year[row[0]] = [row[1]]
        
    # All Students
    con.row_factory = sqlite3.Row
    res = con.execute("""
    select Fname || " " || Lname as Name, Gender, Faculty, Level
    from Member
    inner join Member_Valid_For_Term
    on Member.Email = Member_Valid_For_Term.Email
    where Member_Valid_For_Term.Tcode = "S2024"
    Order by Name
    """)
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
def form_submit(email, firstname, lastname, student_id, gender, faculty, level_of_play):
    con = sqlite3.connect("SERVE_PROD.db")
    try:
        email_exists = con.execute("SELECT count(Email) FROM Member where Email = '%s'" % (str(email))).fetchall()[0][0] # 1 if account exists else 0
        print(email_exists)
        if email_exists == 0: # Email DNE, add new record
            # print("A")
            con.execute("INSERT INTO Member (StdNo, Fname, Lname, Email, Gender, Faculty, Level, EvaluatorEmail) VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', NULL)" % 
                (student_id, firstname, lastname, str(email), gender, faculty, level_of_play)) #Update Member
            con.commit()
            # print("B")
            con.execute("INSERT INTO Member_Valid_For_Term (Tcode, Email) values ('%s', '%s')" % ("S2024", str(email))) # Update Member_Valid_For_Term
            con.commit()
        else: # email exists, update
            con.execute("UPDATE Member SET StdNo = ?, Fname = ?, Lname = ?, Gender = ?, Faculty = ?, Level = ? where Email = ?", 
                (student_id, firstname, lastname, gender, faculty, level_of_play, email))
            con.commit()
        con.close()
        return True
    except Exception as e:
        # print(str(e))
        return False

@app.route('/sendcode', methods = ['GET', 'POST'])
def send_code():
    # Get email input
    email = str(request.args.get('email'))

    # Check if email is in S24_Members (count(Email) >= 1)
    con = sqlite3.connect("SERVE_PROD.db")
    result = con.execute("SELECT count(Email) FROM Member where Email = '%s'" % (str(email))).fetchall()[0][0]
    result_exec = 0 #con.execute("SELECT count(Email) FROM Executive where Email = '%s'" % (str(email))).fetchall()[0][0]
    con.close()
    if result == 0 and result_exec == 0:
        return {'status': "Please Register or contact Admin - Email not detected in database."}

    # Generate and update password in Password (called code)
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))
    con = sqlite3.connect("SERVE_PROD.db")
    result = con.execute("SELECT count(Email) FROM Account where Email = '%s'" % (str(email))).fetchall()[0][0]
    if result == 0: # Email never logged in, add new row
        con.execute("INSERT INTO Account (Password, Email) VALUES ('%s', '%s')" % (password, email))
        con.commit()
        con.close()
    else: # Email in table, update password
        con.execute("UPDATE Account SET Password = '%s' WHERE Email = '%s'"%(password, email))
        con.commit()
        con.close()
    print("Hello")
    # if the email is registered send a custom code
    email = str(request.args.get('email'))
    subject = "Email Subject"
    body = "This is your password: " + password
    sender = "uwservedb@gmail.com"
    recipients = [email]
    password = "yuqjdcbrvdhtkqku"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server: #_SSL 465
        try:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
            return {'status': "Code Sent to Email! This may take a few minutes! Please use it below:"}
        except Exception as e:
            return {'status': "Error: " + str(e)}

@app.route('/checkpassword', methods = ['GET', 'POST'])
def check_password():
    password = str(request.args.get('password'))
    con = sqlite3.connect("SERVE_PROD.db")
    result = con.execute("SELECT count(Email) FROM Account where Password = '%s'" % (str(password))).fetchall()[0][0]
    con.close()
    if result == 1: # success
        return {'status': 1}
    else: # fail
        return {'status': 0}

@app.route('/session', methods = ['GET', 'POST'])
def session():

    con = sqlite3.connect("SERVE_PROD.db")
    teams = con.execute("""SELECT Team.TeamName, Tournament.TorneyName, Tournament.Date, Tournament.StartTime, Tournament.EndTime, Tournament.Location
                            From Team
                            INNER JOIN Tournament
                            ON Team.EventId = Tournament.EventId
                            WHERE Tcode = 'S2024'""").fetchall()
    events = con.execute("""SELECT distinct Tournament.TorneyName, Tournament.Date, Tournament.StartTime, Tournament.EndTime, Tournament.Location
                            From Tournament
                            WHERE Tcode = 'S2024'""").fetchall()
    con.close()
    return {"teams": teams, "events": events}

"""
With Teams as (
SELECT *
From Team
INNER JOIN Tournament
ON Team.EventId = Tournament.EventId
WHERE Tcode = 'S2024'
) SELECT Email, Teams.TeamName
From Member_Make_Team
inner JOIN Teams
on Teams.TeamId = Member_Make_Team.TeamId
"""