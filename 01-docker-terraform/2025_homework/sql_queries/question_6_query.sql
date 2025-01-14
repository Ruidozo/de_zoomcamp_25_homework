-- Question 6 - Largest Tip

SELECT 
    drop_zones."Zone" AS dropoff_zone,
    MAX(taxi_trips.tip_amount) AS largest_tip
FROM 
    public.green_taxi_trips AS taxi_trips
JOIN 
    public.taxi_zone_lookup AS pickup_zones
ON 
    taxi_trips."PULocationID" = pickup_zones."LocationID"
JOIN 
    public.taxi_zone_lookup AS drop_zones
ON 
    taxi_trips."DOLocationID" = drop_zones."LocationID"
WHERE 
    pickup_zones."Zone" = 'East Harlem North'
    AND DATE(taxi_trips.lpep_pickup_datetime) BETWEEN '2019-10-01' AND '2019-10-31'
GROUP BY 
    drop_zones."Zone"
ORDER BY 
    largest_tip DESC
LIMIT 1;
