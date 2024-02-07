from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    import pandas as pd
    #dtypes declaring
    taxi_dtypes = taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float 
    }

    #load all three months at once
    file_list = ["green_tripdata_2020-10.csv.gz", "green_tripdata_2020-11.csv.gz", "green_tripdata_2020-12.csv.gz"]
    compression = "gzip"
    dtype = taxi_dtypes  
    parse_dates = ["lpep_pickup_datetime", "lpep_dropoff_datetime"]

    dfs = [pd.read_csv(file, compression=compression, dtype=dtype, parse_dates=parse_dates) for file in file_list]
    df = pd.concat(dfs)
    

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'