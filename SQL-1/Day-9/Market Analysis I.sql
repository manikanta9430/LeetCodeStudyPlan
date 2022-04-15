Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id is the primary key of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.

 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the primary key of this table.
item_id is a foreign key to the Items table.
buyer_id and seller_id are foreign keys to the Users table.

 

Table: Items

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
item_id is the primary key of this table.

 

Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.

Return the result table in any order.

The query result format is in the following example.

# Write your MySQL query statement below
select us.user_id as buyer_id, us.join_date as join_date, IFNull(buy.orders_in_2019,0) as orders_in_2019 
	from Users as us left join (select count(orders.item_id) as orders_in_2019, orders.buyer_id as buyer_id from
		(select * from
			Orders where order_date>="2019-01-01" and order_date<="2019-12-31") as orders 
			group by orders.buyer_id) as buy
on us.user_id = buy.buyer_id
