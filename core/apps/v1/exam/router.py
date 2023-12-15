from fastapi import APIRouter,Depends
from fastapi import Path
from sqlalchemy.orm import Session

from core import dependencies
from core.apps.v1.exam import schemas
from core.apps.v1.exam import controller

#Router para exam
router=APIRouter()

@router.get("/get_all_exams/", response_model=list[schemas.ExamRead])
def get_all_exams(db: Session = Depends(dependencies.get_db)):
        return controller.get_all_exam(db=db)

@router.get("/get_exam/{id}", response_model=schemas.ExamRead)
def get_exam(id:int=Path(ge=1), db: Session = Depends(dependencies.get_db)):
        return controller.get_exam(id=id,db=db)

@router.put("/update_exam/{id}", response_model=schemas.ExamRead)
def update_exam(exam:schemas.ExamUpdate, id:int=Path(ge=1), db: Session = Depends(dependencies.get_db)):
        return controller.update_exam(id=id,exam=exam,db=db)

@router.delete("/delete_exam/{id}", response_model=schemas.ExamRead)
def delete_exam(id:int=Path(ge=1), db: Session = Depends(dependencies.get_db)):
        return controller.delete_exam(id=id,db=db)

        