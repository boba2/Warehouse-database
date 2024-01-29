from fastapi import APIRouter
from bson import ObjectId

from models.category import Category
from config.setup import client
from schemas.category import categoryEntity, categoriesEntity


category = APIRouter()

@category.get('/')
async def find_all_categories():
    return categoriesEntity(client.konrad_borowik.categories.find())


@category.post('/')
async def create_category(category: Category):
    client.konrad_borowik.categories.insert_one(dict(category))
    return categoriesEntity(client.konrad_borowik.categories.find())


@category.put('/')
async def update_category(query: dict, new_value: str):
    for q in query.items():
        key, value = q

    client.konrad_borowik.categories.find_one_and_update(
        {
            key: value
        },
        {
            "$set": {key: new_value} 
        }
    )
    return categoriesEntity(client.konrad_borowik.categories.find())


@category.delete('/')
async def delete_category(query: dict):
    client.konrad_borowik.categories.find_one_and_delete(query)
    return categoriesEntity(client.konrad_borowik.categories.find())
