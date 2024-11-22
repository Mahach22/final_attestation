from pyspark.sql import SparkSession
import psycopg2
from clickhouse_connect.driver.client import Client

# Настройки PostgreSQL
# pg_config = {
#     "host": "localhost",
#     "port": 5432,
#     "user": "user",
#     "password": "password",
#     "database": "testdb"
# }

# Настройки ClickHouse
ch_config = {
    "host": "localhost",
    "port": 8123,
    "username": "default",
    "password": "default"
}

# Создание SparkSession
spark = SparkSession.builder \
    .appName("Postgres and ClickHouse Integration").config("spark.jars", "postgresql-42.7.4.jar") \
    .getOrCreate()

# Чтение данных из PostgreSQL
# pg_conn = psycopg2.connect(**pg_config)
# pg_query = "SELECT * FROM test_table"
# pg_df = spark.read.format("jdbc").options(
#     url=f"jdbc:postgresql://{pg_config['host']}:{pg_config['port']}/{pg_config['database']}",
#     dbtable="(SELECT * FROM test_table) as temp_table",
#     user=pg_config['user'],
#     password=pg_config['password'],
#     driver="org.postgresql.Driver"
# ).load()

# Чтение данных из ClickHouse
ch_client = Client(host=ch_config['host'], port=ch_config['port'])
ch_query = "SELECT * FROM test_table"
ch_data = ch_client.query_dataframe(ch_query)

# Конвертация ClickHouse данных в Spark DataFrame
ch_df = spark.createDataFrame(ch_data)

# Объединение данных
# combined_df = pg_df.union(ch_df)

# Вывод объединённых данных
# combined_df.show()

ch_df.show()
# Завершение работы
# pg_conn.close()
ch_client.close()
