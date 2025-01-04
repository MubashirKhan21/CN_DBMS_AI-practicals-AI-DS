create database office2;
use office2;
create table employee(EID int, FirstName varchar(255), Lastname varchar(255), Dept varchar(255), age int, salary int);
insert into employee values(1,'Sagar','Bahubali','CSE',28,100000),
                           (2,'Virat','Kohli','ENTC',30,150000),
                           (3,'Rohit','Sharma','IT',36,2000000),
                           (4,'Shubhaman','Gill','AI&DS',23,8000000),
                           (5,'Hardik','Pandya','AI&ML',25,1200000);

select *from employee;

-- delete command
delete from employee where FirstName='Sagar';

-- update command
update employee set FirstName='Krunal' where EID=5;

-- alter command
alter table employee add city varchar(20);

update employee set city='pune' where EID=2;
update employee set city='wagholi' where EID=3;
update employee set city='manjari' where EID=4;
update employee set city='lohegaon' where EID=5;

alter table employee drop city;

truncate table employee;
