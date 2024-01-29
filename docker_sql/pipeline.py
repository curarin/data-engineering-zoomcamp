import pandas as pd
from sqlalchemy import create_engine
from time import time
import sys
import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    print(url)

    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")

    #create postgres DB connection
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    #create iter 
    ny_data_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    #iterate and create chunks & upload to postgres
    while True:
        try:
            t_start = time()
            ny_data = next(ny_data_iter)
            ny_data.tpep_pickup_datetime = pd.to_datetime(ny_data.tpep_pickup_datetime)
            ny_data.tpep_dropoff_datetime = pd.to_datetime(ny_data.tpep_dropoff_datetime)
            ny_data.to_sql(name=table_name, con=engine, if_exists="append")
            t_end = time()
            print("Inserted another chunk..., took %.3f seconds" % (t_end - t_start))
        except StopIteration:
            print("Data fully loaded.")
            break

if __name__ == "__main__":
    #cli parser
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")
    #user
    parser.add_argument("--user", help="user name for postgres")
    #password
    parser.add_argument("--password", help="password for postgres")
    #host
    parser.add_argument("--host", help="host for postgres")
    #port
    parser.add_argument("--port", help="port for postgres", type=int)
    #db name
    parser.add_argument("--db", help="db name for postgres")
    #table name
    parser.add_argument("--table_name", help="name of table where we will write results")
    #url of the csv
    parser.add_argument("--url", help="url of the csv file")

    args = parser.parse_args()
    main(args)


#load data
ny_data = pd.read_csv("/Users/paulherzog/Documents/GitHub/de-zoomcamp/de-zoomcamp/docker_sql/yellow_tripdata_2021-01.csv")



