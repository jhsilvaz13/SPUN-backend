from jwt import encode, decode
from core.config import config
from datetime import datetime, timedelta
from core.apps.v1.auth.schemas import Token, DataToken
from core.exceptions import CredentialsNotValid, TokenExpired

def create_token(data:DataToken)->Token:
    token:str=encode(payload=data, key=config.SECRET_KEY, algorithm=config.ALGORITHM)
    return Token(access_token=token, token_type="bearer", expires_in=config.TOKEN_EXPIRE_MINUTES*60).dict()

def validate_token(token:str)->DataToken:
    data:DataToken=decode(jwt=token, key=config.SECRET_KEY, algorithms=[config.ALGORITHM])
    return data

def get_current_user(token: str)->DataToken:
    payload = validate_token(token)
    if payload is None:
        raise CredentialsNotValid
    return payload