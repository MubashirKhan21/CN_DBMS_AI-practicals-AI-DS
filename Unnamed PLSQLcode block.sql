-- Create a new database
CREATE DATABASE BookDatabase;
USE BookDatabase;

-- Create the Borrower table
CREATE TABLE Borrower (
    Roll_no INT PRIMARY KEY,
    Name VARCHAR(255),
    Date_of_Issue DATE,
    Name_of_Book VARCHAR(255),
    Status CHAR(1)
);

-- Create the Fine table
CREATE TABLE Fine (
    Roll_no INT,
    Date DATE,
    Amt DECIMAL(10, 2)
);

-- Insert random data into the Borrower table
INSERT INTO Borrower (Roll_no, Name, Date_of_Issue, Name_of_Book, Status)
VALUES
    (1, 'John Doe', '2023-10-01', 'Book 1', 'I'),
    (2, 'Jane Smith', '2023-10-15', 'Book 2', 'I'),
    (3, 'Alice Johnson', '2023-09-01', 'Book 3', 'I'),
    (4, 'Bob Williams', '2023-09-15', 'Book 4', 'I'),
    (5, 'Eve Davis', '2023-08-01', 'Book 5', 'I');

-- Example: Adjusted input values for testing
SET @input_roll_no = 4; -- Replace with the actual Roll_no value for testing
SET @input_book_name = 'Book 4'; -- Replace with the actual book name for testing

-- Check the number of days from Date_of_Issue
SELECT Date_of_Issue INTO @issue_date
FROM Borrower
WHERE Roll_no = @input_roll_no AND Name_of_Book = @input_book_name;

SET @current_date = CURDATE();
SET @days_diff = DATEDIFF(@current_date, @issue_date);

-- Calculate the fine amount using the CASE statement
SET @fine_amt = 
    CASE
        WHEN @days_diff BETWEEN 15 AND 30 THEN @days_diff * 5
        WHEN @days_diff > 30 THEN @days_diff * 50
        ELSE 0
    END;

-- Update the Status in Borrower table
UPDATE Borrower
SET Status = 'R'
WHERE Roll_no = @input_roll_no AND Name_of_Book = @input_book_name;

-- Insert fine details into the Fine table if fine condition is true
INSERT INTO Fine (Roll_no, Date, Amt)
SELECT @input_roll_no, @current_date, @fine_amt
WHERE @fine_amt > 0;

-- Display the Fine table
SELECT * FROM Fine;
