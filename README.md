# DBS_assignment
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

#### Datasets

* **Weblogs**: Data from monitoring a Apache HTTP Server
	* Data
		1. Data from monitoring a website &rarr; [weblogs.small.csv](https://github.com/tuplex/tuplex/blob/master/tuplex/test/resources/weblogs.small.csv "weblogs.small.csv")
		2. List of IPs that are concerned maliciously &rarr; [bad_ips_all.txt](https://github.com/tuplex/tuplex/blob/master/tuplex/test/resources/bad_ips_all.txt "bad_ips_all.txt")
	* Query: [runtuplex.py](https://github.com/tuplex/tuplex/blob/master/benchmarks/logs/runtuplex.py "runtuplex.py") returns all the records of a file (e.g. weblogs.small.csv) that have a matching column (in our case the IP address) with another file. 
	* Analyzing [runtuplex.py](https://github.com/tuplex/tuplex/blob/master/benchmarks/logs/runtuplex.py "runtuplex.py") ([runpyspark.py](https://github.com/tuplex/tuplex/blob/master/benchmarks/logs/runpyspark.py) is the exact same "query" with [runtuplex.py](https://github.com/tuplex/tuplex/blob/master/benchmarks/logs/runtuplex.py "runtuplex.py") on PySpark)
		1. line 65-118: are functions which take one csv column, do some queries (this should be transformed in UDFs in every DB)
		2. line 236: how the flows go, the sequence and applies filters 
			pipeline_type (regex, strip, split_regex, split)
		3. line 250: should be definitely run after 246
		4. line 283: join on IPs (weblogs.small.csv & bad_ips_all.txt)
		5. line 285: final select and create output file
		6. you can change sequence, if this does not affect the result (if one function needs as input the result of previous function)
		7. If you want to run: 
			````
			$ sudo apt update
			$ sudo apt install python3-pip
			$ pip install tuplex
			$ wget https://raw.githubusercontent.com/tuplex/tuplex/master/benchmarks/logs/runtuplex.py https://raw.githubusercontent.com/tuplex/tuplex/master/tuplex/test/resources/pipelines/weblogs/ip_blacklist.csv https://raw.githubusercontent.com/tuplex/tuplex/master/tuplex/test/resources/pipelines/weblogs/logs.sample.txt
			$ python3 runtuplex.py --path logs.sample.txt --ip_blacklist_path ip_blacklist.csv --pipeline_type split_regex 
			```` 
			The output file should only have 1 line 
`1.1.209.108,01/Jan/2000:03:01:24 -0500,GET,/research/finance/,HTTP/1.0,304,0`

* **Zillow**: Real estate data, records from apartments, adds
	* Data: [zillow.csv](https://github.com/athenarc/YeSQL/blob/main/data/zillow.csv)
	* Query: [zillow.sql](https://github.com/athenarc/YeSQL/blob/main/sql_queries/zillow.sql)
	* UDFs: [zillow.py](https://github.com/athenarc/YeSQL/blob/main/udfs/zillow.py)
	* ~~we will need to transform UDFs for all DBs (not pyspark, dask)~~
    * use zillow query as example
    * create extension in order to support python based on documetion
    * (?) For Spark & Dask -> we have to create a python query similar to [runpyspark.py](https://github.com/tuplex/tuplex/blob/master/benchmarks/logs/runpyspark.py) and [rundask.py](https://github.com/tuplex/tuplex/blob/master/benchmarks/logs/rundask.py). Look [here](https://github.com/rafailagln/DBS_assignment/tree/main/examples) for examples.
    * (?) For other DBs -> we have to implement the UDFs and execute the given query in every db. 

    
* Datasets are sample, we can generate sample data with a randomized way

#### TODO:

* we should transform to SQL lines 235-252, 283-285 functions 65-118 should be executed as UDFs inside the DB and then called with SQL as UDFs ([runtuplex.py](https://github.com/tuplex/tuplex/blob/master/benchmarks/logs/runtuplex.py "runtuplex.py")). 

* all should be done in one SQL query (SELECT FROM WHERE) FROM: table that are join where: UDFS might be necessary to have subqueries seperate queries are not the most efficient solution -> nested queries

* UDFs used will have the same body with this attached


* vertica: we will not place the UDF in terminal, save in .py file and load the file e.g. for vertica [PythonExampleAdd2Ints](https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/ExtendingVertica/UDx/ScalarFunctions/Python/PythonExampleAdd2Ints.htm)