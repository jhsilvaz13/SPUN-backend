from fastapi import APIRouter,Depends, Path, Request
from sqlalchemy.orm import Session
from typing import Annotated

from core import dependencies
from core.apps.v1.user import schemas
from core.apps.v1.user import controller
from core.apps.v1.auth.schemas import DataToken
from core.apps.v1.user.dependencies import get_current_user

#Router para question_block
router=APIRouter()

@router.get("/get_user", response_model=list[schemas.UserRead])
async def get_all_user(db: Session = Depends(dependencies.get_db)):
    return controller.get_all_user(db=db)

@router.get("/get_user/{id}", response_model=schemas.UserRead)
async def get_user(id:int=Path(ge=1), db: Session = Depends(dependencies.get_db)):
    return controller.get_user(id=id, db=db)

@router.patch("/update_user/{id}", response_model=schemas.UserRead)
async def delete_user(user:schemas.UserUpdate,id:int=Path(ge=1),db:Session=Depends(dependencies.get_db)):
    return controller.update_user(id=id,user=user, db=db)

@router.delete("/delete_user/{id}", response_model=schemas.UserRead)
async def delete_user(id:int=Path(ge=1), db:Session=Depends(dependencies.get_db)):
    return controller.delete_user(id=id, db=db)

@router.get("/get_user/{email}", response_model=schemas.UserRead)
async def get_user_by_email(email:str, db: Session = Depends(dependencies.get_db)):
    return controller.get_user_by_email(email=email, db=db)

@router.get("/get_user/me/info", response_model=schemas.UserRead)
async def get_user_me(current_user:schemas.UserRead= Depends(get_current_user), db: Session = Depends(dependencies.get_db)):
    return current_user