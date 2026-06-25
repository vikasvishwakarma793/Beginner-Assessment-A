-- write your solution here
-- salary + income ctes
with income_data as (select * from salary s cross join income i),

income_amount as (select emp_name,income, base_salary*percentage/100 as amount from income_data),

pivot_income as (select emp_name, 
                                  sum(case 
	                                      when income='Basic'
	                                      then amount
	                                  end) as Basic,
	                                  
	                              sum(case 
	                                      when income='Allowance'
	                                      then amount
	                                  end) as Allowance,
	                                  
	                              sum(case 
	                                      when income='Others'
	                                      then amount
	                                  end) as Others from income_amount group by emp_name),

salary_report as ( select *, (Basic+Allowance+Others) as Gross from pivot_income),



deduction_data as ( select * from salary s cross join deduction d),

deduction_amount as ( select emp_name,deduction,base_salary*percentage/100 as deduction_amount from deduction_data ),

pivot_deduction as (select emp_name,

                                  sum(case 
	                                      when deduction='Insurance'
	                                      then deduction_amount
	                                  end) as Insurance,
	                                  
	                              sum(case 
	                                      when deduction='Health'
	                                      then deduction_amount
	                                  end) as Health,
	                                  
	                              sum(case 
	                                      when deduction='House'
	                                      then deduction_amount
	                                  end) as House from deduction_amount group by emp_name),

deduction_report as ( select *, (Insurance+Health+House) as total_deduction from pivot_deduction)

select sr.emp_name,
       sr.Basic, 
       sr.Allowance, 
       sr.Others, 
       sr.Gross,
       dr.Insurance,
       dr.Health,
       dr.House,
	   dr.total_deduction,
       (sr.gross-dr.total_deduction) as Net_Pay 
	   from salary_report sr join deduction_report dr on sr.emp_name = dr.emp_name order by emp_name;


	                              

	                              




