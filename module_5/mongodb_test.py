""" 
    Title: mongodb_test.py
    Author: Josh Boettcher
    Date: 10 November 2021
    Description: Test program for connecting to a 
                 MongoDB Atlas cluster
"""

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.qcdpi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names())
