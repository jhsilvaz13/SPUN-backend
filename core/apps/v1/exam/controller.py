from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from core.apps.v1.exam import services
from core.apps.v1.exam import schemas

def get_all_exam(db:Session) -> list[schemas.ExamRead]:
    """"""
    data=services.get_all(db=db)
    return data

def get_exam(id:int, db: Session):
    """"""
    data=services.get(id=id,db=db)
    return data

def update_exam(id:int, exam:schemas.ExamUpdate, db: Session ):
    """"""
    data=services.update(id=id,exam=exam,db=db)
    return data

def delete_exam(id:int, db: Session):
    """"""
    data=services.delete(id=id,db=db)
    return data
