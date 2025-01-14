import os
import pandas as pd
from sqlalchemy import create_engine
from time import time

# Environment variables
user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DB')
table = os.getenv('TABLE_NAME')
url = os.getenv('URL')
table_2 = os.getenv('TABLE_NAME_2')
url_2 = os.getenv('URL_2')

# Download the first CSV file
df = pd.read_csv(url)

# Save the first CSV file
csv_file = 'green_tripdata.csv'
df.to_csv(csv_file, index=False)

# Ingest the first CSV file into the database
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
engine.connect()

# Ingest the entire CSV file into the database
df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
df.to_sql(table, engine, if_exists='replace', index=False)

print(f"Data ingested into table {table}")

# Download the second CSV file
df_zones = pd.read_csv(url_2)

# Save the second CSV file
csv_file_2 = 'taxi_zone_lookup.csv'
df_zones.to_csv(csv_file_2, index=False)

# Ingest the second CSV file into the database
df_zones.to_sql(table_2, engine, if_exists='replace', index=False)
print(f"Taxi zone lookup data ingested into table {table_2}")