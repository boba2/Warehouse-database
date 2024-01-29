from fastapi import APIRouter
from bson import ObjectId

from models.category import Category
from config.setup import client
from schemas.category import categoryEntity, categoriesEntity
from routes.utils.category_utils import check_if_category_is_empty


category = APIRouter()

@category.get('/')
async def find_all_categories():
    return categoriesEntity(client.konrad_borowik.categories.find())


# @category.get('/{key: value}')
# async def find_category_by_value(value: str):
#     return categoryEntity(client.konrad_borowik.categories.find_one(
#         {}, {value}
#     ))


@category.post('/')
async def create_category(category: Category):
    client.konrad_borowik.categories.insert_one(dict(category))
    return categoriesEntity(client.konrad_borowik.categories.find())


@category.put('/{id}')
async def update_whole_category(id, category: Category):
    client.konrad_borowik.categories.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {
            "$set": dict(category)
        }
    )
    return categoryEntity(client.konrad_borowik.categories.find_one({"_id": ObjectId(id)}))


# @category.put('/{key: value}')
# async def update_one_element_in_category(key: str, value: str, new_value: str):
#     client.konrad_borowik.categories.find_one_and_update(
#         {
#             key: value
#         },
#         {
#             "$set": {key: new_value} 
#         }
#     )
#     return categoryEntity(client.konrad_borowik.categories.find())


@category.delete('/{id}')
async def delete_category(id):
    if check_if_category_is_empty(client, id):
        client.konrad_borowik.categories.find_one_and_delete({"_id": ObjectId(id)})
        return f'Category deleted.'
    else:
        return f'This category is not empty.'