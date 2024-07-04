import sqlite3

con = sqlite3.connect('SampleData/SERVE_SAMPLE.db')
cursor = con.cursor()

# Select All
cursor.execute("SELECT * FROM Member")
# Gender Count
cursor.execute("SELECT Gender, count(*) from Member group by Gender")
# Faculty Count
cursor.execute("SELECT Faculty, count(*) from Member group by Faculty")
# Level Count
cursor.execute("SELECT Level, count(*) from Member group by Level")
# Level by Faculty Count
cursor.execute("SELECT Level, Faculty, count(*) from Member group by Faculty, Level")
# Evaluator Count
cursor.execute("SELECT EvaluatorEmail, count(*) from Member group by EvaluatorEmail")
# Students by Faculty
cursor.execute("""SELECT Faculty, count(*)
    from Member
    inner join Member_Valid_For_Term
    on Member.Email = Member_Valid_For_Term.Email
    where Member_Valid_For_Term.Tcode = "S2024"
    group by Faculty""")
# Students by Gender
cursor.execute("""SELECT Gender, count(*)
    from Member
    inner join Member_Valid_For_Term
    on Member.Email = Member_Valid_For_Term.Email
    where Member_Valid_For_Term.Tcode = "S2024"
    group by Gender
    """)
# Students by Level
cursor.execute("""SELECT coalesce(Level, "Not Assigned") as Assigned_Level, count(*)
    from Member
    inner join Member_Valid_For_Term
    on Member.Email = Member_Valid_For_Term.Email
    where Member_Valid_For_Term.Tcode = "S2024"
    group by Assigned_Level
    """)
# All students
cursor.execute("""SELECT Fname || " " || Lname as Name, Gender, Faculty, Level
    from Member
    inner join Member_Valid_For_Term
    on Member.Email = Member_Valid_For_Term.Email
    where Member_Valid_For_Term.Tcode = "S2024"
    Order by Name
    """)
# Check if email exists
cursor.execute("SELECT count(Email) FROM Member where Email = '%s'")
# Check if password exists
cursor.execute("SELECT count(Email) FROM Account where Password = '%s'")
# Tournament information
cursor.execute("""SELECT distinct Tournament.TorneyName, Tournament.Date, Tournament.StartTime, 
               Tournament.EndTime, Tournament.Location, Tournament.EventId
    From Tournament""")
# Member and team information for a specific tournament
cursor.execute("""SELECT Member.Fname || " " || Member.Lname as Member_Name, Member.Level, Team.TeamName
    From Team
    INNER JOIN Tournament
    ON Team.EventId = Tournament.EventId
    Inner Join Member_Make_Team
    on Member_Make_Team.TeamId = Team.TeamId
    Inner join Member
    on Member.Email = Member_Make_Team.Email
    WHERE Tournament.EventId = '%s'
    """)
# List of sessions
cursor.execute("""select session.EventId, session.Date, Session.StartTime, Session.EndTime, Session.Location, 
               count(Member_Attend_Session.Email) as participant_count, Session_Levels.Level
    from session
    inner join Member_Attend_Session
    on session.EventId = Member_Attend_Session.EventId
    inner join Session_Levels
    on Session_Levels.EventId = Session.EventId
    group by session.EventId
    """)
# Check if student is registered to session
cursor.execute("""select count(*)
    from Member_Attend_Session
    where Member_Attend_Session.Email = '%s' and Member_Attend_Session.EventId = '%s'
    """)


rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
con.close()
