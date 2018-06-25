from pyspark.sql.functions import col
from pyspark.sql import SQLContext, SparkSession
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from collections import namedtuple
from pyspark.ml import PipelineModel
# from pyspark.sql.functions import desc
import pandas as pd

sc = SparkContext("local[2]", "Streaming App")
lr=PipelineModel.load("logreg.model")
ssc = StreamingContext(sc, 10)
sqlContext = SQLContext(sc)
#ssc.checkpoint( "file:/home/ubuntu/tweets/checkpoint/")

socket_stream = ssc.socketTextStream("172.31.3.247", 5512) # Internal ip of  the tweepy streamer

lines = socket_stream.window(20)
#lines.pprint()
fields = ("SentimentText")
Tweet = namedtuple( 'Tweet', fields )

def getSparkSessionInstance(sparkConf):
    	if("sparkSessionSingletonInstance" not in globals()):
       		globals()["sparkSessionSingletonInstance"] = SparkSession \
            	.builder \
            	.config(conf=sparkConf) \
            .	getOrCreate()
    	return globals()["sparkSessionSingletonInstance"]

def do_something(time, rdd):
	print("========= %s =========" % str(time))
    
	# Get the singleton instance of SparkSession
	spark = getSparkSessionInstance(rdd.context.getConf())

	# Convert RDD[String] to RDD[Tweet] to DataFrame
	rowRdd = rdd.map(lambda w: Tweet(w))
	linesDataFrame = spark.createDataFrame(rowRdd)

	# Creates a temporary view using the DataFrame
	linesDataFrame.createOrReplaceTempView("tweets")

	# Do tweet character count on table using SQL and print it
	lineCountsDataFrame = spark.sql("select SentimentText as text from tweets")
	lrp=lr.transform(lineCountsDataFrame)
	ft = ["text","prediction"]
	lrp_s=lrp.select([column for column in lrp.columns if column in ft])
	lrp_s.show(n=10)
	s=lrp_s.toPandas()
	
	s.to_csv('Tweets3.csv', mode='a', header=False, index = False)
	t_in_csv = pd.read_csv('Tweets3.csv', index_col = False, encoding = 'unicode_escape')
	if (len(t_in_csv)>3000):
		ssc.stop()
	#lineCountsDataFrame.show()
	#lineCountsDataFrame.coalesce(1).write.format("com.databricks.spark.csv").save("dirwithcsv")

	print("terminate")


# key part!
lines.foreachRDD(do_something)

ssc.start()
ssc.awaitTermination()
