import pymongo
import pandas as pd
import time
import udfs

# Connect to the MongoDB server˜
connectionString = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(connectionString)

# Get the "assignment" database
db = client["assignment"]

# Get the "weblogs" and bad_ips collections
collection_wb = db["weblogs"]
collection_bips = db["bad_ips"]

start_time = time.perf_counter()

results_wb = collection_wb.find()
results_bips = collection_bips.find()

# Load dataframe
df_wb = pd.DataFrame(list(results_wb))
df_bips = pd.DataFrame(list(results_bips))

# extract endpoint, ip, client_id, user_id, method, protocol, response_code, content_size, date from the dataframe
df_wb['endpoint'] = df_wb.apply(lambda x: udfs.extract_endpoint(x.column1), axis=1)
df_wb['ip'] = df_wb.apply(lambda x: udfs.extract_ip(x['column1']), axis=1)
df_wb['client_id'] = df_wb.apply(lambda x: udfs.extract_client_id(x['column1']), axis=1)
df_wb['user_id'] = df_wb.apply(lambda x: udfs.extract_user_id(x['column1']), axis=1)
df_wb['method'] = df_wb.apply(lambda x: udfs.extract_method(x['column1']), axis=1)
df_wb['protocol'] = df_wb.apply(lambda x: udfs.extract_protocol(x['column1']), axis=1)
df_wb['response_code'] = df_wb.apply(lambda x: udfs.extract_response_code(x['column1']), axis=1)
df_wb['content_size'] = df_wb.apply(lambda x: udfs.extract_content_size(x['column1']), axis=1)
df_wb['date'] = df_wb.apply(lambda x: udfs.extract_date(x['column1']), axis=1)

df_wb.drop('column1', inplace=True, axis=1)
df_wb.drop('_id', inplace=True, axis=1)
df_bips.drop('_id', inplace=True, axis=1)
result = pd.merge(df_wb, df_bips, left_on='ip', right_on='BadIPs')

result.to_csv(r'results.txt', header=None)

end_time = time.perf_counter()
print(f'Time to execute: {end_time - start_time:0.6f} seconds')
