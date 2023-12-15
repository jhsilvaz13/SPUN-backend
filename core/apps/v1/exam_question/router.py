from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from core import dependencies
from core.apps.v1.exam_question import schemas
from core.apps.v1.exam_question import controller

router=APIRouter()

@router.post("/create_random_exam/", response_model=schemas.ExamQuestionBlocksRead)
def create_random_exam(exam:schemas.ExamCreate, db: Session = Depends(dependencies.get_db)):
        return controller.create_random_exam(exam=exam,db=db)

@router.post("/create_random_simulacrum/", response_model=schemas.ExamQuestionBlocksRead)
def create_random_simulacrum( db: Session = Depends(dependencies.get_db)):
        exam=schemas.ExamCreate(component="simulacrum",is_simulacrum=True)
        return controller.create_random_simulacrum(exam=exam,db=db)