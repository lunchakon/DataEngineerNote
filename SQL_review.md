**What is SQL and why is it important in data engineering?**
  RD : Realtional databases managed and altered using the language SQL(Structured Query Language). For the purpose of maintaining, querying, and updating data kept in relational database systems, it is essential in data engineering.

**What is a stored procedure in SQL and its advantages?**
  A collection of SQL statements which may be kept in a database is called a stored procedure. Improved security, less network traffic, and increased performance are among the benefits.

**How do you ensure the security of a SQL database?**
  Security can be ensured by implementing proper access controls, using SSL connections, regular patching of the database software, encrypting sensitive data, and monitoring for unusual access patterns.

**Basic SQL **
Basic SELECT Queries:
<sub>
SELECT * FROM employees;
SELECT first_name, last_name FROM employees;

FIltering Data 
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE hire_date > '2020-01-01';

Sorting Data:
SELECT * FROM employees ORDER BY last_name ASC;
SELECT * FROM employees ORDER BY salary DESC;

Aggregate Functions:
SELECT COUNT(*) FROM employees;
SELECT AVG(salary) FROM employees;
</sub>
Intermediate SQL 
Joins:
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;

SELECT e.first_name, e.last_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;

Group By
SELECT department_id, SUM(salary) AS total_salary
FROM employees
GROUP BY department_id;

SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;

Subqueries:
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

SELECT first_name, last_name
FROM employees
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'Sales');

Advanced SQL Questions
Window Functions:
SELECT first_name, last_name, salary,
       SUM(salary) OVER (ORDER BY salary) AS cumulative_salary
FROM employees;

Rank employees based on their salaries within each department.
SELECT first_name, last_name, department_id, salary,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
FROM employees;

Complex Joins:
Retrieve employees who have not completed any projects (assuming a projects and employee_projects table exist)
SELECT e.first_name, e.last_name
FROM employees e
LEFT JOIN employee_projects ep ON e.employee_id = ep.employee_id
WHERE ep.project_id IS NULL;

Common Table Expressions (CTEs):
Using CTEs to find the hierarchical structure of employees and their managers.
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT employee_id, first_name, last_name, manager_id
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.first_name, e.last_name, e.manager_id
    FROM employees e
    INNER JOIN EmployeeHierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM EmployeeHierarchy;

Practice Projects
Database Design:

Design a database schema for a simple e-commerce platform including tables for users, products, orders, and order_items.
Data Analysis:

Create a set of SQL queries to analyze sales data from an e-commerce database, such as total sales per month, best-selling products, and customer purchase history.

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

