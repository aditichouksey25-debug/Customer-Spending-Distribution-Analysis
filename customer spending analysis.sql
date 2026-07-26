select * from public."online retail";
select count(*) from public."online retail";
alter table public."online retail"
add column transaction_amount double precision;
update public."online retail"
set transaction_amount = "Quantity" * "UnitPrice";
select transaction_amount 
from public."online retail"
limit 5;
select * from public."online retail";
select round(avg("transaction_amount"):: numeric,2) as mean
from public."online retail";
select max(transaction_amount) as max_amount
from public."online retail";
select min(transaction_amount) as min_amount
from public."online retail";
select round(stddev("transaction_amount"):: numeric,2) as std_dev
from public."online retail";
select *, round(((transaction_amount-avg(transaction_amount)over())
/stddev(transaction_amount)over()):: numeric,2)as z_score
from public."online retail";
with z_score as (select *,(transaction_amount-avg(transaction_amount)over())
/stddev(transaction_amount)over() as z_score
from public."online retail")
select count (*) as outliers 
from z_score
where abs(z_score)>3;
with z_score as (select *,(transaction_amount-avg(transaction_amount)over())
/stddev(transaction_amount)over() as z_score
from public."online retail")
select count (*) as outliers ,
round(count(*)*100.0/(select count(*) from public."online retail"),2)
as outlier_percentage
from z_score
where abs (z_score)>3;