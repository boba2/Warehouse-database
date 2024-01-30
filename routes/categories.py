from fastapi import APIRouter
from bson import ObjectId

from models.category import Category
from config.setup import client
from schemas.category import categoryEntity, categoriesEntity
from routes.utils.category_utils import (
    check_if_category_is_empty,
    check_if_child_catogories_are_empty
)

router = APIRouter()


@router.get('/categories')
async def find_all_categories():
    return categoriesEntity(client.konrad_borowik.categories.find())


@router.post('/categories')
async def create_category(category: Category):
    client.konrad_borowik.categories.insert_one(dict(category))
    return categoriesEntity(client.konrad_borowik.categories.find())


@router.put('/categories/{id}')
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


@router.delete('/categories/{id}')
async def delete_category(id):
    if check_if_category_is_empty(client, id) and check_if_child_catogories_are_empty(client, id):
        client.konrad_borowik.categories.find_one_and_delete({"_id": ObjectId(id)})
        return f'Category deleted.'
    else:
        return f'This category is not empty.'
