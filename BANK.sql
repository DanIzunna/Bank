use bank;
select * from customers;
-- CREATE table CUSTOMERS (ID_NO INT primary KEY auto_increment, FIRST_NAME VARCHAR(64) NOT NULL, 
-- LAST_NAME VARCHAR(64) NOT NULL, DATE_OF_BIRTH DATE not null, GENDER varchar(1) NOT NULL, PIN VARCHAR(64) NOT NULL,
-- ACCOUNT_NUMBER INT NOT NULL, ACCOUNT_TYPE VARCHAR(64) NOT NULL,  BALANCE float, CURRENCY VARCHAR(3), DATE_CREATED date NOT NULL);

-- drop table customers;
-- DELETE FROM customers WHERE (ID_NO between 21 and 50 );

-- select * from customers where account_number = 272261537 and pin = 'cbfad02f9ed2a8d1e08d8f74f5303e9eb93637d47f82ab6f1c15871cf8dd0481';
-- DELETE FROM customers WHERE account_number = 272261537 and pin =  'cbfad02f9ed2a8d1e08d8f74f5303e9eb93637d47f82ab6f1c15871cf8dd0481'