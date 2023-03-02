import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb

def brevet_insert(start_time, brevet_dist, checkpoints):
    pass

def brevet_find():
    # return start_time, brevet_dist, checkpoints
    pass
