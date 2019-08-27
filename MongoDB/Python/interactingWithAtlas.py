from pymongo import MongoClient
import sys

#from lists import receipts
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
    print(numberOfItemsInDB())
    records.insert_many(jsonFile)
    print('File uploaded')
    print(numberOfItemsInDB())


#how to find one document
def showAllObjects():
    retrivingObjects = list(records.find())
    for i in retrivingObjects:
        print(i)

def returnAllObjects():
    return list(records.find())



def findBetweenDatesRami(name ,firstDate, secondDate):
    lst1 = list(records.find({'$and': [{'$and': [{'item_name': name}, {'date': {'$gt': firstDate, '$lt': secondDate}}]},{'src': 'rami levi'}]}))
    return lst1

def findBetweenDatesYenot(name ,firstDate, secondDate):
    lst1 = list(records.find({'$and': [{'$and': [{'item_name': name}, {'date': {'$gt': firstDate, '$lt': secondDate}}]},{'src': 'yenot bitan'}]}))
    return lst1
#insertMultipleJsons(receipts)

#lst = findBetweenDates('Peach', '00-00-00T00:00:00.000Z', '2019-06-06T00:00:00.000Z')
#for i in lst:
    #print(i)

#lst = findBetweenDatesRami('Tomatoes', '00-00-00T00:00:00.000Z', '2500-06-06T00:00:00.000Z')
#lst2 = findBetweenDatesYenot('Tomatoes', '00-00-00T00:00:00.000Z', '2500-06-06T00:00:00.000Z')

#lst3 = []
#lst3.append(len(lst))
#lst3.append(len(lst2))

# print(lst3)
# import plotly.graph_objects as go
# fig = go.Figure(
#     data=[go.Bar(y=lst3)],
#     layout_title_text="Rami levi left \t\t\t Yenot Bitan  "
# )
# fig.show()
