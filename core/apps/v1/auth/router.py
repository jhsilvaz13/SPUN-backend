from fastapi import Path


from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from core import dependencies
from core.apps.v1.auth import schemas
from core.apps.v1.auth import controller


#Router para autenticacion
router=APIRouter()


@router.post("/login")
async def login(user:schemas.UserLogin, db: Session = Depends(dependencies.get_db)):
    return controller.login(user=user, db=db)
    
@router.post("/signup")
async def signup(user:schemas.UserSignUp, db: Session = Depends(dependencies.get_db)):
    return controller.signup(user=user, db=db)