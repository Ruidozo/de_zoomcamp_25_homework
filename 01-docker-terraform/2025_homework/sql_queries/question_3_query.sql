-- Question 3 - Trip Segmentation Count

SELECT 
    SUM(CASE 
        WHEN trip_distance <= 1 THEN 1 
        ELSE 0 
    END) AS trips_up_to_1_mile,
    SUM(CASE 
        WHEN trip_distance > 1 AND trip_distance <= 3 THEN 1 
        ELSE 0 
    END) AS trips_between_1_and_3_miles,
    SUM(CASE 
        WHEN trip_distance > 3 AND trip_distance <= 7 THEN 1 
        ELSE 0 
    END) AS trips_between_3_and_7_miles,
    SUM(CASE 
        WHEN trip_distance > 7 AND trip_distance <= 10 THEN 1 
        ELSE 0 
    END) AS trips_between_7_and_10_miles,
    SUM(CASE 
        WHEN trip_distance > 10 THEN 1 
        ELSE 0 
    END) AS trips_over_10_miles
FROM 
    public.green_taxi_trips
WHERE 
    lpep_pickup_datetime >= '2019-10-01' 
    AND lpep_pickup_datetime < '2019-11-01';
