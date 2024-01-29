from fastapi import APIRouter

from models.part import Part
from config.setup import client
from schemas.parts import partEntity, partsEntity


part = APIRouter()

@part.get('/')
async def find_all_parts():
    return partsEntity(client.konrad_borowik.parts.find())


@part.post('/')
async def create_part(part: Part):
    client.konrad_borowik.parts.insert_one(dict(part))
    return partsEntity(client.konrad_borowik.parts.find())


@part.put('/')
async def update_part(query: dict, new_value: str):
    for q in query.items():
        key, value = q

    client.konrad_borowik.parts.find_one_and_update(
        {
            key: value
        },
        {
            "$set": {key: new_value} 
        }
    )
    return partsEntity(client.konrad_borowik.parts.find())


@part.delete('/')
async def delete_part(query: dict):
    client.konrad_borowik.parts.find_one_and_delete(query)
    return partsEntity(client.konrad_borowik.parts.find())
