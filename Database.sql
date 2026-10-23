create database shop_db;
use shop_db;

create table product(id int primary key auto_increment,name varchar(50), category varchar(50), price decimal(10,2), quandity int, manufacturer varchar(50));
show tables;
select * from product;