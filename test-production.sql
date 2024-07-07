-- Students by Faculty (R6)
SELECT Faculty, count(*)
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
group by Faculty

-- Students by Gender (R6)
SELECT Gender, count(*)
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
group by Gender

-- Students by Level (R6)
SELECT coalesce(Level, "Not Assigned") as Assigned_Level, count(*)
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
group by Assigned_Level

-- All Students (R6)
select Fname || " " || Lname as Name, Gender, Faculty, Level
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
Order by Name

-- Insert new member to db (R7)
INSERT INTO Member (StdNo, Fname, Lname, Email, Gender, Faculty, Level, EvaluatorEmail) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', NULL) % 
(student_id, firstname, lastname, str(email), gender, faculty, level_of_play)

-- Update new member term (R7)
INSERT INTO Member_Valid_For_Term (Tcode, Email) values ('%s', '%s') % ("S2024", str(email))

-- Update member information (R8)
UPDATE Member SET StdNo = ?, Fname = ?, Lname = ?, Gender = ?, Faculty = ?, Level = ? where Email = ?, (student_id, firstname, lastname, gender, faculty, level_of_play, email)

-- Check if email exists for member (R9)
SELECT count(Email) FROM Member where Email = 'testemail@gmail.com'

-- Check if email exists for executive (R9)
SELECT count(Email) FROM Executive where Email = '%s';

-- Email is not in Acount, add new tuple (R9)
INSERT INTO Account (Password, Email) VALUES ('BBBBBAAAAAAAAAAAAAAA12345', 'testemail@gmail.com');

-- Email is in Account, update tuple (R9)
UPDATE Account SET Password = 'AAAAAAAAAAAAAAAAAAAA12345' where Email = 'j4noronh@uwaterloo.ca'

-- Inputted password not in account (R9)
SELECT count(Email) FROM Account where Password = '1234567890QWERTYUIOP09876'

-- Inputted password in account (R9)
SELECT count(Email) FROM Account where Password = 'BBBBBAAAAAAAAAAAAAAA12345'

-- Check if email belongs to a current executive (R9)
select count(E.Email) 
from Executive as E
inner join Executive_Works_For_Term as ET 
on E.Email = ET.Email
where ET.Tcode = 'S2024' and E.Email = '%s'

-- List of sessions along with details (R10)
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

-- Check if a student belongs to a session (R10)
select count(*)
from Member_Attend_Session
where Member_Attend_Session.Email = '%s' and Member_Attend_Session.EventId = '%t'

-- Insert the previously unregistered student into the registered list (R10)
Insert into Member_Attend_Session values('%s', '%s2')

-- Delete the previously registered student from the registered list (R10)
delete from Member_Attend_Session where Email = '%s' and EventId = '%s2'

-- Returns information about each tournament (R11)
SELECT distinct Tournament.TorneyName, Tournament.Date, Tournament.StartTime, Tournament.EndTime, Tournament.Location, Tournament.EventId
From Tournament

-- All teams participating in a tournament (R11)
SELECT Member.Fname || " " || Member.Lname as Member_Name, Member.Level, Team.TeamName
From Team
INNER JOIN Tournament ON Team.EventId = Tournament.EventId
Inner Join Member_Make_Team on Member_Make_Team.TeamId = Team.TeamId
Inner join Member on Member.Email = Member_Make_Team.Email
WHERE Tournament.EventId = '%s'

