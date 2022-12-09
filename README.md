# DBMS_assignment
This is a repo for Database Management Systems course assignment.


## Project 5 Description:
Scope: familiarity with big data platforms, develop analytical skills, engineering flavor

Benchmarking big data systems for data science queries

__In__
* SQL with Python UDFs

__Out__
* Experimental analysis

__Data__
* Platforms: SQLite, DuckDB, PostgreSQL, MonetDB, Vertica (community edition),
Spark, MongoDB, Dask
* Datasets: zillow, flights, logs, tpch, 311
* Dimensions: parallelism (single-threaded vs multi-threaded), caches (hot/cold),
data size


__Steps__
* Investigate and deploy platforms
* Run experiments




### Call 24/11
DB/Tool per member

| DB/tool        | Member|
| --------------- |:-------------:| 
| MongoDB         | Rafaila       | 
| Vertica         | John N.       | 
| Spark, Dask     | George        |
|Postgres, Monetdb| John K.       |

Final report should be like section 6 of this paper: [YeSQL: “You extend SQL” with Rich and Highly Performant
User-Defined Functions in Relational Databases](https://www.vldb.org/pvldb/vol15/p2270-foufoulas.pdf)


### Call 09/12

* algorithms: https://github.com/tuplex/tuplex/blob/master/benchmarks/logs/runtuplex.py (this should be transformed)
analysis on apache server's logs, got the IPs, resources etc. 

* datasets:

    1a. [Weblogs tuplex](https://github.com/tuplex/tuplex/blob/master/tuplex/test/resources/weblogs.small.csv)

    Description: data from monitoring a website

    1b. [Malicious IPs](https://github.com/tuplex/tuplex/blob/master/tuplex/test/resources/bad_ips_all.txt)
    Description: 
    list of IPs that are concerned malicious 

    2. [zillow](https://github.com/athenarc/YeSQL/blob/main/data/zillow.csv)
        + description: real estate data, records from apartments' adds
        + query: [zillow.sql](https://github.com/athenarc/YeSQL/blob/main/sql_queries/zillow.sql)
        + UDFS: [zillow.py](https://github.com/athenarc/YeSQL/blob/main/udfs/zillow.py)
        + we will need to transform UDFs for all DBs (not pyspark, dask)
        + use zillow query as example
        + create extension in order to support python based on documetion
    
* datasets are sample, we can generate sample data with a randomized way

* Analyzing [runpyspark.py](https://github.com/tuplex/tuplex/blob/master/benchmarks/logs/runpyspark.py) file
    - line 65-118: are functions which take one csv column, do some queries 

    - line 236: how the flows go, the sequence and applies filters 

    - you can change sequence, if this does not affect the result (if one function needs as input the result of prev function)

    - line 250 should be definitely run after 256

    - line 283 join on IPs from dataset 2 

    - line 285 final select

TODO:

* we should transform to SQL lines 235-252, 283-285
functions 65-118 should be executed as UDFs inside the DB and then called with SQL as UDFs. 

* all should be done in one SQL query (SELECT FROM WHERE)
FROM: table that are join 
where: UDFS
might be necessary to have subqueries
seperate queries are not the most efficient solution -> nested queries 

* UDFs used will have the same body with this attached


* vertica: we will not place the UDF in terminal, save in .py file and load the file 
e.g. for vertica [PythonExampleAdd2Ints](https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/ExtendingVertica/UDx/ScalarFunctions/Python/PythonExampleAdd2Ints.html)

