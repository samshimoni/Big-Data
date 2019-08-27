from pymongo import MongoClient
from lists import receipts
#Connects to Atlas

client = MongoClient('mongodb://samshimoni:1234@rest-shard-00-00-bu6z1.mongodb.net:27017,rest-shard-00-01-bu6z1.mongodb.net:27017,rest-shard-00-02-bu6z1.mongodb.net:27017/test?ssl=true&replicaSet=rest-shard-0&authSource=admin&retryWrites=true&w=majority')

#enters 'BigData' Database
db = client.get_database('BigData')

records = db.Receipts
#check how many documents I have

def numberOfItemsInDB():
    number = records.count_documents({})
    return number

#how to insert one document
    def insertJsonDoc(jsonFile):
        records.insert_one(jsonFile)

#How to insert multiple documents
def insertMultipleJsons(jsonFile):
    records.insert_many(jsonFile)

#how to find one document
def showAllObjects():
    retrivingObjects = list(records.find())
    for i in retrivingObjects:
        print(i)

def returnAllObjects():
    return list(records.find())



def findBetweenDates(name ,firstDate, secondDate):
    lst1 = list(records.find({'$and': [{'item_name': name}, {'date': {'$gt': firstDate, '$lt': secondDate}}]}))
    return lst1


lst = findBetweenDates('Peach', '00-00-00T00:00:00.000Z', '2019-06-06T00:00:00.000Z')
print(lst)




