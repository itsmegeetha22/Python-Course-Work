
use join_pfs53;
-- SUB QUERY
-- A SUB QUERY IS A QUERY WRITTEN INSIDE ANOTHER QUERY IS USED BY THE OUTER QUERY EITHER TO COMPARE OR AGGREAGATE OR REFLECT THE CALCULATED COLUMNS.
-- EVEN MORE USED FOR COMPARISION OF DATA BASED ON AGGREAGATION FUNCTIONS

-- WHY SUB QUERY?
-- TO REFLECT THE DATA FROM MULTIPLE TABLE WE HAVE JOINS,BUT IN CASE OF JOINS WE MIGHT GET DUPLICATE DATA SOMETIMES,
-- IN CASE FILTERING(CONDITIONS)
-- IN  CASE SUBQUERY THE GROUP BY WILL BE COLLAPSED BY EITHER RETURNING THE PARTICULAR DATA EITHER FOR COMPARISION OR REFLECTING AS COLUMN
-- TYPES OF SUB QUERIES:
-- ---------------------
-- SCALAR(SINGLE VALUE)
-- COLUMN(IT GIVES ONE COLUMN)
-- ROW(IT GIVES ONE ROW)
-- TABLE(IT GIVES MULTIPLE ROWS)
-- SOME(IT CHECKS ATLEAST ONE OR MORE)
-- ANY(WORKS LIKE OR(SPECIALLY USED FOR LARGE DATA SETS))
-- ALL(IT CHECKS WITH EVERY VALUE)
-- EXISTS(IT WORKS LIKE CONDITION)
-- NOTEXISTS(NEGOTION OF EXISTS)
-- NESTED(QUERY INSIDE SUBQUERY)
-- CORRELATED(USERS THE OUTER QUERY IN THE SUBQUERY)





-- Find customers older than the average customer age. ( average means calculated value)
select*from customers;
select avg(age) from customers;
select*From customers where age>29;
-- scalar subquery- the query which depends on subquery single value
select*from customers where age>
(
select avg(age) from customers);
-- Find products from categories containing expensive products (price > 1000).
-- find the cateogry where electronics ad fashion where price>1000
-- note1: this query depends category which is a column so it is column subquery.
-- note2:in quetion the category whether it has expensive product or not (atleast one)
select*from products where category IN ('Electronics','Fashion') and price>1000;
select*from products
where category in(select distinct category from products where price>1000);
-- Find customers who placed orders above 1000.
select c.customer_id,c.name from customers c
join orders o on c.customer_id=o.customer_id
where total_amount>1000;
-- get the customers where customer_id are 1,2,4
select c.customer_id ,c.name from customers c where customer_id in(1,2,4);
select c.customer_id,c.name from customers c
where c.customer_id in(select customer_id from orders  where orders.total_amount >1000);
-- note:this subquery depends on different table so it is table subquery
-- Display customers and their total order count.
-- note: select (expression) sub query 
select customer_id,name,
(select count(*) from orders o where o.customer_id=c.customer_id) as total_orders
 from customers c;
-- find the products cheaper than electornics 
--  select * from products where price < SOME ELECTRONICS(Laptop,MOUSE,);
select product_name ,price from products where price < SOME (
select price from products where category='Electronics');
-- some: it is ike any one value,it compares a value with list of other values in the sub query list, if the comparision is true for atleast one value ,it is enough
-- SOME IS AN OPERATOR
-- IT IS SAME AS OR OPERATOR
-- WHY TO USE SOME?
-- FOR LARGE DATA SETS WE COMPARE THE DATA ,SOME OPERATOR REDUCES TIME 
-- 
-- Products Cheaper than SOME FASHION
select product_name ,price,category from products where price < SOME (
select price from products where category='Fashion');
-- select product_name ,price from products where price < SOME (
-- select price from products where category='Electronics');
-- Customers who placed orders more expensive than SOME Average spenders.
-- customers who have orders (no duplicates)
select c.customer_id,c.name from customers c join orders o on c.customer_id=o.customer_id group by c.customer_id,c.name;
-- avg order  amount of customers
select customer_id,avg(total_amount) from orders group by customer_id;

select c.customer_id, c.name from customers c
join orders o
on c.customer_id=o.customer_id 
group by c.customer_id,c.name 
having SUM(o.total_amount)>SOME(
                             select avg(total_amount)
                             from orders
                             group by customer_id); 
 
-- Find products whose price is greater than ANY/ALL Electronics product prices.
-- ANY: COMPARES A VALUE AGAINST AT LEAST ONE VALUE RETURNED BY THE SUBQUERY
-- ALL: COMPARES A VALUE AGAINST EVERY VALUE RETURNED BY THE SUBQUERY(LOPP OF VALUES)
-- DESCRIPTION: ANY/ALL WORKS LIKE COMPARISION OPEARTOR JUST LIKE SOME
-- Find customers who have placed orders.
-- customers and orders
-- customers id is present in orders 
-- join 
select c.customer_id,c.name,o.order_id,o.total_amount from customers c
join orders o ON c.customer_id=o.customer_id;
-- find customers with id 1,2,3,4
select *from customers where customer_id IN(1,2,3,4);
-- exists: it is a keyword which checks the given value in the list
--         it works like in operator but used for large data sets
select name,city from customers
where EXISTS (
select o.customer_id from orders o where o.customer_id=customers.customer_id);
-- Find customers who have not placed any orders.
select name,city from customers
where  NOT EXISTS (
select o.customer_id from orders o where o.customer_id=customers.customer_id);
-- Find customers who placed orders above the average order amount.
-- A) GET AVG OF ORDERS TOTAL_AMOUNT
-- B) GET CUSTOMERS WHO PLACED ORDERS
select avg(total_amount) from orders;
select name,city from customers 
where exists (
select * from orders o 
where o.customer_id=customers.customer_id);
-- get orders greater than amount 13000 or >avg of orders amount
select*from orders where total_amount>13000;
-- get customers whose orders greater than 13000
select name,city from customers
where exists(
select*from orders o 
where o.customer_id=customers.customer_id and total_amount>13000);
select name,city from customers
where exists(
select*from orders o 
where o.customer_id=customers.customer_id and total_amount>(select avg(total_amount) from orders)
);
-- Find customers older than the average age of their city.
-- get avg of city 'mumbai'
select avg(age) from customers where city='Mumbai';
-- get avg age
select city,avg(age) from customers
group by city;
-- get customers who are greater than  31 from city 'mumbai'
select*from customers where city='Mumbai' and age>31;
-- self join connect city of outside table to inside table
select *from customers c where age>(
select avg(age) from customers c where c.city=c.city);
