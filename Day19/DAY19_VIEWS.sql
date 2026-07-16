-- VIEWS
-- IT IS A VIRTUAL TABLE WHICH DOESN'T EXIST PHYSICALLY BUT GIVES RESTRICTED VIEW OF TABLE DATA.
-- B.VIEWS MAKE SIMPLE TO WRITE COMPLEX QUERIES BY WRAPPING THEM WITH VIEW NAME WHICH CAN BE REUSED ANY NO.OF TIMES
-- C.IT ENHANCES DATA SECURITY BY SELECTING ANY FEW COLUMNS WHICH DISPLAYS THE TABLE (VIRTUAL) SAME AS THE REAL TABLE
-- D.BUT ALL THE DATA IS BEING PULLED FROM REAL TABLE
-- SYNTAX: TO CREATE VIEWS
-- CREATE VIEW VIEW NAME AS 
--             SELECT COLUMN 1,COLUMN 2...........
--              FROM TABLE_NAME
--              WHERE CONDITION ;(WHERE IS OPTIONAL)
-- DISPLAY ONLY FEW COLUMNS OF CUSTOMERS
create view customers_lite as
select customer_id,name,city from customers;

select*from customers_lite;
-- group the customers on the basis of city whose age is >avg(Age) of city
-- get cutomers of 'mumbai'
select*from customers where city='Mumbai';

create view cities_avg_age as
select c.name,c.city from customers c
where age>(
select avg(age) from customers
where city=c.city
);
select*from cities_avg_age;
-- get monthly revenue of products
create view product_montly_revenue as
select
 monthname(o.order_date )as month ,
 sum(o.total_amount) as revenue 
 from orders o
join order_items oi on o.order_id=oi.order_id
join products p on oi.product_id=oi.product_id
group by monthname(o.order_date); 

-- get customers who doesnt have orders
create view customers_no_orders as
select name,city from customers c
 left join orders o ON c.customer_id=o.customer_id
where o.customer_id IS NULL;
-- modify the view
-- display age,join_date along with name and city
-- syntax: alter view view_name as
--         select query
alter view customers_no_orders as
select c.name,c.city,c.join_date,c.age
from customers c left join orders o 
on c.customer_id=o.customer_id
where o.customer_id IS NULL;
SELECT*FROM CUSTOMERS_NO_ORDERS;
-- DROP THE VIEW
-- SYNTAX: DROP VIEW VIEW_NAME 

DROP VIEW CUSTOMERS_NO_ORDERS;
-- WE CANNNOT UPDATE THE DATA THROUGH VIEWS IF THE VIEW HAS AGGREGATIONS ,JOINS 
-- GET CUSTOMERS FROM MUMBAI 
CREATE VIEW MUMBAI_CUSTOMERS as 
SELECT*FROM CUSTOMERS WHERE CITY='Mumbai';
select*from mumbai_customers;
-- update the age of david
update mumbai_customers
set age=29
where customer_id=4;
select*from mumbai_customers;
insert into mumbai_customers
values(11,'Kiran','Hyderabad',27,'kiran2@gmail.com','2025-07-24');
select*from mumbai_customers;
select*from customers;











