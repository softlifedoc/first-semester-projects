-- SQL queries for retrieving insights
SELECT * FROM customers;
SELECT * FROM orders ORDER BY order_date DESC;
SELECT * FROM products WHERE category = 'Drinks';
SELECT COUNT(*) as total_orders FROM orders;
SELECT AVG(price) as avg_price FROM products;
SELECT 
    products.product_id, 
    SUM(products.price * orders.quantity) as revenue 
FROM orders
JOIN products ON orders.product_id = products.product_id
GROUP BY products.product_id;
SELECT orders.order_id, customers.name, products.product_name, orders.quantity, orders.order_date
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id
INNER JOIN products ON orders.product_id = products.product_id;
SELECT customers.name, orders.order_id
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;
SELECT products.product_name, orders.order_id
FROM products
LEFT JOIN orders ON products.product_id = orders.product_id;
