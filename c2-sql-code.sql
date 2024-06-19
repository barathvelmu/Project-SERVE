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