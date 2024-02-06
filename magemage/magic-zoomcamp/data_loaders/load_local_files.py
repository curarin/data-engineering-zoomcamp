from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    import pandas as pd
    import glob

    # Define the dtypes
    taxi_dtypes = {
        'VendorID': 'Int64',
        'passenger_count': 'Int64',
        'trip_distance': 'float64',
        'RatecodeID': 'Int64',
        'store_and_fwd_flag': 'str',
        'PULocationID': 'Int64',
        'DOLocationID': 'Int64',
        'payment_type': 'Int64',
        'fare_amount': 'float64',
        'extra': 'float64',
        'mta_tax': 'float64',
        'tip_amount': 'float64',
        'tolls_amount': 'float64',
        'improvement_surcharge': 'float64',
        'total_amount': 'float64',
        'congestion_surcharge': 'float64'
    }

    # Get the file list matching the regex pattern
    file_list = glob.glob("green_tripdata_2022-*.parquet")
    
    # Load data from Parquet files
    dfs = [pd.read_parquet(file) for file in file_list]
    
    # Concatenate all DataFrames
    df = pd.concat(dfs)
    
    # Convert columns to specified dtypes
    df = df.astype(taxi_dtypes)
    
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
