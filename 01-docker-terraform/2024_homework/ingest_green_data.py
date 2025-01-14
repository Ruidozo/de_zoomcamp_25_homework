import os
import pandas as pd
from sqlalchemy import create_engine
from time import time
import wget

def main():
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    database = os.getenv('DB')
    table = os.getenv('TABLE_NAME')
    url = os.getenv('URL')

    # Download the CSV file
    csv_file = 'green_tripdata_2019-09.csv.gz'
    wget.download(url, csv_file)

    # Create a connection to the database
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

    # Read the CSV file in chunks
    df_iter = pd.read_csv(csv_file, iterator=True, chunksize=100000)
    df = next(df_iter)

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    df.head(n=0).to_sql(table, engine, if_exists='replace', index=False)

    start_time = time()
    df.to_sql(table, engine, if_exists='append', index=False)
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")

    while True:
        try:
            t_start = time()
            df = next(df_iter)
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

            df.to_sql(table, engine, if_exists='append', index=False)
            t_end = time()
            print(f"Inserted another chunk, took {t_end - t_start} seconds")
        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break

    # Download and upload taxi zone lookup data
    zone_url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
    zone_csv = 'taxi_zone_lookup.csv'
    wget.download(zone_url, zone_csv)

    df_zones = pd.read_csv(zone_csv)
    df_zones.to_sql('zones', engine, if_exists='replace', index=False)
    print("Finished uploading taxi zone lookup data")

if __name__ == "__main__":
    main()