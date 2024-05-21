**What is SQL and why is it important in data engineering?**
  RD : Realtional databases managed and altered using the language SQL(Structured Query Language). For the purpose of maintaining, querying, and updating data kept in relational database systems, it is essential in data engineering.

**What is a stored procedure in SQL and its advantages?**
  A collection of SQL statements which may be kept in a database is called a stored procedure. Improved security, less network traffic, and increased performance are among the benefits.

**How do you ensure the security of a SQL database?**
  Security can be ensured by implementing proper access controls, using SSL connections, regular patching of the database software, encrypting sensitive data, and monitoring for unusual access patterns.

**Basic SQL**

**Basic SELECT Queries:**
```
SELECT * FROM employees;
SELECT first_name, last_name FROM employees;
```

FIltering Data 
```
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE hire_date > '2020-01-01';
```
**Sorting Data:**
```
SELECT * FROM employees ORDER BY last_name ASC;
SELECT * FROM employees ORDER BY salary DESC;
```
**Aggregate Functions:**
```
SELECT COUNT(*) FROM employees;
SELECT AVG(salary) FROM employees;
```
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

1. Users Table

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
2. Products Table

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

3. Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

4. Order Items Table
   
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert data into users table
INSERT INTO users (first_name, last_name, email, password_hash)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'hashed_password_1'),
('Jane', 'Smith', 'jane.smith@example.com', 'hashed_password_2'),
('Alice', 'Johnson', 'alice.johnson@example.com', 'hashed_password_3');

-- Insert data into products table
INSERT INTO products (product_name, description, price, stock_quantity)
VALUES 
('Laptop', 'A high performance laptop', 999.99, 50),
('Smartphone', 'A latest model smartphone', 699.99, 100),
('Headphones', 'Noise cancelling headphones', 199.99, 200);

-- Insert data into orders table
INSERT INTO orders (user_id, total_amount, status)
VALUES 
(1, 1199.98, 'Pending'),
(2, 199.99, 'Shipped'),
(3, 999.99, 'Delivered');

-- Insert data into order_items table
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES 
(1, 1, 1, 999.99),
(1, 3, 1, 199.99),
(2, 3, 1, 199.99),
(3, 1, 1, 999.99);



Exmaple : join orders an order imtems 
SELECT 
    o.order_id,
    o.user_id,
    u.first_name,
    u.last_name,
    o.total_amount,
    o.status,
    oi.product_id,
    p.product_name,
    oi.quantity,
    oi.price
FROM orders o
JOIN users u ON o.user_id = u.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;

Advanced SQL Questions

Find the total amount spent by each user.
SELECT u.user_id, u.first_name, u.last_name, SUM(o.total_amount) AS total_spent
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, u.first_name, u.last_name
ORDER BY total_spent DESC;

Find the most popular product (the product with the highest quantity sold).
SELECT p.product_id, p.product_name, SUM(oi.quantity) AS total_quantity_sold
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 1;

List users who have placed more than one order.
SELECT u.user_id, u.first_name, u.last_name, COUNT(o.order_id) AS order_count
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, u.first_name, u.last_name
HAVING order_count > 1
ORDER BY order_count DESC;

Get the average order amount per user.
SELECT u.user_id, u.first_name, u.last_name, AVG(o.total_amount) AS average_order_amount
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, u.first_name, u.last_name;

Using CTEs on the Database

Example 1: Using CTE to Calculate Total Spent by Each User
WITH UserTotalSpent AS (
    SELECT 
        u.user_id, 
        u.first_name, 
        u.last_name, 
        SUM(o.total_amount) AS total_spent
    FROM 
        users u
    JOIN 
        orders o ON u.user_id = o.user_id
    GROUP BY 
        u.user_id, u.first_name, u.last_name
)
SELECT * FROM UserTotalSpent
ORDER BY total_spent DESC;

The CTE UserTotalSpent calculates the total amount spent by each user and then selects all columns from this CTE, ordering the results by the total spent in descending order.

Example 2: Using CTE to Find Most Popular Product
WITH ProductSales AS (
    SELECT 
        p.product_id, 
        p.product_name, 
        SUM(oi.quantity) AS total_quantity_sold
    FROM 
        products p
    JOIN 
        order_items oi ON p.product_id = oi.product_id
    GROUP BY 
        p.product_id, p.product_name
)
SELECT * FROM ProductSales
ORDER BY total_quantity_sold DESC
LIMIT 1;

The CTE ProductSales calculates the total quantity sold for each product. The main query then selects from this CTE, ordering by total quantity sold and limiting the result to the top product.

Example 3: Using CTE to List Users with Multiple Orders
WITH UserOrderCount AS (
    SELECT 
        u.user_id, 
        u.first_name, 
        u.last_name, 
        COUNT(o.order_id) AS order_count
    FROM 
        users u
    JOIN 
        orders o ON u.user_id = o.user_id
    GROUP BY 
        u.user_id, u.first_name, u.last_name
)
SELECT * FROM UserOrderCount
WHERE order_count > 1
ORDER BY order_count DESC;

The CTE UserOrderCount calculates the number of orders placed by each user. The main query selects users who have placed more than one order and orders the results by the number of orders in descending order.

