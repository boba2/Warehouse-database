from fastapi import APIRouter
from bson import ObjectId

from app.models.category import Category
from app.config.setup import client
from app.schemas.category import categoryEntity, categoryEntities
from app.routes.utils.category_utils import (
    check_if_category_is_empty,
    check_if_child_catogories_are_empty,
    input_validation
)


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.get('/')
async def find_all_categories():
    return categoryEntities(client.konrad_borowik.categories.find())


@router.post('/')
async def create_category(category: Category):
    try:
        input_validation(category)
        client.konrad_borowik.categories.insert_one(dict(category))
        return categoryEntities(client.konrad_borowik.categories.find())
    except Exception as e:
        return f'Caught this error: {e}'


@router.put('/{id}')
async def update_category(id, category: Category):
    client.konrad_borowik.categories.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {
            "$set": dict(category)
        }
    )
    return categoryEntity(client.konrad_borowik.categories.find_one({"_id": ObjectId(id)}))


@router.delete('/{id}')
async def delete_category(id):
    if check_if_category_is_empty(id) and check_if_child_catogories_are_empty(id):
        client.konrad_borowik.categories.find_one_and_delete({"_id": ObjectId(id)})
        return f'Category deleted.'
    else:
        return f'This category is not empty.'
