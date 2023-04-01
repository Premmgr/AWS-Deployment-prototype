-- Create the customers table
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  phone_number VARCHAR(20)
);

-- Insert sample customers
INSERT INTO customers (customer_id, first_name, last_name, phone_number)
VALUES
  (1, 'John', 'Doe', '555-1234'),
  (2, 'Jane', 'Smith', '555-5678'),
  (3, 'Bob', 'Johnson', '555-9876');

-- Create the categories table
CREATE TABLE categories (
  category_id INT PRIMARY KEY,
  category_name VARCHAR(50) NOT NULL
);

-- Insert sample categories
INSERT INTO categories (category_id, category_name)
VALUES
  (1, 'Electronics'),
  (2, 'Clothing'),
  (3, 'Home Goods');

-- Create the products table
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(50) NOT NULL,
  category_id INT,
  price DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Insert sample products
INSERT INTO products (product_id, product_name, category_id, price)
VALUES
  (1, 'TV', 1, 799.99),
  (2, 'Shirt', 2, 29.99),
  (3, 'Couch', 3, 599.99),
  (4, 'Laptop', 1, 999.99),
  (5, 'Dress', 2, 49.99),
  (6, 'Chair', 3, 89.99);

-- Create the orders table
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert sample orders
INSERT INTO orders (order_id, customer_id, order_date, total)
VALUES
  (1, 1, '2023-03-30', 1799.98),
  (2, 2, '2023-03-29', 79.98),
  (3, 3, '2023-03-28', 689.97);

-- Create the order_items table
CREATE TABLE order_items (
  order_id INT,
  product_id INT,
  quantity INT NOT NULL,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample order items
INSERT INTO order_items (order_id, product_id, quantity)
VALUES
  (1, 1, 2),
  (1, 4, 1),
  (2, 2, 2),
  (3, 3, 1),
  (3, 6, 4);
