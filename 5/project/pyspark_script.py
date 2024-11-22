from pyspark.sql import SparkSession

# Настройки PostgreSQL
pg_config = {
    "host": "localhost",
    "port": 5432,
    "user": "user",
    "password": "password",
    "database": "testdb"
}

# Настройки ClickHouse
ch_config = {
    "host": "localhost",
    "port": 8123,  # HTTP порт ClickHouse для JDBC
    "username": "default",
    "password": "default",
    "database": "default"
}

# Создание SparkSession
spark = SparkSession.builder \
    .appName("Postgres and ClickHouse Integration") \
    .config("spark.jars", "postgresql-42.7.4.jar,clickhouse-jdbc-0.4.6.jar") \
    .getOrCreate()

# Чтение данных из PostgreSQL
pg_df = spark.read.format("jdbc").options(
    url=f"jdbc:postgresql://{pg_config['host']}:{pg_config['port']}/{pg_config['database']}",
    dbtable="test_table",
    user=pg_config['user'],
    password=pg_config['password'],
    driver="org.postgresql.Driver"
).load()

# Чтение данных из ClickHouse
ch_df = spark.read.format("jdbc").options(
    url=f"jdbc:clickhouse://{ch_config['host']}:{ch_config['port']}/{ch_config['database']}",
    dbtable="test_table",
    user=ch_config['username'],
    password=ch_config['password'],
    driver="com.clickhouse.jdbc.ClickHouseDriver"
).load()

# Вывод данных из PostgreSQL
print("Данные из PostgreSQL:")
pg_df.show()

# Вывод данных из ClickHouse
print("Данные из ClickHouse:")
ch_df.show()

# Завершение работы SparkSession
spark.stop()
