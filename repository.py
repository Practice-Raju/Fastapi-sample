"""
This module is to play crud base alchemy to play here
"""
from database import get_db
from models import Items as ItemModel
from schemas import Item,ItemBase
from sqlalchemy.orm import Session

def create_item_repo(item: ItemBase, db: Session) -> ItemModel:
    item_ob = ItemModel(name = item.name)
    db.add(item_ob)
    db.commit()
    db.refresh(item_ob)
    return item_ob

