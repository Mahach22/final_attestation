**Данный проект создан в рамках выполнения итогового задания № 5**
---
**Задание 5. Создание Docker-контейнера с PostgreSQL и ClickHouse**

Цель: Научиться развертывать базы данных PostgreSQL и ClickHouse в Docker с использованием Docker Compose, создавать таблицы и данные в этих базах данных, а затем использовать PySpark для чтения данных из обеих баз данных и работы с ними в рамках одного DataFrame.

Описание задания: <br>
*	Создайте директорию для проекта и необходимые файлы.
*	Создайте файлы create_tables.sql, которые будут содержать SQL-запросы для создания таблиц и вставки данных в обе базы данных.
*	В docker-compose.yml опишите конфигурацию для развертывания контейнеров с PostgreSQL и ClickHouse.
*	Выполните команду для запуска контейнеров с PostgreSQL и ClickHouse.
*	Создайте файл pyspark_script.py в вашем локальном окружении (вне Docker), который будет подключаться к обеим базам данных и читать данные.
*	Вы должны увидеть вывод данных из обеих баз данных (PostgreSQL и ClickHouse), считанных и обработанных PySpark. <br>

Пример вывода: 
 
<img src="https://github.com/Mahach22/final_attestation/blob/main/5/0.primer.png" width="200" height="400">

Результат задания — после выполнения задания у вас будет Docker-среда, в которой будет 2 базы данных. Используя PySpark, необходимо прочитать данные из обеих БД в рамках одного скрипта.



---

**Выполнение задания:** <br>

Создаем файлы [create_tables.sql для PostgreSQL](https://github.com/Mahach22/final_attestation/blob/main/5/project/postgresql/create_tables.sql) и [create_tables.sql для ClickHouse](https://github.com/Mahach22/final_attestation/blob/main/5/project/clickhouse/create_tables.sql) в своих папках, чтобы не было путаницы. <br>

Создаем [docker-compose.yaml](https://github.com/Mahach22/final_attestation/blob/main/5/project/docker-compose.yaml) для наших контейнеров PostgreSQL и ClickHouse.

Запускаем наши контейнеры командой:
```
docker-compose up -d
```
![compose up](https://github.com/Mahach22/final_attestation/blob/main/5/1.compose-up.png)

Создаем файл [pyspark_script.py](https://github.com/Mahach22/final_attestation/blob/main/5/project/pyspark_script.py) для чтения обеих баз данных. <br>

Также нам потребуется PostgreSQL JDBC, который мы скачаем с официального сайта `https://jdbc.postgresql.org/download/` и поместим рядом с python скриптом. <br>

При отсутствии установим зависимости:
```
pip install pyspark psycopg2 clickhouse-connect
```
Запустим наш python скрипт и увидим, что данные выведены в соответствии с нашим заданием. <br>

![result](https://github.com/Mahach22/final_attestation/blob/main/5/2.result_py_script.png)
