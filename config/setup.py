import json
from pymongo import MongoClient
from typing import List


def read_file(filename: str) -> List:
    with open(f'config/data/{filename}') as f:
        data = json.load(f)
    f.close()
    return data
    

dummy_categories = read_file('dummy_categories.json')
dummy_parts = read_file('dummy_parts.json')
# mongodb+srv://rekrutacja:BZijftwEru0oELxT@cluster11.yxu8n2k.mongodb.net/
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