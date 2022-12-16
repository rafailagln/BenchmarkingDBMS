import math
import re
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# create a Spark session
spark = SparkSession.builder.appName('MyApp').getOrCreate()

# read the CSV file as a DataFrame
df = spark.read.csv('zillow.csv', header=True)


# define your UDFs
def extractprice_sell(val):
    try:
        return int(val[1:].replace(',', ''))
    except:
        return -1


extractprice_sell.registered = True


def extract_type(val):
    try:
        t = val.lower()
        type = 'unknown'
        if 'condo' in t or 'apartment' in t:
            type = 'condo'
        if 'house' in t:
            type = 'house'
        return type
    except:
        return 'null'


extract_type.registered = True

def extractbd(val):
      try:
        max_idx = val.find(' bd')
        if max_idx < 0:
            max_idx = len(val)
        s = val[:max_idx]
        split_idx = s.rfind(',')
        if split_idx < 0:
            split_idx = 0
        else:
            split_idx += 2
        r = s[split_idx:]
        return int(r)
      except:
        return -1
extractbd.registered = True

def extractba(val):
      try:
        max_idx = val.find(' ba')
        if max_idx < 0:
            max_idx = len(val)
        s = val[:max_idx]
        split_idx = s.rfind(',')
        if split_idx < 0:
            split_idx = 0
        else:
            split_idx += 2
        r = s[split_idx:]
        ba = math.ceil(2.0 * float(r)) / 2.0
        return int(ba)
      except:
        return -1

extractba.registered = True

def extractsqfeet(val):
      try:
        max_idx = val.find(' sqft')
        if max_idx < 0:
            max_idx = len(val)
        s = val[:max_idx]
        split_idx = s.rfind('ba ,')
        if split_idx < 0:
            split_idx = 0
        else:
            split_idx += 5
        r = s[split_idx:]
        r = r.replace(',', '')
        return int(r)
      except:
        return -1

extractsqfeet.registered = True

def extractid(val):
  match = re.search("(\d+)_zpid/$",val)
  try:
      return int(match.group(1))
  except:
      return  0

extractid.registered = True

def extractpcode(val):
      try:
        return '%05d' % int(val)
      except:
        return ''
extractpcode.registered = True


# register your UDFs
extract_price_udf = udf(extractprice_sell, returnType=StringType())
extract_type_udf = udf(extract_type, returnType=StringType())
extract_bedrooms_udf = udf(extractbd, returnType=StringType())
extract_bathrooms_udf = udf(extractba, returnType=StringType())
extract_sqtfeets_udf = udf(extractsqfeet, returnType=StringType())
extract_id_udf = udf(extractid, returnType=StringType())
extract_code_udf = udf(extractpcode, returnType=StringType())

# apply your UDFs to the DataFrame and create new columns with the extracted data
df = df.withColumn('title', extract_type_udf('title'))
df = df.withColumn('price', extract_price_udf('price'))
df = df.withColumn('bedrooms', extract_bedrooms_udf('facts and features'))
df = df.withColumn('bathrooms', extract_bathrooms_udf('facts and features'))
df = df.withColumn('sqfeets', extract_sqtfeets_udf('facts and features'))
df = df.withColumn('id', extract_id_udf('url'))
df = df.withColumn('code', extract_code_udf('postal_code'))


# run your query on the DataFrame and specify both columns
df.select('id','code','title', 'price', 'bedrooms', 'bathrooms','sqfeets').show()

