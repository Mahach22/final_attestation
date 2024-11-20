
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

def hello_world():
    print("Hello, world!")

def print_date():
    print("Today is: " + str(datetime.now()))

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 19),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG('final_task8_dag', 
          default_args=default_args, 
          schedule_interval='45 9 * * *')

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=hello_world,
    dag=dag,
)

print_date_task = PythonOperator(
    task_id='print_date_task',
    python_callable=print_date,
    dag=dag,
)

end_task = BashOperator(
    task_id='end_task',
    bash_command='echo End',
    dag=dag,
)

start >> hello_task >> print_date_task >> end_task >> end
