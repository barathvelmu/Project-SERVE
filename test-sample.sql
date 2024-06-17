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

-- con.execute("INSERT INTO S24_Members (Email, Name, Firstname, StudentNumber, Gender, YearofStudy, Faculty, LevelofPlay, OttawaVNLTripInterest, Completiontime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, strftime('%m/%d/%Y', 'now'))", 
--             (email, full_name, firstname, student_id, gender, year_of_study, faculty, level_of_play, ottawa_trip_interest))
-- SELECT count(Email) FROM Password where Email = '%s'
-- "UPDATE Password SET code = '%s' WHERE Email = '%s'"%(password, email)
-- con.execute("INSERT INTO Password (Email, Code) VALUES ('%s', '%s')" % (email,password))