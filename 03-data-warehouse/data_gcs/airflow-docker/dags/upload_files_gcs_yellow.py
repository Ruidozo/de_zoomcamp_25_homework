import pandas as pd
import requests
from io import BytesIO, StringIO
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from datetime import datetime

# Configurations
BUCKET_NAME = "yellow_cab_bucket_zoomcamp_25_oduir"
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-{month:02d}.parquet"
CHUNK_SIZE = 100000  # Number of rows per chunk

# Expected schema for validation
EXPECTED_COLUMNS = [
    "VendorID", "tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count",
    "trip_distance", "RatecodeID", "store_and_fwd_flag", "PULocationID", "DOLocationID",
    "payment_type", "fare_amount", "extra", "mta_tax", "tip_amount", "tolls_amount",
    "improvement_surcharge", "total_amount", "congestion_surcharge"
]

def process_and_upload_to_gcs_in_chunks(month, **kwargs):
    # Download the Parquet file from the URL
    url = URL_TEMPLATE.format(month=month)
    response = requests.get(url)
    response.raise_for_status()
    parquet_file = BytesIO(response.content)

    # Load Parquet file into a DataFrame
    df = pd.read_parquet(parquet_file, engine="fastparquet")

    # Validate and align schema
    missing_columns = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing columns in the dataset: {missing_columns}")

    # Ensure column order matches the schema
    df = df[EXPECTED_COLUMNS]

    # Convert columns to match the schema
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"], errors="coerce")
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"], errors="coerce")
    numeric_columns = [
        "passenger_count", "trip_distance", "fare_amount", "extra", "mta_tax",
        "tip_amount", "tolls_amount", "improvement_surcharge", "total_amount",
        "congestion_surcharge"
    ]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

    # Directory for GCS storage
    gcs_directory = f"yellow_tripdata_2022-{month:02d}/"

    # Process and upload data in chunks
    total_rows = len(df)
    for i in range(0, total_rows, CHUNK_SIZE):
        chunk = df.iloc[i:i + CHUNK_SIZE]

        # Convert chunk to CSV
        csv_buffer = StringIO()
        chunk.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        # GCS file name
        gcs_file_name = f"{gcs_directory}chunk_{i // CHUNK_SIZE + 1}.csv"

        # Upload to GCS
        gcs_hook = GCSHook(gcp_conn_id='google_cloud_default')
        gcs_hook.upload(
            bucket_name=BUCKET_NAME,
            object_name=gcs_file_name,
            data=csv_buffer.getvalue(),
            mime_type='text/csv',
        )
        print(f"Chunk {i // CHUNK_SIZE + 1} uploaded to {gcs_file_name}")

# DAG Definition
default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id="process_yellow_tripdata",
    default_args=default_args,
    description="Processes Yellow Cab trip data and uploads to GCS",
    schedule_interval=None,  # Set to `None` for manual execution
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:

    # Create tasks for each month
    for month in range(1, 13):
        PythonOperator(
            task_id=f"process_yellow_{month:02d}",
            python_callable=process_and_upload_to_gcs_in_chunks,
            op_kwargs={"month": month},
        )
