from pydantic import BaseModel


class Category(BaseModel):
    name: str
    parent_name: str