from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from core.apps.v1.question import services
from core.apps.v1.question import schemas

def create_question(question: schemas.QuestionCreate, db:Session):
    """Create a question in the database with the data that is passed as a parameter, the id of the question is not necessary because it is automatically generated, also creates all choces that are associated with the question, returns the created question or 
    a meesage if something wrong happened"""
    data=services.create(question=question, db=db)
    return data
    
def get_all_question(db:Session):
    """Return the list of all questions registered in the database"""
    data=services.get_all(db=db)
    return data
    
def get_question(id:int, db:Session):
    """Return a question that has as id the one that is passed as a parameter"""
    data=services.get(id=id, db=db)
    return data
    
def update_question(id:int, question: schemas.QuestionUpdate, db:Session):
    """"""
    data=services.update(id=id, question=question, db=db)
    return data
    
def delete_question(id:int, db:Session):
    """"""
    data=services.delete(id=id, db=db)
    return data
    
