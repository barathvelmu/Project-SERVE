-- Creating Tables
CREATE TABLE "Account" (
	"Password"	TEXT NOT NULL UNIQUE,
	"Email"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("Password","Email")
)
CREATE TABLE "Executive" (
	"StdNo"	INTEGER NOT NULL UNIQUE,
	"Fname"	TEXT NOT NULL,
	"Lname"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL UNIQUE,
	"Gender"	TEXT NOT NULL,
	"Faculty"	TEXT NOT NULL,
	PRIMARY KEY("Email")
)
CREATE TABLE "Executive_For_Term" (
	"Tcode"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	"ExecTeam"	TEXT NOT NULL,
	PRIMARY KEY("Tcode","Email")
)
CREATE TABLE "Member" (
	"StdNo"	INTEGER NOT NULL UNIQUE,
	"Fname"	TEXT NOT NULL,
	"Lname"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	"Gender"	TEXT NOT NULL,
	"Faculty"	TEXT NOT NULL,
	"Level"	TEXT,
	"EvaluatorEmail"	TEXT,
	PRIMARY KEY("Email")
)
CREATE TABLE "Member-Make-Team" (
	"Email"	TEXT NOT NULL,
	"TeamId"	TEXT NOT NULL,
	PRIMARY KEY("Email","TeamId")
)
CREATE TABLE "Member_Attend_Session" (
	"Email"	TEXT NOT NULL,
	"EventId"	TEXT NOT NULL,
	PRIMARY KEY("Email","EventId")
)
CREATE TABLE "Member_Valid_For_Term" (
	"Tcode"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	PRIMARY KEY("Tcode","Email")
)
CREATE TABLE "Session" (
	"EventId"	TEXT NOT NULL,
	"Date"	TEXT NOT NULL,
	"StartTime"	TEXT NOT NULL,
	"EndTime"	TEXT NOT NULL,
	"Location"	TEXT NOT NULL,
	"Tcode"	TEXT NOT NULL,
	PRIMARY KEY("EventId")
)
CREATE TABLE "Session_Levels" (
	"EventId"	TEXT NOT NULL,
	"Level"	INTEGER NOT NULL,
	PRIMARY KEY("EventId","Level")
)
CREATE TABLE "Team" (
	"TeamId"	TEXT NOT NULL,
	"TeamName"	TEXT NOT NULL,
	"TeamSize"	INTEGER NOT NULL,
	"EventId"	TEXT NOT NULL,
	PRIMARY KEY("TeamId")
)
CREATE TABLE "Term" (
	"Tcode"	TEXT NOT NULL,
	"Year"	INTEGER NOT NULL,
	"Season"	TEXT NOT NULL,
	PRIMARY KEY("Tcode")
)
CREATE TABLE "Tournament" (
	"EventId"	TEXT NOT NULL,
	"Date"	TEXT NOT NULL,
	"StartTime"	TEXT NOT NULL,
	"EndTime"	TEXT NOT NULL,
	"Location"	TEXT NOT NULL,
	"Tcode"	TEXT NOT NULL,
	"TorneyName"	TEXT NOT NULL,
	"NumOfTeams"	INTEGER NOT NULL,
	PRIMARY KEY("EventId")
)
CREATE TABLE "Tournament_Levels" (
	"EventId"	TEXT NOT NULL,
	"Level"	INTEGER NOT NULL,
	PRIMARY KEY("EventId","Level")
)

-- Stored Procedures
with CTE as ( -- List of all Duplicate StudentNumber
	select 
		StudentNumber
	from 
		S24_Members
	group by 
		StudentNumber
	having 
		count(*) > 1
), CTE2 as ( -- List of submissions that have a duplicated StudentNumber
	select 
		* 
	from 
		S24_Members
	left join 
		CTE 
	on 
		CTE.StudentNumber = s24_Members.StudentNumber
	where 
		CTE.StudentNumber is not NULL
	order by 
		S24_Members.StudentNumber
), CTE3 as ( -- Get list of StudentNumber with duplicate entries and NO Eval record
	Select 
		StudentNumber
	from 
		CTE2
	group by
		StudentNumber
	HAVING
		sum(case when EvaledLEVEL is not null then 1 else 0 end) = 0
), CTE4 as ( -- Get list of Student Number with duplicate entries
	Select 
		StudentNumber
	from 
		CTE2
	group by
		StudentNumber
	HAVING
		sum(case when EvaledLEVEL is not null then 1 else 0 end) > 0
) SELECT * from S24_Members

-- DELETE FROM S24_Members WHERE StudentNumber in CTE3; (deleting ALL dupes with no eval)
-- DELETE FROM S24_Members WHERE StudentNumber in CTE4 and EvaledLEVEL is Null; (deleting dupes from evaled students, only NON EVALED ENTRIES)