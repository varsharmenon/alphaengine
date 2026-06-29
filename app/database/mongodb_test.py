from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["alphaengine"]

collection = db["test"]

collection.insert_one({
    "name": "layla",
    "age": 16
})

for document in collection.find():
    print(document)