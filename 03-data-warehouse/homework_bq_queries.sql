-- Question 1
SELECT COUNT(*) FROM de-zoomcamp-25.week_3_green_taxi.green_taxi_2022;

-- Question 2
SELECT count(DISTINCT PULocationID) FROM de-zoomcamp-25.week_3_green_taxi.green_taxi_2022;

--Question 3
SELECT COUNT(*) FROM de-zoomcamp-25.week_3_green_taxi.green_taxi_2022 WHERE fare_amount = 0;

--Question 4 -Partition by lpep_pickup_datetime  Cluster on PUlocationID
CREATE TABLE de-zoomcamp-25.week_3_green_taxi.optimized_green_taxi_2022
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
SELECT * 
FROM de-zoomcamp-25.week_3_green_taxi.green_taxi_2022;

--Question 5 - retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)

--Non - Partitioned
SELECT DISTINCT PULocationID FROM de-zoomcamp-25.week_3_green_taxi.green_taxi_2022 WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';

-- Partioned
SELECT DISTINCT PULocationID FROM de-zoomcamp-25.week_3_green_taxi.optimized_green_taxi_2022 WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';

-- Question 8

## (Bonus: Not worth points) Question 8:

-- ## (Bonus: Not worth points) Question 8:

SELECT count(*) FROM de-zoomcamp-25.week_3_green_taxi.optimized_green_taxi_2022;


 

