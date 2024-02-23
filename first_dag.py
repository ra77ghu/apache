'''from airflow import DAG
from airflow.sensors.external_task import ExternalTaskMarker, ExternalTaskSensor
from airflow.operators.python import PythonOperator
from datetime import datetime


dag = DAG(
    dag_id='master',
    start_date=datetime(2023, 3, 15),
    schedule_interval='@daily'
)
'''


from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.sensors.filesystem import FileSensor
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 20, 12, 24, 0),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'slave_dag',
    default_args=default_args,
    catchup=False,
    schedule_interval=timedelta(hours=1) 
)

#t2= FileSensor(task_id="wait_for_file", filepath="/home/ratnaprakash/Documents/testfile.sh")

t1 = BashOperator(
    task_id='task_1',
    bash_command='echo "Hello from task 1!"',
    dag=dag
)

#t2 >>
t1









