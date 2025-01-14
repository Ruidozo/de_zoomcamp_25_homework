from airflow import DAG
from airflow.providers.google.cloud.operators.gcs import GCSCreateBucketOperator, GCSDeleteBucketOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
import pendulum

# Configurações do GCS
BUCKET_GREEN = "green_cab_bucket_zoomcamp_25_oduir"
BUCKET_YELLOW = "yellow_cab_bucket_zoomcamp_25_oduir"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}

with DAG(
    dag_id="create_or_replace_gcs_buckets",
    default_args=default_args,
    description="Apaga e cria buckets no GCS, depois dispara os DAGs de upload.",
    schedule_interval=None,
    start_date=pendulum.today('UTC').add(days=-1),
    catchup=False,
) as dag:
    start = DummyOperator(task_id="start")

    # Tasks para apagar os buckets
    delete_green_bucket = GCSDeleteBucketOperator(
        task_id="delete_green_bucket",
        bucket_name=BUCKET_GREEN,
        gcp_conn_id='google_cloud_default',
        force=True,
        trigger_rule="all_done",
    )

    delete_yellow_bucket = GCSDeleteBucketOperator(
        task_id="delete_yellow_bucket",
        bucket_name=BUCKET_YELLOW,
        gcp_conn_id='google_cloud_default',
        force=True,
        trigger_rule="all_done",
    )

    # Tasks para criar os buckets
    create_green_bucket = GCSCreateBucketOperator(
        task_id="create_green_bucket",
        bucket_name=BUCKET_GREEN,
        storage_class="STANDARD",
        location="EUROPE-WEST2",
        gcp_conn_id='google_cloud_default',
    )

    create_yellow_bucket = GCSCreateBucketOperator(
        task_id="create_yellow_bucket",
        bucket_name=BUCKET_YELLOW,
        storage_class="STANDARD",
        location="EUROPE-WEST2",
        gcp_conn_id='google_cloud_default',
    )

    # Disparar os DAGs de upload
    trigger_green_upload = TriggerDagRunOperator(
        task_id="trigger_green_upload",
        trigger_dag_id="process_green_tripdata",
    )

    trigger_yellow_upload = TriggerDagRunOperator(
        task_id="trigger_yellow_upload",
        trigger_dag_id="process_yellow_tripdata",
    )

    # Sequência de execução
    start >> [delete_green_bucket, delete_yellow_bucket]
    delete_green_bucket >> create_green_bucket >> trigger_green_upload
    delete_yellow_bucket >> create_yellow_bucket >> trigger_yellow_upload
