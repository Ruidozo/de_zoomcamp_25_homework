odiurdigital@de-zoomcamp-25-instance:~/de_zoomcamp_25_homework$ bq load --source_format=CSV \
  --autodetect \
  --replace=true \
  de-zoomcamp-25:week_3_green_taxi.green_taxi_2022 \
  "gs://green_cab_bucket_zoomcamp_25_oduir/*.csv"
Waiting on bqjob_r70ef453de41516cf_0000019465522954_1 ... (7s) Current status: RUNNING