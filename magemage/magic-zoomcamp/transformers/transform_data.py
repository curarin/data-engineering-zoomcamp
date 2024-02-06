if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    df = data


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
