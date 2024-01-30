from fastapi import APIRouter
from bson import ObjectId

from models.part import Part
from models.single_key_query import singleKeyQuery
from config.setup import client
from schemas.parts import partEntity, partEntities


router = APIRouter(
    prefix="/parts",
    tags=["parts"],
)


@router.get('/')
async def find_all_parts():
    return partEntities(client.konrad_borowik.parts.find())


@router.get('/search')
async def find_part(query: singleKeyQuery):
    return partEntities(client.konrad_borowik.parts.find(dict(query)))


@router.post('/')
async def create_part(part: Part):
    client.konrad_borowik.parts.insert_one(dict(part))
    return partEntities(client.konrad_borowik.parts.find())


@router.put('/{id}')
async def update_part(id, part: Part):
    client.konrad_borowik.parts.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {
            "$set": {dict(part)} 
        }
    )
    return partEntity(client.konrad_borowik.parts.find_one({"_id": ObjectId(id)}))


@router.delete('/{id}')
async def delete_part(id):
    client.konrad_borowik.parts.find_one_and_delete({"_id": ObjectId(id)})
    return f'Part deleted.'
