#!/usr/bin/python
# -*- coding: utf-8 -*-
import dask.dataframe as dd

# create a Dask DataFrame
df = dd.read_csv('zillow.csv', header=0)


# define your UDFs
def extractprice_sell(val):
    try:
        return int(val[1:].replace(',', ''))
    except:
        return -1


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


# apply your UDFs to the DataFrame and create new columns with the extracted data
df = df.map_partitions(lambda df: \
                       df.assign(price=df.price.apply(extractprice_sell)).assign(title=df.title.apply(extract_type)))

# run your query on the DataFrame and specify both columns, then compute the results and display them
result = df[['price', 'title']].compute()
print result.head(20)