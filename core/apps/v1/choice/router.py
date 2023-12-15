from fastapi import Path

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from core import dependencies
from core.apps.v1.choice import schemas
from core.apps.v1.choice import controller

#Router para user
router=APIRouter()

@router.get("/get_choice", response_model=list[schemas.ChoiceRead])
async def get_all_choice(db: Session = Depends(dependencies.get_db)):
    return controller.get_all_choice(db=db)

@router.get("/get_choice/{id}", response_model=schemas.ChoiceRead)
async def get_choice(id:int=Path(ge=1), db: Session = Depends(dependencies.get_db)):
    return controller.get_choice(id=id, db=db)

@router.patch("/update_choice/{id}", response_model=schemas.ChoiceRead)
async def delete_choice(choice:schemas.ChoiceUpdate,id:int=Path(ge=1),db:Session=Depends(dependencies.get_db)):
    return controller.update_choice(id=id,choice=choice, db=db)

@router.delete("/delete_choice/{id}", response_model=schemas.ChoiceRead)
async def delete_choice(id:int=Path(ge=1), db:Session=Depends(dependencies.get_db)):
    return controller.delete_choice(id=id, db=db)