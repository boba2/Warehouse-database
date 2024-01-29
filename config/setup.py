import json
from pymongo import MongoClient
from typing import List

# from .database import Database


def read_file(filename: str) -> List:
    with open(f'config/data/{filename}') as f:
        data = json.load(f)
    f.close()
    return data
    

dummy_categories = read_file('dummy_categories.json')
dummy_parts = read_file('dummy_parts.json')
# database = Database(dummy_categories, dummy_parts)
client = MongoClient(
    host='localhost',
    port=27017,
)

if not 'konrad_borowik' in client.list_database_names():
    db = client['konrad_borowik']
    categories = db['categories']
    parts = db['parts']

    categories.insert_many(dummy_categories)
    parts.insert_many(dummy_parts)