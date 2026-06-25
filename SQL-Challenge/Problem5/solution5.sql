-- write your solution here

update job_skills js join 

(with new_data as 
                 (SELECT ROW_ID,
                         JOB_ROLE, 
                         SKILLS, 
                         COUNT(JOB_ROLE) OVER (ORDER BY ROW_ID) AS grouped_count FROM job_skills)

select ROW_ID,
       MAX(JOB_ROLE) OVER(partition by grouped_count) as REV_JOB_ROLE,
       skills from new_data order by ROW_ID
       ) as new_js

on js.ROW_ID = new_js.ROW_ID

set js.JOB_ROLE = new_js.REV_JOB_ROLE where js.JOB_ROLE is null;
       
select * from job_skills js ;



