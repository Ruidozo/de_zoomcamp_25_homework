-- Question 4 - Trip Segmentation Count

WITH daily_max_distances AS (
    SELECT 
        DATE(lpep_pickup_datetime) AS pickup_day,
        MAX(trip_distance) AS max_distance
    FROM 
        public.green_taxi_trips
    GROUP BY 
        DATE(lpep_pickup_datetime)
)
SELECT 
    pickup_day, 
    max_distance
FROM 
    daily_max_distances
WHERE 
    pickup_day IN ('2019-10-11', '2019-10-24', '2019-10-26', '2019-10-31')
ORDER BY 
    max_distance DESC
LIMIT 1;
