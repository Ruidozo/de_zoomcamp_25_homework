```bash
odiurdigital@de-zoomcamp-25-instance:~/de_zoomcamp_25_homework$ bq load --source_format=CSV \
  --autodetect \
  --replace=true \
  de-zoomcamp-25:week_3_green_taxi.green_taxi_2022 \
  "gs://green_cab_bucket_zoomcamp_25_oduir/*.csv"
  ```