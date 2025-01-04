create database employee15;
use employee15;
create table O_Roll_Call(student_id int, roll_date int, attendance_status varchar(255));
insert into O_Roll_Call values(1,1/4/2003,'y');
insert into O_Roll_Call values(2,24/10/2006,'n');
insert into O_Roll_Call values(3,20/9/2002,'y');
insert into O_Roll_Call values(4,6/8/2001,'y');
insert into O_Roll_Call values(5,28/12/2000,'n');


create table N_Roll_Call(student_id int, roll_date int, attendance_status varchar(255));

select *from O_Roll_Call;
select *from N_Roll_Call;


DELIMITER $$

-- Create a stored procedure to merge data from N_Roll_Call into O_Roll_Call
CREATE PROCEDURE MergeRollCallData()
BEGIN
  DECLARE done INT DEFAULT 0;
  DECLARE studentId INT;
  DECLARE rollDate DATE;
  DECLARE attendanceStatus VARCHAR(255);
  
  -- Declare a cursor for N_Roll_Call
  DECLARE cur CURSOR FOR
    SELECT student_id, roll_date, attendance_status
    FROM N_Roll_Call;
  
  -- Declare handlers for exceptions
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
  
  OPEN cur;
  
  read_loop: LOOP
    FETCH cur INTO studentId, rollDate, attendanceStatus;
    IF done = 1 THEN
      LEAVE read_loop;
    END IF;

    -- Check if the record already exists in O_Roll_Call
    IF NOT EXISTS (
      SELECT 1
      FROM O_Roll_Call
      WHERE student_id = studentId
      AND roll_date = rollDate
    ) THEN
      -- If the record doesn't exist in O_Roll_Call, insert it
      INSERT INTO O_Roll_Call (student_id, roll_date, attendance_status)
      VALUES (studentId, rollDate, attendanceStatus);
    END IF;
  END LOOP;

  CLOSE cur;
END $$

DELIMITER ;
