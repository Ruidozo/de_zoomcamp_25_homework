# Docker

## Question 1. Understanding docker first run 

Run docker with the `python:3.12.8` image in an interactive mode, use the entrypoint `bash`.

What's the version of `pip` in the image?

- 24.3.1 <-- Answer
- 24.2.1
- 23.3.1
- 23.2.1


### Answer

To run docker in interactive mode with the entrypoint bash we just need to run this commando on the shell:

```bash

docker run -it --entrypoint bash python:3.12.8

```

We can then see which version pip has inside the container:

```shell
root@2da7e4ded1f4:/# pip --version
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
root@2da7e4ded1f4:/# 
```

## Question 2. Understanding Docker networking and docker-compose

Given the following `docker-compose.yaml`, what is the `hostname` and `port` that **pgadmin** should use to connect to the postgres database?

- postgres:5433
- localhost:5432
- db:5433
- postgres:5432
- db:5432 <-- Answer

### Answer

Since **db** is setup as the service name as the postgresSQL database this can be acessed using the hostname db. The port is set as 5432.  

```yaml
servic<es:
  db: #<-- hostname
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432' # <-- Port
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin  

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```


# Postgres

A docker-compose file was done [here](/01-docker-terraform/2025_homework/docker-compose.yaml) where it forms a container with pgadmin, postgres and ingest the data for the two tables.

## Question 3. Trip Segmentation Count

During the period of October 1st 2019 (inclusive) and November 1st 2019 (exclusive), how many trips, **respectively**, happened:
1. Up to 1 mile
2. In between 1 (exclusive) and 3 miles (inclusive),
3. In between 3 (exclusive) and 7 miles (inclusive),
4. In between 7 (exclusive) and 10 miles (inclusive),
5. Over 10 miles 

### Answer

After loading the data into postgres i did a query that can be found [here](/01-docker-terraform/2025_homework/sql_queries/question_3_query.sql) that return the following result:

![result query Q3](/01-docker-terraform/2025_homework/images/image.png)

Since the values do not exactly match with the options, i went with the closest which was aswer 5

- 104,793;  197,670;  110,612;  27,831;  35,281
- 104,793;  198,924;  109,603;  27,678;  35,189
- 101,056;  201,407;  110,612;  27,831;  35,281
- 101,056;  202,661;  109,603;  27,678;  35,189
- 104,838;  199,013;  109,645;  27,688;  35,202 <-- Answer


## Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance?
Use the pick up time for your calculations.

Tip: For every day, we only care about one single trip with the longest distance. 

### Answer

For this question i again wrote a [query](/01-docker-terraform/2025_homework/sql_queries/question_4_query.sql) which filters the days that we are interested to know and orders them in descending order. From here limits to 1 to gives us  the result of the max distance. 

The result of the query is: 

![Question 4](/01-docker-terraform/2025_homework/images/image-1.png)


- 2019-10-11
- 2019-10-24
- 2019-10-26
- 2019-10-31 <-- Answer 


## Question 5. Three biggest pickup zones

Which were the top pickup locations with over 13,000 in
`total_amount` (across all trips) for 2019-10-18?

Consider only `lpep_pickup_datetime` when filtering by date.

### Answer

for this question, i made an new [query](/01-docker-terraform/2025_homework/sql_queries/question_5_query.sql) where it joins both tables using the PULocationID to match the LocationID in the zones table. then it filtres by date, aggregates the data to calculate the total amount and filters the zones to keep only the ones exciding 13,000, than sort and limits to 3 zones. 

the rsult on pgadmin is 

![alt text](/01-docker-terraform/2025_homework/images/image-2.png)

- East Harlem North, East Harlem South, Morningside Heights <-- answer
- East Harlem North, Morningside Heights
- Morningside Heights, Astoria Park, East Harlem South
- Bedford, East Harlem North, Astoria Park


## Question 6. Largest tip

For the passengers picked up in Ocrober 2019 in the zone
name "East Harlem North" which was the drop off zone that had
the largest tip?

### Answer

The [query](/01-docker-terraform/2025_homework/sql_queries/question_6_query.sql) starts by joining tables, filters the pickup zones and dates and calculates the largest tip. It then sorts and limits to the top place:

![Question 6](/01-docker-terraform/2025_homework/images/image-3.png)

- Yorkville West
- JFK Airport <-- Answer
- East Harlem North
- East Harlem South


# Terraform

## Question 7. Terraform Workflow

Which of the following sequences, **respectively**, describes the workflow for: 
1. Downloading the provider plugins and setting up backend,
2. Generating proposed changes and auto-executing the plan
3. Remove all resources managed by terraform`


### Answer

- Terraform [main.tf](/01-docker-terraform/2025_homework/terraform/main.tf)
- Terraform [variables.tf](/01-docker-terraform/2025_homework/terraform/variables.tf)
- Terminal output [here](/01-docker-terraform/2025_homework/terraform/output_terraform.md)


Answers:
- terraform import, terraform apply -y, terraform destroy
- teraform init, terraform plan -auto-apply, terraform rm
- terraform init, terraform run -auto-aprove, terraform destroy
- terraform init, terraform apply -auto-approve, terraform destroy <-- Answer 
- terraform import, terraform apply -y, terraform rm