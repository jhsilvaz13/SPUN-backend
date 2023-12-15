from fastapi import APIRouter,Depends, Path
from sqlalchemy.orm import Session

from core import dependencies
from core.apps.v1.question import schemas
from core.apps.v1.question import controller

#Router para question_block
router=APIRouter()

@router.post("/create_question",response_model=schemas.QuestionRead)
async def create_question(question: schemas.QuestionCreate, db: Session = Depends(dependencies.get_db)):
    return  controller.create_question(question=question, db=db)

@router.get("/get_question",response_model=list[schemas.QuestionRead])
async def get_all_question(db: Session = Depends(dependencies.get_db)):
    return controller.get_all_question(db=db)

@router.get("/get_question/{id}",response_model=schemas.QuestionRead)
async def get_question(id:int=Path(ge=1), db: Session = Depends(dependencies.get_db)):
    return controller.get_question(id=id, db=db)

@router.patch("/update_question/{id}",response_model=schemas.QuestionRead)
async def update_question(question: schemas.QuestionUpdate, id:int=Path(ge=1), db: Session = Depends(dependencies.get_db)):
    return controller.update_question(id=id, question=question, db=db)

@router.delete("/delete_question/{id}",response_model=schemas.QuestionRead)
async def delete_question(id:int=Path(ge=1), db: Session = Depends(dependencies.get_db)):
    return controller.delete_question(id=id, db=db)
