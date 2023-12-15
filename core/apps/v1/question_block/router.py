from fastapi import APIRouter,Depends, Path
from sqlalchemy.orm import Session

from core import dependencies
from core.utils import Components
from core.apps.v1.question_block import schemas
from core.apps.v1.question_block import controller

#Router para question_block
router=APIRouter()

@router.post("/create_question_block",response_model=schemas.QuestionBlockRead) 
async def create_question_block(question_block: schemas.QuestionBlockCreate, db: Session = Depends(dependencies.get_db)):
    return  controller.create_question_block(question_block=question_block, db=db)

@router.get("/get_question_block",response_model=list[schemas.QuestionBlockRead])
async def get_all_question_block(db: Session = Depends(dependencies.get_db)):
    return controller.get_all_question_block(db=db)

@router.get("/get_question_block/{id}",response_model=schemas.QuestionBlockRead)
async def get_question_block(id:int=Path(ge=1), db: Session = Depends(dependencies.get_db)):
    return controller.get_question_block(id=id, db=db)

@router.get("/get_question_block/by_component/{component}",response_model=list[schemas.QuestionBlockRead])
async def get_all_question_block_by_component(component:Components=Path(), db: Session = Depends(dependencies.get_db)):
    return controller.get_all_question_block_by_component(component=component, db=db)

@router.get("/get_question_block/by_component/{component}/random",response_model=list[schemas.QuestionBlockRead])
async def get_all_question_block_by_component_random(component:Components=Path(), db: Session = Depends(dependencies.get_db)):
    return controller.get_all_question_block_by_component_random(component=component, db=db)

@router.patch("/update_question_block/{id}",response_model=schemas.QuestionBlockRead)
async def update_question_block( question_block: schemas.QuestionBlockUpdate, id:int=Path(ge=1), db: Session = Depends(dependencies.get_db)):
    return controller.update_question_block(id=id, question_block=question_block, db=db)

@router.delete("/delete_question_block/{id}",response_model=schemas.QuestionBlockRead)
async def delete_question_block(id:int=Path(ge=1), db: Session = Depends(dependencies.get_db)):
    return controller.delete_question_block(id=id, db=db)