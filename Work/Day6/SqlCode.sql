SET SERVEROUTPUT ON

begin
DBMS_OUTPUT.PUT_LINE('Hello World!');
END;

DECLARE
v_message varchar2(30) := 'Hello World!';
BEGIN
DBMS_OUTPUT.PUT_LINE(v_message);
END;


DECLARE
A INTEGER := 10;
B INTEGER :=20;
C INTEGER ;
BEGIN
C := A+B;
DBMS_OUTPUT.PUT_LINE('The value of C is : ' || C);
END;


DECLARE
a INTEGER := 101;
BEGIN
IF(a < 100) THEN
dbms_output.put_line('The value of a is less than 100');
ELSE
dbms_output.put_line('The value of a is greater than 100');

END IF;
dbms_output.put_line('The value of a is :' || a);

end;

DECLARE
grade char(1):= 'C';
begin
case grade
when 'A' then dbms_output.put_line('The letter is A');
when 'B' then dbms_output.put_line('The letter is B');
else dbms_output.put_line('Sorry the case didnt match anywhere');
END CASE;
END;

create table product(pid number(5) , pname varchar2(30) , quantity number(10));
insert into product values(1 , 'Choclate' , 10);
DECLARE
product_id number := &var;
product_name varchar2(30);
BEGIN
select pname into product_name from product where pid = product_id;
dbms_output.put_line('The product name is : ' || product_name);
END;


begin
for j in 1..10 loop
dbms_output.put_line(j);
end loop;
end;

insert into product values(2 , 'Laptop' , 100);

create table shop(shop_id number(5) , shop_name varchar2(20));

insert into shop values(1 , 'Pizza');

create or replace procedure myproc(id in number ,  shopname in varchar2)
is begin
insert into shop values (id , shopname);
end;

begin
myproc(101 , 'Pizza');
dbms_output.put_line('The values instered successfully');
end;

select * from shop;

drop procedure myproc ;

create or replace procedure myproc(shopid in number , shopname in varchar2 )
is begin
insert into shop values (shopid , shopname);
end;

declare
shop_id number :=&var;
shopname varchar2 :=&var;
begin
myproc(shop_id , shopname);
end;

create or replace procedure testproc as
begin
dbms_output.put_line('Test procedure called');
end;

begin
testproc;
end;

execute testproc;

create or replace function addnum(num1 in number  , num2 in number )
return number
is num3 number(10);
begin
num3 := num1 + num2 ;
return num3;
end;

declare
num3 number(10);
begin
num3 := addnum(6,10);
dbms_output.put_line('The sum of the numbers is : ' || num3);
end;

drop function addnum;
