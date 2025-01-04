create database companies;

use companies;
create table emp(empno int, e_name varchar(255),Deptno varchar(255));
insert into emp values(1,'varun','A'),
                      (2,'Amrit','B'),
                      (3,'Ravi','C');
                           
create table EDept(Deptno varchar(255), D_name varchar(255), Location varchar(255));
insert into EDept values('A','IT','Delhi'),
                       ('B','HR','Hydrabad'),
                       ('C','Finance','Pune'),
                       ('D','Testing','Noida');

create table studies1(S_ID int,C_ID varchar(255), sub varchar(255));
insert into studies1 values(1,'A','DBMS'),
						(2,'B','AI'),
                        (1,'B','Python');
                 

select *from emp;

select *from studies1;
select *from EDept;

-- inner join
Select e.empno,e.e_name,d.Location,d.D_name 
FROM emp e inner join Dept d
 ON 
 e.Deptno = d.Deptno;



-- self join
Select T2.S_ID 
FROM studies1 as T1,
studies1 as T2 where T1.S_ID=T2.S_ID and T1.C_ID<>T2.C_ID;



-- left join
Select e.empno,e.e_name,d.D_name 
FROM emp e left join EDept d
 ON 
 e.Deptno = d.Deptno;

 
 -- right join
 
 Select e.empno,e.e_name,d.Location 
FROM emp e right join EDept d
 ON 
 e.Deptno = d.Deptno;

-- Creating View

create view studentdata1
as
select *from EDept;

-- insert values in virtual table

insert into studentdata1 values('E','AI&DS','Wagholi');                      
-- select *from studentdata;


