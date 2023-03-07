import os
import pprint
from pymongo import MongoClient
import time 

# Implement mongodb access library

client = MongoClient(os.getenv('MONGO_STR'))


# db = client['todo-bot']
# collection = db.test

# test_document = {
#     "name": "Tim321",
#     "type": "Test2"
# }

# inserted_id = collection.insert_one(test_document)

