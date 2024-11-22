from pyspark.sql import SparkSession
import psycopg2
from clickhouse_driver import Client

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
    "port": 9000,
    "username": "default",
    "password": "default"
}

# Создание SparkSession
spark = SparkSession.builder \
    .appName("Postgres and ClickHouse Integration").config("spark.jars", "postgresql-42.7.4.jar") \
    .getOrCreate()

# Чтение данных из PostgreSQL
pg_conn = psycopg2.connect(**pg_config)
pg_query = "SELECT * FROM test_table"
pg_df = spark.read.format("jdbc").options(
    url=f"jdbc:postgresql://{pg_config['host']}:{pg_config['port']}/{pg_config['database']}",
    dbtable="(SELECT * FROM test_table) as temp_table",
    user=pg_config['user'],
    password=pg_config['password'],
    driver="org.postgresql.Driver"
).load()

# Чтение данных из ClickHouse
ch_client = Client(host=ch_config['host'], port=ch_config['port'], user=ch_config['username'], password=ch_config['password'])
ch_query = "SELECT * FROM test_table"
ch_data = ch_client.query_dataframe(ch_query)

# Конвертация ClickHouse данных в Spark DataFrame
ch_df = spark.createDataFrame(ch_data)

#вывод объединённых данных
print("Данные из PostgreSQL:")
pg_df.show()
print("Данные из ClickHouse:")
ch_df.show()

# завершение работы
spark.stop()