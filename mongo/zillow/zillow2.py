import pymongo
import pandas as pd
import time
import udfs
import extra_udfs

# Connect to the MongoDB server˜
# connectionString = 'mongodb://192.168.31.200:27017/'
connectionString = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(connectionString)

# Get the "assignment" database
db = client["assignment"]

# Get the "zillow" collection
collection = db["zillow"]

start_time = time.perf_counter()

results = collection.find()

# Use the filter() function to filter the results
# filtered_results2 = filter(lambda x: udfs.extractbd(x['facts and features']) < 10
#                                     and 100000 <= udfs.extractprice_sell(x['price']) <= 20000000
#                                     and x['facts and features'].find("None") == -1
#                                     #and udfs.extracttype(x['title']) == 'condo'
#                           , results)
# temp = sum(int(udfs.extractba(item['facts and features'])) for item in filtered_results2)

# Load dataframe
df = pd.DataFrame(list(results))
print(df.dtypes)
# df = df._reindex_columns()
print(df.columns)

# print(df.columns.get_loc('facts_and_features'))
# Replace '+' with ''
df['price'] = df.apply(lambda x: udfs.extractprice_sell(x['price']), axis=1)
df['price'] = df['price'].replace('+', '')

# print(df['facts_and_features'].astype(str))

# extract bedrooms, bathrooms, sqft, zip_code, url, offer from the dataframe
df['bedrooms'] = df.apply(lambda x: udfs.extractbd(x['facts and features']), axis=1)
df['bathrooms'] = df.apply(lambda x: udfs.extractba(x['facts and features']), axis=1)
df['sqft'] = df.apply(lambda x: udfs.extractsqfeet(x['facts and features']), axis=1)
df['zip_code'] = df.apply(lambda x: udfs.extractpcode(x['postal_code']), axis=1)
df['url'] = df.apply(lambda x: extra_udfs.replace_o_a(extra_udfs.strip(extra_udfs.to_lower(x['url']))), axis=1)
df['offer'] = df.apply(lambda x: udfs.extracttype(x['title']), axis=1)

# Filter the dataframe using the WHERE clause
df = df[(df['bedrooms'].astype(int) < 10) &
        (df['price'].astype(int) > 100000)
        & (df['price'].astype(int) < 20000000)
        & (df['facts and features'] != 'None')]

# aggregate data using groupby
grouped_df = df.groupby(['bedrooms']).agg(
    {'bathrooms': 'sum', 'sqft': 'sum', 'url': 'count', 'offer': 'count', 'zip_code': 'count'})

# rename columns
grouped_df.rename(
    columns={'bathrooms': 'sum_ba', 'sqft': 'sum_sqft', 'url': 'urls', 'offer': 'offers', 'zip_code': 'zip_codes'},
    inplace=True)

print(grouped_df)

# with open("results.txt", "w") as file:
#     for result in filtered_results:
#         file.write(str(udfs.extractba(result['facts and features'])) + '\t' +
#                    str(result['url']) + '\t' +
#                    # str(result['url']) + '\n' + todo: address missing field?
#                    str(udfs.extractpcode(result['postal_code'])) + '\t' +
#                    str(udfs.extractbd(result['facts and features'])) + '\t' +
#                    str(result['city']) + '\t' +
#                    str(result['state']) + '\t' +
#                    str(udfs.extract_offer(result['title'])) + '\t' +
#                    str(udfs.extracttype(result['title'])) + '\t' +
#                    str(udfs.extractpcode(result['postal_code'])) + '\t' +
#                    str(udfs.extractsqfeet(result['facts and features'])) + '\t' +
#                    str(udfs.extractprice_sell(result['price'])) + '\n'
#                    )


end_time = time.perf_counter()
# print(f'Time to execute: {end_time - start_time:0.6f} seconds')
