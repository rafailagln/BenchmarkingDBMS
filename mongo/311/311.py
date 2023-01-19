import pymongo
import time

# Connect to the MongoDB server˜
# connectionString = 'mongodb://192.168.31.200:27017/'
connectionString = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(connectionString)

# Get the "assignment" database
db = client["assignment"]

# Get the "zillow" collection
collection = db["311Services"]

start_time = time.perf_counter()

# retrieve the documents
results = collection.find()

# iterate through the cursor and print the documents
# for document in results:
#     print(document)

distinct_values = collection.distinct("Incident Zip")

print(distinct_values)
with open("results311.txt", "w") as file:
    file.writelines(distinct_values)

file.close()
end_time = time.perf_counter()
print(f'Time to execute: {end_time - start_time:0.6f} seconds')
