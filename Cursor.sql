-- Create a new database
CREATE DATABASE yesDatabase;
USE yesDatabase;

-- Create the N_Roll_Call and O_Roll_Call tables
CREATE TABLE N_Roll_Call (
    roll_id INT PRIMARY KEY,
    roll_no VARCHAR(255),
    name VARCHAR(255),
    year INT
);

CREATE TABLE O_Roll_Call (
    roll_id INT PRIMARY KEY,
    roll_no VARCHAR(255),
    name VARCHAR(255),
    year INT
);

-- Insert random data for at least 5 people into N_Roll_Call
INSERT INTO N_Roll_Call (roll_id, roll_no, name, year)
VALUES
    (1, 'N001', 'John Smith', 2020),
    (2, 'N002', 'Alice Johnson', 2021),
    (3, 'N003', 'Bob Williams', 2019),
    (4, 'N004', 'Sarah Davis', 2022),
    (5, 'N005', 'Michael Brown', 2018);

-- Insert random data for at least 5 people into O_Roll_Call
INSERT INTO O_Roll_Call (roll_id, roll_no, name, year)
VALUES
    (2, 'O001', 'Alice Johnson', 2021),
    (4, 'O002', 'Sarah Davis', 2022),
    (6, 'O003', 'Alex Martin', 2017),
    (8, 'O004', 'Linda Wilson', 2023),
    (10, 'O005', 'George Lee', 2020);

-- Define the n_roll_id value you want to merge
SET @n_roll_id = 3; -- Replace with a valid n_roll_id value

-- Check if the data already exists in O_Roll_Call
SELECT roll_id INTO @v_n_roll_id
FROM O_Roll_Call
WHERE roll_id = @n_roll_id;

-- Check if the data doesn't exist and insert it into O_Roll_Call
INSERT INTO O_Roll_Call (roll_id, roll_no, name, year)
SELECT N.roll_id, N.roll_no, N.name, N.year
FROM N_Roll_Call N
WHERE N.roll_id = @n_roll_id
AND @v_n_roll_id IS NULL;

-- Select a message indicating the result
SELECT 
    CASE
        WHEN @v_n_roll_id IS NULL THEN 'Data merged successfully.'
        ELSE 'Data already exists in O_Roll_Call. Skipping.'
    END AS message;
