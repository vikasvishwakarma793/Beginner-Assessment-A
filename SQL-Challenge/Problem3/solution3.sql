-- write your solution here
-- without first marks
with new as ( select *,lag(marks) over(order by test_id) as previous_marks from student_marks)
select test_id,marks from new where marks > previous_marks;

-- with first marks comparing with 0 , using coalesce-- it will make null to default we set

with new1 as ( select *,coalesce(lag(marks) over(order by test_id),0) as previous_marks from student_marks)
select test_id,marks from new1 where marks > previous_marks;
-- or simple add on in where condition
with new2 as ( select *,lag(marks) over(order by test_id) as previous_marks from student_marks)
select test_id,marks from new2 where marks > previous_marks or previous_marks is null;

