import pymongo
import pandas as pd
import time
import udfs
import numpy as np
from multiprocessing import Pool

def applyUdfs(df_wb):
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
    return df_wb

def parallelize_dataframe(df, func, n_cores=4):
    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df

# Connect to the MongoDB server˜
connectionString = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(connectionString)

# Get the "assignment" database
db = client["assignment"]

# Get the "weblogs" and bad_ips collections
collection_wb = db["weblogs"]
collection_bips = db["bad_ips"]

time1 = time.perf_counter()

# start_time = time.perf_counter()

results_wb = collection_wb.find()
results_bips = collection_bips.find()

# Load dataframe
df_wb = pd.DataFrame(list(results_wb))
df_bips = pd.DataFrame(list(results_bips))

time2 = time.perf_counter()

print(f'Time to get all collections: {time2 - time1:0.6f} seconds')

df_wb = applyUdfs(df_wb)

time3 = time.perf_counter()
print(f'Time to execute udfs (single-core): {time3 - time2:0.6f} seconds')

df_wb = parallelize_dataframe(df_wb, applyUdfs)

time4 = time.perf_counter()
print(f'Time to execute udfs (multi-core): {time4 - time3:0.6f} seconds')


df_wb.drop('column1', inplace=True, axis=1)
df_wb.drop('_id', inplace=True, axis=1)
df_bips.drop('_id', inplace=True, axis=1)
result = pd.merge(df_wb, df_bips, left_on='ip', right_on='BadIPs')


time5 = time.perf_counter()

print(f'Time to merge data: {time5 - time4:0.6f} seconds')

result.to_csv(r'results.txt', header=None)

time6 = time.perf_counter()

print(f'Time to write to file: {time6 - time5:0.6f} seconds\n')

print(f'Total time to execute (single-core): {(time2 - time1)+(time3-time2)+(time5-time4)+(time6-time5):0.6f} seconds')
print(f'Total time to execute (multi-core): {(time2 - time1)+(time4-time3)+(time5-time4)+(time6-time5):0.6f} seconds')
# end_time = time.perf_counter()
# print(f'Time to execute: {end_time - start_time:0.6f} seconds')
