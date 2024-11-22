CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    salary INTEGER
);

INSERT INTO test_table (id, name, age, salary) VALUES
(1, 'Мурад', 23, 87000),
(2, 'Залина', 21, 300000),
(3, 'Рустам', 29, 64000),
(4, 'Фатима', 26, 212000),
(5, 'Тимур', 31, 53000),
(6, 'Амина', 25, 270000),
(7, 'Магомед', 34, 110000),
(8, 'Лейла', 28, 295000),
(9, 'Заур', 27, 125000),
(10, 'Ася', 22, 152000);
