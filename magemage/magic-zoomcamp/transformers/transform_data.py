if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    df = data
    #remove rows where passenger_count = 0
    df = df[(df["passenger_count"] > 0) & (df["trip_distance"] > 0)]

    #transform to date
    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date
    df["lpep_dropoff_date"] = df["lpep_dropoff_datetime"].dt.date

    #check column names for snakecase potentials and renaming
    df = df.rename(columns={
        "VendorID": "vendor_id",
        "RatecodeID": "ratecode_id",
        "PULocationID": "pu_location_id",
        "DOLocationID": "do_location_id"
    })
    #find out existing values of VendorID
    vendor_ids_grouped = df.groupby(["vendor_id"]).count()

    return df

@test
def vendor_id_check(df) -> None:
    #get vendor ids in list and check if its one of the values inside the list
    vendor_ids_grouped = df.groupby(["vendor_id"]).count()
    vendor_ids_list = vendor_ids_grouped.index.to_list()
    assert df["vendor_id"].isin(vendor_ids_list).all(), "Vendor ID is not one of existing values in the column."

@test
def passanger_count_greater_zero(df) -> None:
    assert (df["passenger_count"] > 0).all(), "Dataset currently has taxi drives with potentially false passenger count (equal to 0)"

@test
def trip_distance_greater_zero(df) -> None:
    assert (df["trip_distance"] >0).all(), "Dataset currently has taxi drives which potentiall false drives, as the trrip distance is 0 km."