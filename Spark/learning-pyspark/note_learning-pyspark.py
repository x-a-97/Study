
# [20190429-16:37] chapter 1: Understanding Spark

RDD have 2 sets of parallel operations:
    -transformations
    -actions

Rdd transformation operation are lazy.

DataFrames, immutable collections of data distributed among the nods in a cluster, organized into named columns.

DataFrame = Dataset[Row]

SparkConf
SparkContext
SQLContext
HiveContext
SparkSession
Streaming Context

df = spark.read.format('json').load('py/test/sql/people.json')
df = spark.read.json('py/test/sql/people.json')

[20100429-17:53] Chapter 2: Resilient Distributed Datasets
each transformation is excuted in parallel for enormous increase in speed

# create an RDD
data = sc.parallelize(
	[('Amber', 22), 
	('Alfred', 23), 
	('Skye', 4), 
	('Albert', 12), 
	('Amber', 9)]
	)
# .collect() returns the whole RDD
data.collect()
# or reference a file
# the last parameter specifies the number of paritions the dataset is divided into
data_from_file = sc.textFile('User/drabast/Documents/PySpark_data/VS14MORT.txt.gz', 4)

# worked on my env
data_from_file = sc.textFile('/Users/axa/Study/Spark/VS14MORT.txt.gz', 4)

filesystems supported:
	- NTFS,
	- FAT,
	- HFS+ (Mac OS)
	- HDFS,
	- S3
	- Cassandra

data formats supported:
	- text,
	- parquet,
	- JSON,
	- Hive tables,
	- data from relational. databases can be read using a JDBC driver
	
# RDDs are schema-less data structures
# parallelizing a dataset, the following code snippet is perfectly fine
data_heterogenous = sc.parallelize([
	('Ferrari', 'fast'),
	{'Porsche': 100000},
	['Spain', 'visite', 4504]
	]).collect()

# access the data in the object
data_heterogenous[1]['Porsche']

# when read from a text file, each row from the file forms an element of an RDD.
data_from_file.take(1)

