""" 
    Title: mongodb_test.py
    Author: James Smith
    Date: 4/10/2021
    Assignment: Module 5.2
"""

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.7qjgy.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print("\n -- Pytech Collection List --")
print(db.list_collection_names())
input("\n\n  End of program, press any key to exit... ")