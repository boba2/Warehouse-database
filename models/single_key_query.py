from pydantic import BaseModel
from typing import Union

from models.part import Location


class singleKeyQuery(BaseModel):
    key: str
    value: int | float | str | Location
