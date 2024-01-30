from pydantic import BaseModel
from typing import Union


class singleKeyQuery(BaseModel):
    name: str
    value: Union[str, int, float, dict]
