import pymongo
import time
import udfs
import pandas as pd

# Connect to the MongoDB server˜
connectionString = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(connectionString)

# Get the "assignment" database
db = client["assignment"]

# Get the "zillow" collection
collection = db["zillow"]

start_time = time.perf_counter()

results = collection.find()

# Load dataframe
df = pd.DataFrame(list(results))

df['price'] = df.apply(lambda x: udfs.extractprice_sell(x['price']), axis=1)
df['price'] = df['price'].replace('+', '')

# extract bedrooms, bathrooms, sqft, zip_code, url, offer from the dataframe
df['bedrooms'] = df.apply(lambda x: udfs.extractbd(x['facts and features']), axis=1)
df['bathrooms'] = df.apply(lambda x: udfs.extractba(x['facts and features']), axis=1)
df['sqft'] = df.apply(lambda x: udfs.extractsqfeet(x['facts and features']), axis=1)
df['zip_code'] = df.apply(lambda x: udfs.extractpcode(x['postal_code']), axis=1)
df['offer'] = df.apply(lambda x: udfs.extracttype(x['title']), axis=1)

# Filter the dataframe using the WHERE clause
df = df[(df['bedrooms'].astype(int) < 10)
        & (df['price'].astype(int) > 100000)
        & (df['price'].astype(int) < 20000000)
        & ("None" not in df['facts and features'])
        & (df['title'] == 'condo')]


df.to_csv('results.txt')

end_time = time.perf_counter()
print(f'Time to execute: {end_time - start_time:0.6f} seconds')