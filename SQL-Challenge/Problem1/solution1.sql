-- write your solution here
select
(select car from footer_values where car is not null order by id desc limit 1) as a,
(select length from footer_values where length is not null order by id desc limit 1) as b,
(select height from footer_values where height is not null order by id desc limit 1) as d,
(select width from footer_values where width is not null order by id desc limit 1) as c;