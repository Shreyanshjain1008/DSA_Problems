# Write your MySQL query statement below
select name as Customers 
From Customers c
Left Join Orders o
on c.id = o.customerId 
where o.customerId is NULL;
