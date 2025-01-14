-- Question 5. Three biggest pickup zones

SELECT 
    zones."Zone" AS pickup_zone,
    SUM(taxi_trips.total_amount) AS total_amount
FROM 
    public.green_taxi_trips AS taxi_trips
JOIN 
    public.taxi_zone_lookup AS zones
ON 
    taxi_trips.PULocationID = zones.LocationID
WHERE 
    DATE(taxi_trips.lpep_pickup_datetime) = '2019-10-18'
GROUP BY 
    zones."Zone"
HAVING 
    SUM(taxi_trips.total_amount) > 13000
ORDER BY 
    total_amount DESC
LIMIT 3;