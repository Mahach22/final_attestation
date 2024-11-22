CREATE TABLE test_table (
    id UInt32,
    name String,
    value Int32
) ENGINE = MergeTree()
ORDER BY id;

INSERT INTO test_table VALUES
(1, 'Alice', 100),
(2, 'Bob', 200),
(3, 'Charlie', 300);
