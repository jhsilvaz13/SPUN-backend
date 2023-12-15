from pydantic import BaseModel, validator, EmailStr
from typing import Literal, Optional
from core.apps.v1.question.schemas import QuestionRead
from core.utils import Components

class UserSignUp(BaseModel):
    email: EmailStr
    slug: str
    first_name: str
    last_name: str
    password: str
    is_active: bool
    is_student: bool
    is_editor: bool

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: Literal["bearer"]
    expires_in: Optional[int]

class DataToken(BaseModel):
    email: EmailStr
    slug: str
    first_name: str
    last_name: str
    is_active: bool
    is_student: bool
    is_editor: bool