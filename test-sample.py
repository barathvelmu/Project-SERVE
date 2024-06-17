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

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
con.close()

