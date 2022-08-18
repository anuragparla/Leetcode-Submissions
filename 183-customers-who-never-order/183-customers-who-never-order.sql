# Write your MySQL query statement below
SELECT name as Customers from customers 
WHERE id not in (
    SELECT customerId from orders
);