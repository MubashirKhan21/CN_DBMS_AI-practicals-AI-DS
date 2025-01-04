-- Create a new database
CREATE DATABASE Joins;
USE Joins;

-- Create the "departments" table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

-- Insert sample data into the "departments" table
INSERT INTO departments (department_id, department_name) VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Sales'),
(4, 'Finance');

-- Create the "employees" table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    manager_id INT,
    salary DECIMAL(10, 2)
);

-- Insert sample data into the "employees" table
INSERT INTO employees (employee_id, employee_name, department_id, manager_id, salary) VALUES
(1, 'Alice', 1, NULL, 55000.00),
(2, 'Bob', 1, 1, 60000.00),
(3, 'Charlie', 2, NULL, 65000.00),
(4, 'David', 2, 3, 70000.00),
(5, 'Eve', 3, NULL, 60000.00),
(6, 'Frank', 3, 5, 62000.00),
(7, 'Grace', 4, NULL, 70000.00),
(8, 'Hank', 4, 7, 75000.00);

-- Query 1: INNER JOIN
CREATE TEMPORARY TABLE inner_join_result AS
SELECT employees.employee_id, employees.employee_name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;
SELECT * FROM inner_join_result;

-- Query 2: LEFT JOIN
CREATE TEMPORARY TABLE left_join_result AS
SELECT employees.employee_id, employees.employee_name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id;
SELECT * FROM left_join_result;

-- Query 3: RIGHT JOIN
CREATE TEMPORARY TABLE right_join_result AS
SELECT employees.employee_id, employees.employee_name, departments.department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.department_id;
SELECT * FROM right_join_result;

-- Query 4: FULL OUTER JOIN (Using UNION)
CREATE TEMPORARY TABLE full_outer_join_result AS
SELECT employees.employee_id, employees.employee_name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id
UNION
SELECT employees.employee_id, employees.employee_name, departments.department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.department_id;
SELECT * FROM full_outer_join_result;

-- Query 5: SELF JOIN
CREATE TEMPORARY TABLE self_join_result AS
SELECT e1.employee_id AS employee_id1, e1.employee_name AS employee_name1, e2.employee_id AS employee_id2, e2.employee_name AS employee_name2
FROM employees e1
INNER JOIN employees e2 ON e1.manager_id = e2.employee_id
WHERE e1.employee_id <> e2.employee_id;
SELECT * FROM self_join_result;

-- Query 6: CROSS JOIN
CREATE TEMPORARY TABLE cross_join_result AS
SELECT employees.employee_id, employees.employee_name, departments.department_id, departments.department_name
FROM employees
CROSS JOIN departments;
SELECT * FROM cross_join_result;

-- Query 7: Subquery
CREATE TEMPORARY TABLE subquery_result AS
SELECT employees.employee_id, employees.employee_name, employees.salary
FROM employees
WHERE employees.salary > (SELECT AVG(salary) FROM employees AS subquery WHERE subquery.department_id = employees.department_id);
SELECT * FROM subquery_result;


-- Query 8: Subquery with IN
CREATE TEMPORARY TABLE subquery_in_result AS
SELECT employees.employee_id, employees.employee_name, employees.salary
FROM employees
WHERE employees.department_id IN (SELECT department_id FROM employees WHERE salary > 60000);
SELECT * FROM subquery_in_result;

-- Query 9: Subquery with EXISTS
CREATE TEMPORARY TABLE subquery_exists_result AS
SELECT employees.employee_id, employees.employee_name
FROM employees
WHERE EXISTS (SELECT 1 FROM employees AS subquery WHERE subquery.manager_id = employees.employee_id);
SELECT * FROM subquery_exists_result;


-- Query 10: Create a View
CREATE VIEW department_avg_salary AS
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id;


-- Use the view to query the average salary for each department
SELECT * FROM department_avg_salary;
