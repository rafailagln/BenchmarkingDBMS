import pymongo
import time
import udfs

# Connect to the MongoDB server˜
connectionString = 'mongodb://192.168.31.200:27017/'
# connectionString = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(connectionString)

# Get the "assignment" database
db = client["Assignment"]

# Get the "zillow" collection
collection = db["zillow"]

start_time = time.perf_counter()

results = collection.find()

# Use the filter() function to filter the results
filtered_results = filter(lambda x: udfs.extractbd(x['facts and features']) > 0
                                    and 100000 <= udfs.extractprice_sell(x['price']) <= 20000000
                                    and udfs.extractbd(x['facts and features'] < '10')
                                    and udfs.extracttype(x['title']) == 'condo'
                          , results)

with open("results.txt", "w") as file:
    for result in filtered_results:
        file.write(str(udfs.extractba(result['facts and features'])) + '\t' +
                   str(result['url']) + '\t' +
                   # str(result['url']) + '\n' + todo: address missing field?
                   str(udfs.extractpcode(result['postal_code'])) + '\t' +
                   str(udfs.extractbd(result['facts and features'])) + '\t' +
                   str(result['city']) + '\t' +
                   str(result['state']) + '\t' +
                   str(udfs.extract_offer(result['title'])) + '\t' +
                   str(udfs.extracttype(result['title'])) + '\t' +
                   str(udfs.extractpcode(result['postal_code'])) + '\t' +
                   str(udfs.extractsqfeet(result['facts and features'])) + '\t' +
                   str(udfs.extractprice_sell(result['price'])) + '\n'
                   )

end_time = time.perf_counter()
print(f'Time to execute: {end_time - start_time:0.6f} seconds')
