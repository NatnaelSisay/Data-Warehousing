from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta
# import os
# import sys
# sys.path.append('/Users/java/Documents/10Acadamy/week - 11/data-warehouse')
# from my_scripts import database

# figure out a way to avoid ModuleImportError using the above code
import database

def load_data_to_database(**context):
    print("Loading Data To Data Base")
    database.main()
    return

def dbt_transformation(**context):
    print("DBT Transformation")
    
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

with DAG(dag_id='sensors_pipe',
          default_args=DAG_CONFIG,
          catchup=False,
          schedule_interval='@once') as f:
    
    load_data_to_database = PythonOperator(
        task_id='Loading_Data_To_Database',
        python_callable=load_data_to_database,
        provide_context=True
    )

    dbt_transformation = PythonOperator(
        task_id='DBT_Transformation',
        python_callable=dbt_transformation,
        provide_context=True
    )

    


    load_data_to_database >> dbt_transformation 
