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

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
con.close()