from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from core.apps.v1.question_block import services
from core.apps.v1.question_block import schemas

from core.apps.v1.user.dependencies import get_current_user
from core.apps.v1.auth.schemas import DataToken

def create_question_block(question_block: schemas.QuestionBlockCreate, db: Session, current_user:DataToken= Depends(get_current_user)):
    """Create a question block in the database with the data that is passed as a parameter, the id of the question is not necessary because it is automatically generated, also creates all questions and choces that are associated with the question block, returns the created question block or 
    a meesage if something wrong happened"""
    if not current_user.is_editor:
        raise HTTPException(status_code=401, detail="You don't have enough permissions")
    data=services.create(question_block=question_block, db=db)
    return data
    
def get_all_question_block(db: Session):
    """Return the list of all question blocks registered in the database"""
    data=services.get_all(db=db)
    return data
    
def get_question_block(id:int, db: Session):
    """Return a question block that has as id the one that is passed as a parameter"""
    data=services.get(id=id, db=db)
    return data

def get_all_question_block_by_component(component:str, db: Session):
    """Return the list of all question blocks registered in the database that have the component that is passed as a parameter"""
    data=services.get_all_by_component(component=component, db=db)
    return data
    
def get_all_question_block_by_component_random(component:str, db: Session):
    """Return a list of 20 question blocks that have as component the one that is passed as a parameter, the list is selected randomly"""
    data=services.get_all_by_component_random(component=component, db=db)
    return data

def update_question_block(id:int, question_block: schemas.QuestionBlockUpdate, db: Session):
    data=services.update(id=id, question_block=question_block, db=db)
    return data
    
def delete_question_block(id:int, db: Session):
    data=services.delete(id=id, db=db)
    return data