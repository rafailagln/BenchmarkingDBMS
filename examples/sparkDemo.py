#!/usr/bin/python
# -*- coding: utf-8 -*-
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

# register your UDFs
extract_price_udf = udf(extractprice_sell, returnType=StringType())
extract_type_udf = udf(extract_type, returnType=StringType())

# apply your UDFs to the DataFrame and create new columns with the extracted data
df = df.withColumn('price', extract_price_udf('price'))
df = df.withColumn('title', extract_type_udf('title'))

# run your query on the DataFrame and specify both columns
df.select('price', 'title').show()