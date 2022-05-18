import json
from pymongo import MongoClient
import os

dir_list = os.listdir('./db')

client = MongoClient('localhost', 27017)
db = client['signode']

# with open('./db/markham.json') as f:
#     file_data = json.load(f)

for _ in dir_list:
    collect = os.path.basename(_).split(".")[0]
    with open(f'./db/{collect}.json') as f:
        data = json.load(f)
        db[_].insert_many(data)