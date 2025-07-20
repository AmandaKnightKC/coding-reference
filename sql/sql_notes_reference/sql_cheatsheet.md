# SQL Cheat Sheet

This is a visual reference for common SQL commands and syntax.

![SQL Cheat Sheet](SQLcheatsheet.jpg)

> 📍 Located in: `sql/sql_notes_reference/SQLcheatsheet.jpg`

---

## Quick Highlights (Text Reference)

Here are some of the commands featured in the image:

```sql
-- Select all columns
SELECT * FROM table_name;

-- Filter with WHERE
SELECT * FROM employees
WHERE department = 'Sales';

-- Aggregate functions
SELECT department, COUNT(*) FROM employees
GROUP BY department;

-- Sorting
SELECT * FROM products
ORDER BY price DESC;

-- Joins
SELECT orders.id, customers.name
FROM orders
JOIN customers ON orders.customer_id = customers.id;
