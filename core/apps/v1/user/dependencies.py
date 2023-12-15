from fastapi import Request, Depends
from core import dependencies
from sqlalchemy.orm import Session

from core.apps.v1.auth.jwt import validate_token
from core.exceptions import CredentialsNotValid, TokenExpired
from core.apps.v1.user.schemas import UserRead
from core.apps.v1.user import services as user_services

#Obtener el usuario actual
def get_current_user(request:Request) -> UserRead:
    token:str=request.headers.get("authorization").split(" ")[1]
    payload = validate_token(token)
    if payload is None:
        raise CredentialsNotValid
    return user_services.get_by_email(email=payload["email"], db=Depends(dependencies.get_db))