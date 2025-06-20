from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Example tenants
TENANTS = ['tenant_a', 'tenant_b', 'tenant_c']

def extract(tenant, **kwargs):
    print(f"[{tenant}] Extracting data...")

def transform(tenant, **kwargs):
    print(f"[{tenant}] Transforming data...")

def load(tenant, **kwargs):
    print(f"[{tenant}] Loading data into DB...")

default_args = {
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG('multi_tenant_etl_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    for tenant in TENANTS:
        extract_task = PythonOperator(
            task_id=f'extract_{tenant}',
            python_callable=extract,
            op_kwargs={'tenant': tenant}
        )

        transform_task = PythonOperator(
            task_id=f'transform_{tenant}',
            python_callable=transform,
            op_kwargs={'tenant': tenant}
        )

        load_task = PythonOperator(
            task_id=f'load_{tenant}',
            python_callable=load,
            op_kwargs={'tenant': tenant}
        )

        extract_task >> transform_task >> load_task
