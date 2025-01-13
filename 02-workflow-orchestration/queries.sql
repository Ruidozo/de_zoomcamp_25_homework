-- Question 3
SELECT COUNT(*) FROM `de-zoomcamp-25`.`zoomcamp_dataset_kestra`.`yellow_tripdata` WHERE EXTRACT(YEAR FROM tpep_pickup_datetime) = 2020;

-- Question 4
SELECT COUNT(*) FROM `de-zoomcamp-25`.`zoomcamp_dataset_kestra`.`green_tripdata` WHERE EXTRACT(YEAR FROM lpep_pickup_datetime) = 2020;

-- Question 5
SELECT count(*) FROM `de-zoomcamp-25`.`zoomcamp_dataset_kestra`.`fact_trips` WHERE CAST(pickup_datetime AS STRING) LIKE '2020%';