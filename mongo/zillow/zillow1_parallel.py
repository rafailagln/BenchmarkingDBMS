import pymongo
import time
import udfs
import pandas as pd
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
    df['offer'] = df.apply(lambda x: udfs.extracttype(x['title']), axis=1)
    return df

# Connect to the MongoDB server˜
connectionString = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(connectionString)

# Get the "assignment" database
db = client["assignment"]

# Get the "zillow" collection
collection = db["zillow"]

# start_time = time.perf_counter()
time1 = time.perf_counter()

results = collection.find()

time2 = time.perf_counter()

print(f'Time to get all collection: {time2 - time1:0.6f} seconds')

df = applyUdfs(df)

time3 = time.perf_counter()
print(f'Time to execute udfs (single-core): {time3 - time2:0.6f} seconds')

df = parallelize_dataframe(df, applyUdfs)

time4 = time.perf_counter()
print(f'Time to execute udfs (multi-core): {time4 - time3:0.6f} seconds')

# Use the filter() function to filter the results
filtered_results = filter(lambda x: udfs.extractbd(x['facts and features']) < 10
                                    and 100000 <= udfs.extractprice_sell(x['price']) <= 20000000
                                    and udfs.extracttype(x['title']) == 'condo'
                          , results)
# Load dataframe
df = pd.DataFrame(list(results))

# Filter the dataframe using the WHERE clause
df = df[(df['bedrooms'].astype(int) < 10)
        & (df['price'].astype(int) > 100000)
        & (df['price'].astype(int) < 20000000)
        & ("None" not in df['facts and features'])
        & (df['title'] == 'condo')]

time5 = time.perf_counter()

print(f'Time to filter data: {time5 - time4:0.6f} seconds')

df.to_csv('results.txt')

time6 = time.perf_counter()

print(f'Time to write to file: {time6 - time5:0.6f} seconds\n')


print(f'Total time to execute (single-core): {(time2 - time1)+(time3-time2)+(time5-time4)+(time6-time5):0.6f} seconds')
print(f'Total time to execute (multi-core): {(time2 - time1)+(time4-time3)+(time5-time4)+(time6-time5):0.6f} seconds')
# end_time = time.perf_counter()
# print(f'Time to execute: {end_time - start_time:0.6f} seconds')
