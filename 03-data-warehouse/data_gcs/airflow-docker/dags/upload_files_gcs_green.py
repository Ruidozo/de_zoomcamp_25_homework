from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
import pandas as pd
import requests
from io import BytesIO, StringIO
from datetime import datetime

# Configurações para Green Cab
BUCKET_NAME = "green_cab_bucket_zoomcamp_25_oduir"
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{month:02d}.parquet"

def process_and_upload_to_gcs(month, **kwargs):
    url = URL_TEMPLATE.format(month=month)
    response = requests.get(url)
    response.raise_for_status()

    # Ler o Parquet e converter para CSV
    parquet_file = BytesIO(response.content)
    df = pd.read_parquet(parquet_file)

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    # Upload para o GCS
    gcs_hook = GCSHook(gcp_conn_id='google_cloud_default')
    gcs_hook.upload(
        bucket_name=BUCKET_NAME,
        object_name=f"green_tripdata_2022-{month:02d}.csv",
        data=csv_buffer.getvalue(),
        mime_type='text/csv',
    )

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id="process_green_tripdata",
    default_args=default_args,
    description="Processa e carrega arquivos Green Cab no GCS",
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    for month in range(1, 13):
        process_and_upload_task = PythonOperator(
            task_id=f"process_green_{month:02d}",
            python_callable=process_and_upload_to_gcs,
            op_kwargs={"month": month},
        )
