from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from core.apps.v1.auth import services
from core.apps.v1.auth import schemas

def login(user:schemas.UserLogin, db: Session):
    """"""
    data=services.login(user=user, db=db)
    return JSONResponse(status_code=200, content=data)

def signup(user:schemas.UserLogin, db: Session):
    """"""
    data=services.signup(user=user, db=db)
    return JSONResponse(status_code=200, content=data)