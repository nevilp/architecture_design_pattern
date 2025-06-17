CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    price INT,
    stock INT

);


ALTER TABLE products REPLICA IDENTITY FULL;