-- Question 3 --
SELECT COUNT(*) AS total_trips
FROM green_taxi_trips
WHERE DATE(lpep_pickup_datetime) = '2019-09-18'
  AND DATE(lpep_dropoff_datetime) = '2019-09-18';

--Question 4 -- 
  SELECT DATE(lpep_pickup_datetime) AS pickup_day, MAX(trip_distance) AS longest_trip_distance
FROM green_taxi_trips
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY longest_trip_distance DESC
LIMIT 1;

--Question 5 --
SELECT zones."Borough", SUM(trips."total_amount") AS total_amount
FROM green_taxi_trips AS trips
JOIN zones ON trips."PULocationID" = zones."LocationID"
WHERE DATE(trips."lpep_pickup_datetime") = '2019-09-18'
  AND zones."Borough" != 'Unknown'
GROUP BY zones."Borough"
HAVING SUM(trips."total_amount") > 50000
ORDER BY total_amount DESC
LIMIT 3;


-- Question 6 --
SELECT dropoff_zones."Zone" AS dropoff_zone, MAX(trips."tip_amount") AS largest_tip
FROM green_taxi_trips AS trips
JOIN zones AS pickup_zones ON trips."PULocationID" = pickup_zones."LocationID"
JOIN zones AS dropoff_zones ON trips."DOLocationID" = dropoff_zones."LocationID"
WHERE pickup_zones."Zone" = 'Astoria'
  AND DATE(trips."lpep_pickup_datetime") BETWEEN '2019-09-01' AND '2019-09-30'
GROUP BY dropoff_zones."Zone"
ORDER BY largest_tip DESC
LIMIT 1;