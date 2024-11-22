CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    value INTEGER
);

INSERT INTO test_table (name, value) VALUES
('Alice', 10),
('Bob', 20),
('Charlie', 30);
