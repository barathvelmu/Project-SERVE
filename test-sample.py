import sqlite3

con = sqlite3.connect('ProdData/SERVE_PROD.db')
cursor = con.cursor()

# -- Students by Faculty (R6)
cursor.execute("""
SELECT Faculty, count(*)
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
group by Faculty
               """)

# -- Students by Gender (R6)
cursor.execute("""
SELECT Gender, count(*)
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
group by Gender
               """)

# -- Students by Level (R6)
cursor.execute("""
SELECT coalesce(Level, "Not Assigned") as Assigned_Level, count(*)
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
group by Assigned_Level
               """)

# -- All Students (R6)
cursor.execute("""
select Fname || " " || Lname as Name, Gender, Faculty, Level
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
Order by Name
               """)

# -- Insert new member to db (R7)
cursor.execute("""
INSERT INTO Member (StdNo, Fname, Lname, Email, Gender, Faculty, Level, EvaluatorEmail) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", ('20882200', 'Nick', 'Lin', 'nlin@uwaterloo.ca', 'Male', 'Math', 'Level 1', 'd78wong@uwaterloo.ca'))
               
# -- Update new member term (R7)
cursor.execute("""
INSERT INTO Member_Valid_For_Term (Tcode, Email) VALUES (?, ?) 
""", ("S2024", "fwong@uwaterloo.ca"))
               
# -- Update member information (R8)
cursor.execute("""
UPDATE Member SET StdNo = ?, Fname = ?, Lname = ?, Gender = ?, Faculty = ?, Level = ? where Email = ?
""", ('20882222', 'Nick', 'Lin', 'Male', 'Math', 'Level 1', 'd78wong@uwaterloo.ca'))
               
# -- Check if email exists for member (R9)
cursor.execute("""
SELECT count(Email) FROM Member where Email = 'testemail@gmail.com'
               """)
               
# -- Check if email exists for executive (R9)
cursor.execute("""
SELECT count(Email) FROM Executive where Email = 'd78wong@uwaterloo.ca';
               """)
               
# -- Email is not in Acount, add new tuple (R9)
cursor.execute("""
INSERT INTO Account (Password, Email) VALUES ('BBBBBAAAAAAAAAAAAAAA12345', 'testemail@gmail.com');
               """)
               
# -- Email is in Account, update tuple (R9)
cursor.execute("""
UPDATE Account SET Password = 'AAAAAAAAAAAAAAAAAAAA12345' where Email = 'j4noronh@uwaterloo.ca'
               """)
               
# -- Inputted password not in account (R9)
cursor.execute("""
SELECT count(Email) FROM Account where Password = '1234567890QWERTYUIOP09876'
               """)
               
# -- Inputted password in account (R9)
cursor.execute("""
SELECT count(Email) FROM Account where Password = 'BBBBBAAAAAAAAAAAAAAA12345'
               """)
               
# -- Check if email belongs to a current executive (R9)
cursor.execute("""
select count(E.Email) 
from Executive as E
inner join Executive_Works_For_Term as ET 
on E.Email = ET.Email
where ET.Tcode = 'S2024' and E.Email = 'd78wong@uwaterloo.ca'
               """)
               
# -- List of sessions along with details (R10)
cursor.execute("""
with temp_table as (
	select session.EventId, session.Date, Session.StartTime, Session.EndTime, Session.Location, count(Member_Attend_Session.Email) as participant_count
	from session
	left join Member_Attend_Session
	on session.EventId = Member_Attend_Session.EventId
	group by session.EventId
) SELECT temp_table.EventId, temp_table.Date, temp_table.StartTime, temp_table.EndTime, temp_table.Location, temp_table.participant_count, Session_Levels.Level
from temp_table
left join Session_Levels
on temp_table.EventId = Session_Levels.EventId
               """)
               
# -- Check if a student belongs to a session (R10)
cursor.execute("""
select count(*)
from Member_Attend_Session
where Member_Attend_Session.Email = '%s' and Member_Attend_Session.EventId = '%t'
               """)
               
# -- Insert the previously unregistered student into the registered list (R10)
cursor.execute("""
Insert into Member_Attend_Session values('%s', '%s2')
               """)
               
# -- Delete the previously registered student from the registered list (R10)
cursor.execute("""
delete from Member_Attend_Session where Email = '%s' and EventId = '%s2'
               """)
               
# -- Returns information about each tournament (R11)
cursor.execute("""
SELECT distinct Tournament.TorneyName, Tournament.Date, Tournament.StartTime, Tournament.EndTime, Tournament.Location, Tournament.EventId
From Tournament
               """)
               
# -- All teams participating in a tournament (R11)
cursor.execute("""
SELECT Member.Fname || " " || Member.Lname as Member_Name, Member.Level, Team.TeamName
From Team
INNER JOIN Tournament ON Team.EventId = Tournament.EventId
Inner Join Member_Make_Team on Member_Make_Team.TeamId = Team.TeamId
Inner join Member on Member.Email = Member_Make_Team.Email
WHERE Tournament.EventId = 'T0016'
               """)
     
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
con.close()