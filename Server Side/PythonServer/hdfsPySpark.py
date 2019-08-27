import json
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession
from snakebite.client import Client
from six.moves import reduce
from pyspark.sql import functions as F
from pyspark.sql import Window

import pymongo
from pymongo import MongoClient


def collectDataFromHDFS():
    conf = SparkConf().setAppName("myFirstApp").setMaster("local")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    HADOOP_HOST = "localhost"
    HADOOP_PORT = 9000
    hadoop_client = Client(HADOOP_HOST, HADOOP_PORT, use_trash=False)
    sql = SQLContext(sc)
    ls = []
    for x in hadoop_client.ls(['/']):
        #print(x['path'])
        csvDataframe = sqlContext.read.format("csv").option("header", "true").option("inferschema", "true").option("mode", "DROPMALFORMED").load("hdfs://localhost:9000"+x['path'])
        ls.append(csvDataframe)
    print(ls)
    df = ls[1][['item_name', 'date', 'price_for_UNIT/KG']].union(ls[0][['item_name', 'date', 'price_for_UNIT/KG']])
    df.show()

    return ls



    #sorted_list_df = df.groupBy("item_name").agg(F.collect_list(F.col("date")).alias("date_list"),
    #F.collect_list(F.col("price_for_UNIT/KG")).alias("prics_list"))
    #sorted_list_df.show()

