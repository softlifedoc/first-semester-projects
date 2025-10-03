-- SQL script to insert sample data
INSERT INTO customers (customer_id, name, email, join_date) VALUES
(1, 'Chinwe Okonkwo', 'chinwe.okonkwo@example.com', '2023-01-15'),
(2, 'Adebayo Adeyemi', 'adebayo.adeyemi@example.com', '2023-02-20'),
(3, 'Ngozi Eze', 'ngozi.eze@example.com', '2023-03-10'),
(4, 'Tunde Bello', 'tunde.bello@example.com', '2023-04-05'),
(5, 'Amina Yusuf', 'amina.yusuf@example.com', '2023-05-12');

INSERT INTO products (product_id, product_name, category, price) VALUES
(1, 'Cola', 'Drinks', 1.50),
(2, 'Pounded Yam', 'Food', 2.00),
(3, 'Suya', 'Snacks', 3.50),
(4, 'Akamu', 'Dairy', 2.75),
(5, 'Palm Wine', 'Drinks', 2.25);

INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date) VALUES
(1, 1, 1, 2, '2023-06-01'),
(2, 2, 2, 3, '2023-06-02'),
(3, 1, 3, 1, '2023-06-03'),
(4, 3, 4, 4, '2023-06-04'),
(5, 4, 5, 2, '2023-06-05');