# Lambda expressions
def extractInformation(row):
    import re
    import numpy as np
    selected_indices = [
        2, 3, 5, 6, 7, 9, 10, 11, 12, 123, 14, 15, 16, 17, 18,
        ...
        77, 78, 79, 81, 83, 84, 85, 87, 89
    ]

    record_split = re.compile(
        r'([\s]{19})([0-9]{1})([\s]{40})
        ...
        ([\s]{33})([0-9\s]{3})([0-9\s]{1})([0-9\s]{1})')
    try:
        rs = np.array(record_split.split(row))[selected_indices]
    except:
        rs = np.array(['-99'] * len(selected_indices))
    return rs

/* in the cluster mode, when a job is submitted for execution, the job is sent to the driver(or a master)nodel
 * the driver node creates a DAG for a job and decides which executor(or worker) nodes will run specific tasks
 * the driver then instructs the workes to execute their tasks and return the results to the driver when done.
 */

 # transformations shape your dataset
 # include mapping, filtering, joining, and transcoding the values in your dataset

 # the .distinct(..) transformation
 distinct_geder = data_from_file_conv.map(
 	lambda row: row[5]).distinct()
 distinct_geder.collect()

 # the .sample(...) transformation
 fraction = 0.1
 data_sample = data_from_file_conv.sample(False, fraction, 666)

 # the .leftOuterJoin(...) transformation
 #.leftOuterJoin(...), just like in the SQL world, joins two RDDs based on the values found in both datasets, 
 # and returns records from the left RDD with records from the right one appended in places where the two RDDs match
 rdd1 = sc.parallelize([('a', 1), ('b', 4), ('c', 10)])
 rdd2 = sc.parallelize([('a', 4), ('a', 1), ('b', '6'), ('d', 15)])
 rdd3 = rdd1.leftOuterJoin(rdd2)
 rdd3.collect()

 # the .join(...) method returns only the values intersect between two RDDs,
 rdd4 = rdd1.join(rdd2)

 # the .intersection(..) returns the records that are equal in both RDDs
rdd5 = rdd1.intersection(rdd2) 

# the .repartition(...) transformation
rdd1 = rdd1.repartition(4)
len(rdd1.glom().collect())

# Actions
# the .take(...) method
#  returns the n top rows from a single data partition in contrast 
data_first = data_from_file_conv.take(1)

# take randomized records
# arguments: 1, whether the sampling should be with replacement
#	     2, specifies the number of records to return
#            3, a seed to the pseudo-random number generator
data_take_sampled = data_from_file_conv.takeSample(False, 1, 667)

# the .collect(...) method
# returns all the elements of the RDD to the driver

# the .reduce(...) method
# reduces the elements of an RDD using a specified method
rdd1.map(lambda row: row[1]).reduce(lambda x, y: x + y)

# .reduceByKey(...)
data_key = sc.parallelize(
	[('a', 4), ('b', 3), ('c', 2), ('a', 8), ('d', 2), ('b', 1), ('d', 3)], 4)
data_key.reduceByKey(lambda x, y: x + y).collect()

# the .count(...) method
# counts the number of elements i hte RDD
# .countByKey() mothod get hte counts of distinct keys

# the .saveAsTextFile(...) method
data_key.saveAsTextFile('/Users/drabast/Documents/PySpark_data/data_key.txt')

# the .foreach(...) method
# applies the same function to each element of the RDD
def f(x):
    print(x)
data_key.foreach(f)

[20190505-15:13] Chapter 3: DataFrames
# A DataFrame is an immutable distributed collection of data 
# that is organized into named columns analogous to a table in a relational database. 

# Typically, you will create DataFrames by importing data using SparkSession (or calling spark in the PySpark shell)

# generate the stringJSONRDD RDD
stringJSONRDD = sc.parallelize(("""
	{ "id": "123",
	"name": "Katie",
	"age": 19,
	"eyeColor": "brown"
	}""",
	"""{
	"id":  "234",
	"name": "Michael",
	"age": 22,
	"eyeColor": "green"
	}""",
	"""{
	"id": "345",
	"name": 23,
	"eyeColor": "blue"
	}""")
	)
# convert the RDD into a DataFrame by using the spark.read.json(...)
swimmersJSON = spark.read.json(stringJSONRDD)

# creating a temporary table
swimmerJSON.createOrReplaceTempView("swimmerJSON")

# It is important to note that parallelize, map, and mapPartitions are all RDD transformations.
# spark.read.json (in this case), are not only the RDD transformations, 
# but also the action which converts the RDD into a DataFrame

# dataframe api query
# Note that creating the temporary table is a DataFrame transformation 
# and not executed until a DataFrame action is executed 
# (for example, in the SQL query to be executed in the following section).
swimmersJSON.show()

# SQL query
spark.sql("select * from swimmersJSON").collect()

# 2 methods for converting exsiting RDDs  to DataFrames:
# 1. inferring the schema using reflection
# 2. programmatically specifying hte schema

# initially, row objects are constructed by passing a list of key/value pairs as **kwags to the row class
# spark sql converts this RDD of row objects into a DataFrame, where the keys are the columns 
# and the data types are inferred by sampling the data

# Print the schema
swimmersJSON.printSchema()

# programmatically specifying the schema
    # import types
    from pyspark.sql.types import *

    # generate comma delimited data
    stringCSVRDD = sc.parallelize([
    (123, 'Katie', 19, 'brown'),
    (234, 'Michael', 22, 'green'),
    (345, 'Simone', 23, 'blue')
    ])

    # specify schema
    # StructField(name, datatype, nullable)
    schema = StructType([
    StructField("id", LongType(), True),
    StructField("name", StringType(), True),
    StructField("age",LongType(), True),
    StructField("eyeColor", StringType(), True)
    ])

    # Apply the schema to the RDD and Create DataFrame
    swimmers = spark.createDataFrame(stringCSVRDD, schema)

    # print the schema
    swimmers.printSchema()

# craetes a temporary view using hte DataFrame
swimmers.createOrReplaceTempView("swimmers")

# Querying with the DataFrame API

# number of rows
swimmers.count()

# running filter statements
swimmers.select("id", "age").filter("age = 22").show()

swimmers.select("name", "eyeColor").filter("eyeColor like 'b'").show()

# Querying with SQl
spark.sql("select count(1) from swimmers").show()

# running filter statement using SQL where Clauses
spark.sql("select id, age from swimmers where age = 22").show()
spark.sql("select name, eyeColor from swimmers where eyeColor like 'b%'").show()

[20190505-17:12] Chapter 4: prepare data for modeling

# All data is dirty, until you have tested and proven the your self that your data is in a clean state, you should neither turst nor use it
# to prepare the data
# - recognize and handle duplicates, missing observations and outliers
# - Calculate descriptive statistics and correlations
# - Visualize your data withe matplotlib and Bokeh

# Duplicates

# compare the counts of the full dataset with he one after running a .distinct() method
print('Count of rows: {0}'.format(df.count()))
print('Count of distinct rows: {0}'.format(df.distinct().count()))

# if these two numbers differ, then 
df = df.dropDuplicate()

# check whether there are any duplicates in the data irrespective od ID
print('Count of ids:  {0}'.format(df.count()))
print('Count of distinct ids: {0}'.format(
    df.select([ c for c in df.columns if c != 'id' 
    ]).distic().count())
)

df = df.dropDuplicates(subset=[
	c for c in df.columns if c != 'id'
	])

# to calculate the total and distinct number of IDs in on step
import pyspark.sql.function as fn
df.agg(
fn.count('di').alias('count'),
fn.countDistinct('id).alias('distinct')).show()

# impute a mean, median  or other calculated value
mean = df_miss_no_income.agg(*[fn.mean(c).alias(c) for c in df_missing_no_income.columns if c != 'gender']).toPandas().to_dict('records')[0]
means['gender'] = 'missing'
df_miss_no_income.fillna(means).show()

# outliers: observations that deviate significantly from the distrubution of the rest of the sample
df_outliers = spark.createDataFrame([
	(1, 143.5, 5.3, 28),
	(2, 154.2, 5.5, 45),
	(3, 342.3, 5.1, 99),
	(4, 144.5, 5.5, 33),
	(5, 133.2, 5.4, 54),
	(6, 124.1, 5.1, 21),
	(7, 129.2, 5.3, 42),
	], ['id', 'weight', 'height', 'age'])

# calculate the lower and upper cut off points for each feature
cols = ['weight', 'height', 'age']
bounds = {}

for col in cols:
	quantiles = df_outliers.approxQuantile(
		col, [0.25, 0.75], 0.05
	)
	IQR = quantiles[1] - quantiles[0]

	bounds[col] = [
		quantiles[0] - 1.5 * IQR,
		quantiles[1] + 1.5 * IQR
		]



