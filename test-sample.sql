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
INSERT INTO Member (StdNo, Fname, Lname, Email, Gender, Faculty, Level, EvaluatorEmail) VALUES (76767676, 'qwert', 'trewq', 'testemail@gmail.com', 'Male', 'Arts', 1, NULL)

-- Update New member term (R7)
INSERT INTO Member_Valid_For_Term (Tcode, Email) values ('S2024', 'testemail@gmail.com')

-- Update member information (R8)
UPDATE Member SET StdNo = 55555566, Fname = 'qwerty', Lname = 'qwerty', Gender = 'F', Faculty = 'Engineering', Level = 1 where email = 'testemail@gmail.com'

-- Check if email exists (R9)
SELECT count(Email) FROM Member where Email = 'testemail@gmail.com'

-- Email is not in Acount, add new tuple (R9)
INSERT INTO Account (Password, Email) VALUES ('BBBBBAAAAAAAAAAAAAAA12345', 'testemail@gmail.com');

-- Email is in Account, update tuple (R9)
UPDATE Account SET Password = 'AAAAAAAAAAAAAAAAAAAA12345' where Email = 'j4noronh@uwaterloo.ca'

-- Inputted password not in account (R9)
SELECT count(Email) FROM Account where Password = '1234567890QWERTYUIOP09876'

-- Inputted password in account (R9)
SELECT count(Email) FROM Account where Password = 'BBBBBAAAAAAAAAAAAAAA12345'