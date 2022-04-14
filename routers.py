from fastapi import APIRouter, Depends, Response
from database import get_db
from schemas import ItemBase, Item, ItemPatchSchema
from repository import create_item_repo
from sqlalchemy.orm import Session
from models import Items as ItemModel

item_router = APIRouter(
    prefix='/item',
    tags= ['Items']
)

@item_router.post('/', response_model = Item)
def create_item(item: ItemBase, response:Response, db:Session = Depends(get_db)):
    result = create_item_repo(item, db)
    if result :
        response.status_code = 201
    return result

@item_router.patch('/{item_id}')
def patch_item(item_id:int,item:ItemPatchSchema,db:Session = Depends(get_db)):
    db.query(ItemModel).get(item_id)
    return 'checking'


