from fastapi import APIRouter
from bson import ObjectId

from app.models.part import Part
from app.routes.utils.parts_utils import (
    parse_key,
    parse_value,
    check_if_correct_category
)
from app.config.setup import client
from app.schemas.parts import partEntity, partEntities


router = APIRouter(
    prefix="/parts",
    tags=["parts"],
)


@router.get('/')
async def find_all_parts():
    return partEntities(client.konrad_borowik.parts.find())


@router.get('/search/{key: value}')
async def find_part(key: str, value: str):
    query = {parse_key(key): parse_value(value)}
    return partEntities(client.konrad_borowik.parts.find(query))


@router.get('/search/{value}')
async def find_part_by_value(value: str):
    value = parse_value(value)
    return partEntities(client.konrad_borowik.parts.aggregate([
        {
            '$match': {
                '$or': [
                    {'serial_number': value},
                    {'name': value},
                    {'description': value},
                    {'category': value},
                    {'quantity': value},
                    {'price': value},
                    {'location.warehouse': value},
                    {'location.room': value},
                    {'location.bookcase': value},
                    {'location.shelf': value},
                    {'location.cuvette': value},
                    {'location.column': value},
                    {'location.row': value}
                ],
            },
        }
    ]))


@router.post('/')
async def create_part(part: Part):
    try:
        check_if_correct_category(part)
        client.konrad_borowik.parts.insert_one(dict(part))
        return partEntities(client.konrad_borowik.parts.find())
    except Exception as e:
        return f'Caught this error: {e}'


@router.put('/{id}')
async def update_whole_part(id, part: Part):
    try:
        check_if_correct_category(part)
        client.konrad_borowik.parts.find_one_and_update(
            {
                "_id": ObjectId(id)
            },
            {
                "$set": {dict(part)}
            }
        )
        return partEntity(client.konrad_borowik.parts.find_one({"_id": ObjectId(id)}))
    except Exception as e:
        return f'Caught this error: {e}'


@router.delete('/{id}')
async def delete_part(id):
    client.konrad_borowik.parts.find_one_and_delete({"_id": ObjectId(id)})
    return f'Part deleted.'
