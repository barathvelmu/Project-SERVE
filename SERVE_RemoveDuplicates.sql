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

