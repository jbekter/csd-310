from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.qcdpi.mongodb.net/test"

client = MongoClient(url)

db = client.pytech

print("\n Pytech Collection List")
print(db.list_collection_names())

