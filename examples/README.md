# Examples

## Description

Here are 2 sample queries in python with Spark & Dask. Both queries read data from a csv file and execute the query by using the provided udfs.

## Execution results

With [zillow.csv](https://github.com/athenarc/YeSQL/blob/main/data/zillow.csv) results are

**[Dask](https://github.com/rafailagln/DBS_assignment/blob/main/examples/daskDemo.py)**

````
      price  title
0    342000  condo
1   1700000  condo
2    336500  condo
3   9950000  house
4    479000  condo
5    899000  house
6    397300  condo
7    619900  condo
8    850000  condo
9    649900  condo
10   625000  condo
11    80000  condo
12  1425000  condo
13   199000  condo
14  1200000  house
15   499950  condo
16   739000  condo
17  1119000  house
18  1699000  house
19   589000  house
````
-------

**[Spark](https://github.com/rafailagln/DBS_assignment/blob/main/examples/sparkDemo.py)**

````
+-------+-----+                                                                 
|  price|title|
+-------+-----+
| 342000|condo|
|1700000|condo|
| 336500|condo|
|9950000|house|
| 479000|condo|
| 899000|house|
| 397300|condo|
| 619900|condo|
| 850000|condo|
| 649900|condo|
| 625000|condo|
|  80000|condo|
|1425000|condo|
| 199000|condo|
|1200000|house|
| 499950|condo|
| 739000|condo|
|1119000|house|
|1699000|house|
| 589000|house|
+-------+-----+
only showing top 20 rows
````