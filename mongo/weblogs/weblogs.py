import pymongo
import pandas as pd
import time
import udfs
import re

# Connect to the MongoDB server˜
# connectionString = 'mongodb://192.168.31.200:27017/'
connectionString = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(connectionString)

# Get the "assignment" database
db = client["assignment"]

# Get the "zillow" collection
collection_wb = db["weblogs"]
collection_bips = db["bad_ips"]

start_time = time.perf_counter()

results_wb = collection_wb.find()
results_bips = collection_bips.find()

# Load dataframe
df_wb = pd.DataFrame(list(results_wb))
df_bips = pd.DataFrame(list(results_bips))
# print(df_wb)

df_wb['endpoint'] = df_wb.apply(lambda x: udfs.extract_endpoint(x.column1), axis=1)

# df_wb = df_wb[df_wb['endpoint'] !='-1']

# df_wb['column1'] = df_wb['column1'].astype('str')
# # # extract bedrooms, bathrooms, sqft, zip_code, url, offer from the dataframe
# df_wb = df_wb.apply(lambda x: udfs.extract_ip(x.values()), axis=1)
df_wb['ip'] = df_wb.apply(lambda x: udfs.extract_ip(x['column1']), axis=1)
df_wb['client_id'] = df_wb.apply(lambda x: udfs.extract_client_id(x['column1']), axis=1)
df_wb['user_id'] = df_wb.apply(lambda x: udfs.extract_user_id(x['column1']), axis=1)
df_wb['method'] = df_wb.apply(lambda x: udfs.extract_method(x['column1']), axis=1)
df_wb['endpoint'] = df_wb.apply(lambda x: udfs.extract_protocol(x['column1']), axis=1)
df_wb['response_code'] = df_wb.apply(lambda x: udfs.extract_response_code(x['column1']), axis=1)
df_wb['content_size'] = df_wb.apply(lambda x: udfs.extract_content_size(x['column1']), axis=1)


print(df_wb.columns)
df_wb.drop('column1', inplace=True, axis=1)
print(df_wb)
result = pd.merge(df_wb, df_bips, left_on='ip', right_on='BadIPs')
print(result)


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
