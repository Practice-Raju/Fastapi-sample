from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    name : str


class Item(BaseModel):
    id : int
    name : str

    class Config:
        orm_mode = True

class ItemPatchSchema(BaseModel):
    name : Optional[str]