from bson import ObjectId

from models.category import Category
from config.setup import client


def check_if_category_is_empty(id: str) -> bool:
    category = client.konrad_borowik.categories.find_one({"_id": ObjectId(id)})
    
    parts = client.konrad_borowik.parts.aggregate([
            {
                '$match': {
                    'category': category['name']
                }
            },
        ])
    
    if len(list(parts)) > 0:
        return False
    return True


def check_if_child_catogories_are_empty(id: str) -> bool:
    category = client.konrad_borowik.categories.find_one({"_id": ObjectId(id)})

    sub_categories = client.konrad_borowik.categories.aggregate([
        {
            '$match': {
                'parent_name': category['name']
            }
        }
    ])
    output = False
    for sc in sub_categories:
        output = check_if_category_is_empty(client, sc['_id'])
    return output
        

def input_validation(category: Category):
    # check if name is empty
    if category.name == '':
        raise Exception(f"Category name can't be empty!")

    # check if name is not 'string'
    if category.name == 'string' or category.parent_name == 'string':
        raise Exception(f"Did you mean 'String'?")

    # check if category name already exists 
    categories = client.konrad_borowik.categories.find()
    for c in categories:
        print(c['name'], category.name)
        if category.name in c['name']:
            raise Exception(f'Category already exists!')
