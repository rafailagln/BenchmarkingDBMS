#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import dask.dataframe as dd

# create a Dask DataFrame
df = dd.read_csv('C:\\Users\\30693\\OneDrive\\Documents\\jj\\zillow.csv', header=0)


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

def extractid(val):
  match = re.search("(\d+)_zpid/$",val)
  try:
      return int(match.group(1))
  except:
      return  0

def extractpcode(val):
      try:
        return '%05d' % int(val)
      except:
        return ''


# apply your UDFs to the DataFrame and create new columns with the extracted data
df = df.map_partitions(
    lambda df: 
    df.assign(price=df.price.apply(extractprice_sell))
    .assign(title=df.title.apply(extract_type))
    .assign(id=df.url.apply(extractid))
    .assign(code=df.postal_code.apply(extractpcode))
    .assign(bedrooms=df["facts and features"].apply(extractbd))
    .assign(bathrooms=df["facts and features"].apply(extractba))
    .assign(sqfeet=df["facts and features"].apply(extractsqfeet))
    )

df = df[
    (df.price.between(100000, 20000000)) 
    & (df.bedrooms < 10) 
    #& (df.offer.isin(['sale', 'rent', 'sold', 'forclosed']))
    & (df.title == 'condo')
    & (df.code.notnull())
    & (df.sqfeet.notnull())
    & (df.bathrooms.notnull())
    & (df.bedrooms.notnull())
    & (df.price.notnull())]

# run your query on the DataFrame and specify both columns, then compute the results and display them
result = df[['price','title','code','bathrooms']].compute()
print (result.head(20))
