## Data Engineering Zoomcamp - Week 23 BigQuery

### These are SQL queries i used for the homework
- Step 1: Spin up docker compose locally
```
docker compose up -d
```
- Step 2: Download the PARQUET files, e.g.:
```
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-01.parquet
```
- Step 3: EL data to GCS using pipeline called week3_homework_etl
- Step 4: Create external table in BQ with data source 'google cloud storage' with URi pattern ('adroit-medium-379911-magedemo/nyc_green_taxi_whole_year_v2/lpep_pickup_date=*')
- Step 5: Create materialized view with the following SQL query
```
CREATE MATERIALIZED VIEW adroit-medium-379911.ny_taxi.week3_homework_materialized AS
SELECT *
FROM `adroit-medium-379911.ny_taxi.week3_homework`
```

For the questinaire I used the following SQL queries
- SQL-Query for Question 1 (Answer: 840,402)
```
SELECT COUNT(*)
FROM adroit-medium-379911.ny_taxi.week3_homework
```
- SQL-Query for Question 2 (Answer: 0 MB for the External Table and 6.41MB for the Materialized Table)
```
SELECT COUNT(DISTINCT pu_location_id)
FROM adroit-medium-379911.ny_taxi.week3_homework_external
```
```
SELECT COUNT(DISTINCT pu_location_id)
FROM adroit-medium-379911.ny_taxi.week3_homework_materialized
```

- SQL-Query for Question 3 (Answer: 1,622)
```
SELECT COUNT(*)
FROM adroit-medium-379911.ny_taxi.week3_homework_materialized
WHERE fare_amount = 0;
```

- Question 4 Answer: Partition by lpep_pickup_datetime Cluster on PUlocationID

- Question 5 Answer was 12.82MB for non-partinioed table and 1.12 MB for partinioned table. The Query used:
```
SELECT COUNT(DISTINCT pu_location_id)
FROM adroit-medium-379911.ny_taxi.week3_homework_materialized
WHERE lpep_pickup_datetime BETWEEN 1654070400000 AND 1656638399000
```

- Question 6 Answer: GCP Bucket
- QUestion 7 Answer: False
- QUestion 8: 0B, because the data is retrieved from meta data and not actual scanning of the rows. 