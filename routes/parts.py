from fastapi import APIRouter
from bson import ObjectId

from models.part import Part
from config.setup import client
from schemas.parts import partEntity, partsEntity


router = APIRouter()


@router.get('/parts')
async def find_all_parts():
    return partsEntity(client.konrad_borowik.parts.find())


@router.post('/parts')
async def create_part(part: Part):
    client.konrad_borowik.parts.insert_one(dict(part))
    return partsEntity(client.konrad_borowik.parts.find())


@router.put('/parts/{id}')
async def update_one_element_of_part(id, part: Part):
    client.konrad_borowik.parts.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {
            "$set": {dict(part)} 
        }
    )
    return partEntity(client.konrad_borowik.parts.find_one({"_id": ObjectId(id)}))


@router.delete('/parts/{id}')
async def delete_part(id):
    client.konrad_borowik.parts.find_one_and_delete({"_id": ObjectId(id)})
    return f'Part deleted.'
