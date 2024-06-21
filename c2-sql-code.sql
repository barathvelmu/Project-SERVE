CREATE TABLE "Executive" (
	"StdNo"	INTEGER NOT NULL UNIQUE,
	"Fname"	TEXT NOT NULL,
	"Lname"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL UNIQUE,
	"Gender"	TEXT NOT NULL,
	"Faculty"	TEXT NOT NULL,
	PRIMARY KEY("Email")
);

CREATE TABLE "Member" (
	"StdNo"	INTEGER NOT NULL UNIQUE,
	"Fname"	TEXT NOT NULL,
	"Lname"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	"Gender"	TEXT NOT NULL,
	"Faculty"	TEXT NOT NULL,
	"Level"	TEXT,
	"EvaluatorEmail"	TEXT,
	FOREIGN KEY("EvaluatorEmail") REFERENCES "Executive"("Email"),
	PRIMARY KEY("Email")
);

CREATE TABLE "Term" (
	"Tcode"	TEXT NOT NULL,
	"Year"	INTEGER NOT NULL,
	"Season"	TEXT NOT NULL,
	PRIMARY KEY("Tcode")
);

CREATE TABLE "Session" (
	"EventId"	TEXT NOT NULL,
	"Date"	TEXT NOT NULL,
	"StartTime"	TEXT NOT NULL,
	"EndTime"	TEXT NOT NULL,
	"Location"	TEXT NOT NULL,
	"Tcode"	TEXT NOT NULL,
	FOREIGN KEY("Tcode") REFERENCES "Term"("Tcode"),
	PRIMARY KEY("EventId")
);

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
);

CREATE TABLE "Team" (
	"TeamId"	TEXT NOT NULL,
	"TeamName"	TEXT NOT NULL,
	"TeamSize"	INTEGER NOT NULL,
	"EventId"	TEXT NOT NULL,
	FOREIGN KEY("EventId") REFERENCES "Tournament"("EventId"),
	PRIMARY KEY("TeamId")
);

CREATE TABLE "Account" (
	"Password"	TEXT NOT NULL UNIQUE,
	"Email"	TEXT NOT NULL UNIQUE,
	FOREIGN KEY("Email") REFERENCES "Member"("Email"),
	PRIMARY KEY("Password","Email")
);

CREATE TABLE "Member_Valid_For_Term" (
	"Tcode"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	FOREIGN KEY("Email") REFERENCES "Member"("Email"),
	FOREIGN KEY("Tcode") REFERENCES "Term"("Tcode"),
	PRIMARY KEY("Tcode","Email")
);

CREATE TABLE "Executive_Works_For_Term" (
	"Tcode"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	"ExecTeam"	TEXT NOT NULL,
	FOREIGN KEY("Email") REFERENCES "Executive"("Email"),
	FOREIGN KEY("Tcode") REFERENCES "Term"("Tcode"),
	PRIMARY KEY("Tcode","Email")
);

CREATE TABLE "Member_Attend_Session" (
	"Email"	TEXT NOT NULL,
	"EventId"	TEXT NOT NULL,
	FOREIGN KEY("EventId") REFERENCES "Session"("EventId"),
	FOREIGN KEY("Email") REFERENCES "Member"("Email"),
	PRIMARY KEY("Email","EventId")
);

CREATE TABLE "Member-Make-Team" (
	"Email"	TEXT NOT NULL,
	"TeamId"	TEXT NOT NULL,
	FOREIGN KEY("Email") REFERENCES "Member"("Email"),
	FOREIGN KEY("TeamId") REFERENCES "Team"("TeamId"),
	PRIMARY KEY("Email","TeamId")
);

CREATE TABLE "Session_Levels" (
	"EventId"	TEXT NOT NULL,
	"Level"	INTEGER NOT NULL,
	FOREIGN KEY("EventId") REFERENCES "Session"("EventId"),
	PRIMARY KEY("EventId","Level")
);

CREATE TABLE "Tournament_Levels" (
	"EventId"	TEXT NOT NULL,
	"Level"	INTEGER NOT NULL,
	PRIMARY KEY("EventId","Level"),
	FOREIGN KEY("EventId") REFERENCES "Tournament"("EventId")
);