-- Select All from Member Table
SELECT * FROM Member

-- Gender Count
SELECT Gender, count(*) from Member group by Gender

-- Faculty Count
SELECT Faculty, count(*) from Member group by Faculty

-- Level Count
SELECT Level, count(*) from Member group by Level

-- Level by Faculty Count
SELECT Level, Faculty, count(*) from Member group by Faculty, Level

-- Evaluator Count
SELECT EvaluatorEmail, count(*) from Member group by EvaluatorEmail

-- Students by Faculty
SELECT Faculty, count(*)
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
group by Faculty

-- Students by Gender
SELECT Gender, count(*)
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
group by Gender

-- Students by Level
SELECT coalesce(Level, "Not Assigned") as Assigned_Level, count(*)
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
group by Assigned_Level

-- All Students
select Fname || " " || Lname as Name, Gender, Faculty, Level
from Member
inner join Member_Valid_For_Term
on Member.Email = Member_Valid_For_Term.Email
where Member_Valid_For_Term.Tcode = "S2024"
Order by Name

-- Check if email exists
SELECT count(Email) FROM Member where Email = '%s'


-- con.execute("INSERT INTO S24_Members (Email, Name, Firstname, StudentNumber, Gender, YearofStudy, Faculty, LevelofPlay, OttawaVNLTripInterest, Completiontime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, strftime('%m/%d/%Y', 'now'))", 
--             (email, full_name, firstname, student_id, gender, faculty, level_of_play))
-- SELECT count(Email) FROM Password where Email = '%s'
-- "UPDATE Password SET code = '%s' WHERE Email = '%s'"%(password, email)
-- con.execute("INSERT INTO Password (Email, Code) VALUES ('%s', '%s')" % (email,password))
