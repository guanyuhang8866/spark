import pymongo
import time
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['test']
for i in range(10):
    mydb.news.insert({"num":i,"createData":time.time()*1000})

