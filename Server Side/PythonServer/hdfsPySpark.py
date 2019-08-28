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

    df = ls[1].union(ls[0])
    for i in range(2, 6):
        df = df.union(ls[i])
    #print(ls)
    #df = ls[1][['item_name', 'date', 'price_for_UNIT/KG']].union(ls[0][['item_name', 'date', 'price_for_UNIT/KG']])
    df.show()

    sorted_list_df1 = df.groupBy("item_name").agg(F.collect_list(F.col("date")).alias("date_list")
                                                  , F.collect_list(F.col("src")).alias("comp")
                                                  , F.collect_list(F.col("price_for_UNIT/KG")).alias("prics_list")
                                                  , F.collect_list(F.col("amount_KG")).alias("kg")
                                                  , F.collect_list(F.col("amount_UNIT")).alias("unit")
                                                  )

    sorted_list_df1.show()

    #sorted_list_df1.show()
    sorted_list_df = df.groupBy("item_name").agg({"price_for_UNIT/KG": "min"})

    sorted_list_df.show()
    inner_join = df.join(sorted_list_df, sorted_list_df['item_name'] == df['item_name'], how='inner')
    inner_join = inner_join.filter(inner_join["price_for_UNIT/KG"] == inner_join['min(price_for_UNIT/KG)'])

    inner_join.show()
    mapa = sorted_list_df.toJSON().map(lambda j: json.loads(j)).collect()
    client = MongoClient('mongodb://samshimoni:1234@rest-shard-00-00-bu6z1.mongodb.net:27017,rest-shard-00-01-bu6z1.mongodb.net:27017,rest-shard-00-02-bu6z1.mongodb.net:27017/test?ssl=true&replicaSet=rest-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = client.get_database('BigData')
    records = db.Receipts

    #print(type(mapa[0]))
    print(mapa)
    print(type(mapa))
    print(records.count_documents({}))
    #records.insert_many(mapa)
    #print(records.count_documents({}))


    return ls




