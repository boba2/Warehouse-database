from pydantic import BaseModel
from typing import Union


class Location(BaseModel):
    warehouse: str
    room: int
    bookcase: int
    shelf: int
    cuvette: int
    column: int
    row: int


class Part(BaseModel):
    serial_number:str
    name: str
    description: str
    category: str
    quantity: int
    price: float
    location: Location
