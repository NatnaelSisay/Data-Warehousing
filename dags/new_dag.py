from airflow import DAG
from airflow.operators.python import PythonOperator, ShortCircuitOperator
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta

def function_one(**context):
    print("Data Extraction")

    # pass A to function2
    context["ti"].xcom_push(key='extraction', value='A')
    return "A"

def function_two(**context):
    print("Data Loading")
    value = context.get('extraction')
    print(f"Data From Extraction : {value}")

    context["ti"].xcom_push(key='load', value='B')
    return "B"

def function_three(**context):
    print("Data Transformation")
    value = context.get('load')
    print(f"Data from Loading : {value}")

    return 

DAG_CONFIG = {
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 1),
    'email': ['natyjava8@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
    'schedule_interval': '0 0/1 0 ? * * *',
}

with DAG(dag_id='new_dag_from_dbt',
          default_args=DAG_CONFIG,
          catchup=False,
          schedule_interval='@once') as f:
    
    data_extraction = PythonOperator(
        task_id='Data_Extraction',
        python_callable=function_one,
        provide_context=True
    )

    data_loading = PythonOperator(
        task_id='Data_Loading',
        python_callable=function_two,
        provide_context=True
    )

    data_transformation = PythonOperator(
        task_id='Data_Transformation',
        python_callable=function_three,
        provide_context=True
    )


    data_extraction >> data_loading >> data_transformation
