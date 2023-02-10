import pymongo
import pandas as pd
import numpy as np
import time
import udfs
import extra_udfs
from multiprocessing import Pool

def parallelize_dataframe(df, func, n_cores=4):
    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df

def applyUdfs(df):
    df['price'] = df.apply(lambda x: udfs.extractprice_sell(x['price']), axis=1)
    df['price'] = df['price'].replace('+', '')

    # extract bedrooms, bathrooms, sqft, zip_code, url, offer from the dataframe
    df['bedrooms'] = df.apply(lambda x: udfs.extractbd(x['facts and features']), axis=1)
    df['bathrooms'] = df.apply(lambda x: udfs.extractba(x['facts and features']), axis=1)
    df['sqft'] = df.apply(lambda x: udfs.extractsqfeet(x['facts and features']), axis=1)
    df['zip_code'] = df.apply(lambda x: udfs.extractpcode(x['postal_code']), axis=1)
    df['url'] = df.apply(lambda x: extra_udfs.replace_o_a(extra_udfs.strip(extra_udfs.to_lower(x['url']))), axis=1)
    df['offer'] = df.apply(lambda x: udfs.extracttype(x['title']), axis=1)
    return df

# Connect to the MongoDB server˜
connectionString = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(connectionString)

# Get the "assignment" database
db = client["assignment"]

# Get the "zillow" collection
collection = db["zillow"]

time1 = time.perf_counter()

results = collection.find()

# Load dataframe
df = pd.DataFrame(list(results))

time2 = time.perf_counter()

print(f'Time to get all collection: {time2 - time1:0.6f} seconds')

df = applyUdfs(df)

time3 = time.perf_counter()
print(f'Time to execute udfs (single-core): {time3 - time2:0.6f} seconds')

df = parallelize_dataframe(df, applyUdfs)

time4 = time.perf_counter()
print(f'Time to execute udfs (multi-core): {time4 - time3:0.6f} seconds')

# Filter the dataframe using the WHERE clause
df = df[(df['bedrooms'].astype(int) < 10)
        & (df['price'].astype(int) > 100000)
        & (df['price'].astype(int) < 20000000)
        & ("None" not in df['facts and features'])]

# aggregate data using groupby
grouped_df = df.groupby(['bedrooms']).agg(
    {'bathrooms': 'sum', 'sqft': 'sum', 'url': 'count', 'offer': 'count', 'zip_code': 'count'})

# rename columns
grouped_df.rename(
    columns={'bathrooms': 'sum_ba', 'sqft': 'sum_sqft', 'url': 'urls', 'offer': 'offers', 'zip_code': 'zip_codes'},
    inplace=True)
time5 = time.perf_counter()

print(f'Time to filter and group data: {time5 - time4:0.6f} seconds')

grouped_df.to_csv('results2.csv')

time6 = time.perf_counter()

print(f'Time to write to file: {time6 - time5:0.6f} seconds\n')
print(f'Total time to execute (single-core): {(time2 - time1)+(time3-time2)+(time5-time4)+(time6-time5):0.6f} seconds')
print(f'Total time to execute (multi-core): {(time2 - time1)+(time4-time3)+(time5-time4)+(time6-time5):0.6f} seconds')