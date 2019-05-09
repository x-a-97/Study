# init spark
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)

# create RDD
lines = sc.parallelize(["pandas", "i like pandas"])
lines = sc.textFile("/path/to/README.md")

# filter() transformation
input RDD = sc.textFile("log.txt")
errorsRDD = inputRDD.filter(lambda x: "error" in x)

# union() transformation
errorsRDD = inputRDD.filter(lambda x: "error" in x)
warningsRDD = inputRDD.filter(lambda x: "warining" in x)
badLinesRDD = errorsRDD.union(warningsRDD)

# 使用行动操作对错误进行计数
print("Input had " + badLinesRDD.count() + " concerning lines")
print("Here are 10 examples:")
for line in badLinesRDD.take(10):
	print(line)

# 在Python 中传递函数
word = rdd.filter(lambda s: "error" in s)

def containsError(s):
	return "error" in s
word = rdd.filter(containsError)

# 传递不带字段引用的python函数
class WordFunctions(object):
	def getMatchesNoReference(self, rdd):
		query = self.query
		return rdd.filter(lambda x: query in x)

# map()
nums = sc.parallelize([1, 2, 3, 4])
squared =  nums.map(lambda x: x * x).collect()
for num in squared:
	print("%i  " % (num))

# flatMap(), 对每个输入元素生成多个输出元素 
# 返回值序列的迭代器
lines = sc.parallelize(["hello world", "hi"])
words = lines.flatMap(lambda line: line.split(" "))
words.first()

# 集合操作

# 行动操作
# reduce()
sum = rdd.reduce(lambda x, y: x + y)

# aggregate()
# 期待返回了类型的初始值, 一个函数把RDD中的元素合并起来 放入累加器, 第二个 函数将累加器两两合并
sumCount = nums.aggregate((0, 0), 
			(lambda acc, value: (acc[0] + value, acc[1] + 1),
			(lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1]))))
return sumCount[0]/float(sumCount[1])

# 键值对操作
# 创建 pari RDD
paris = lines.map(lambda x: (x.split(" ")[0], x))

# 对第二个元素进行筛选
result = pairs.filter(lambda keyValue: len(keyValue[1]) < 20)

# 计算每个键对应的平均值
rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
rdd = sc.textFile("s3://...")
words = rdd.flatMap(lambda  x: x.split(" "))
result = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

# combineByKey() 求每个键对应的 平均值
 sumCount = nums.combineByKey((lambda x: (x, 1)),
 								(lambda x, y: (x[0] + y, x[1] + 1)),
 								(lambda x, y: (x[0] + y[0], x[1] + y[1])))
 sumCount.map(lambda key, xy: (key, xy[0]/xy[1])).collectAsMap()

 # 以字符串顺序对整数进行自定义排序
 rdd.sortByKey(ascending=True, numPartitions=None, keyfunc = lambda x: str(x))

 # 读取文本文件
 input = sc.textFile("file:///home/holden/repos/spark/README.md")

 # 保存文本文件
 result.saveAsTextFile(outputFile)

 # 读取JSON
 import json
 data = input.map(lambda x: json.loads(x))

 # 保存JSON
 (data.filer(lambda x: x["lovesPandas"]).map(lambda x: json.dumps(x))
 	.saveAsTextFile(outputFile))

# 共享变量
# 累加器 
file = sc.textFile(inputFile)
blankLines = sc.accumulator(0) # 累加器

def extractCallSigns(line):
	global blankLines
	if (line == ""):
		blankLines += 1
	return line.split(" ")
callSigns = file.flatMap(extractCallSigns)
callSigns.saveAsTextFile(outputDir + "/callsigns")
print("Blank lines: %d" % blankLines.value)

# 广播变量
signPrefixes =  sc.broadcast(loadCallSignTable())

def processSignCount(sign_count, signPrefixes):
	country = lookupCountry(sign_count[0], signPrefixes.value)
	count = sign_count[1]
	return (country, count)

countryContactCounts = (contactCounts.map(processSignCount).reduceByKey((lambda x, y: x + y)))
countryContactCounts.saveAsTextFile(outputDir + "/countries.txt")


