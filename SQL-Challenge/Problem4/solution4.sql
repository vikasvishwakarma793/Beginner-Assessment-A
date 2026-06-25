-- write your solution here

select product_id,
       day_indicator,
       dates 
       from day_indicator 
       where substring(day_indicator,weekday(dates)+1,1) ='1';
