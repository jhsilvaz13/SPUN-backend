from pydantic import BaseModel, validator, EmailStr
from typing import Literal, Optional
from core.apps.v1.question.schemas import QuestionRead
from core.utils import Components


class UserBase(BaseModel):
    id: int
    email: EmailStr
    slug: str
    first_name: str
    last_name: str
    is_active: bool
    is_student: bool
    is_editor: bool

    class Config:
        orm_mode = True

class UserRead(UserBase):
    pass

class UserUpdate(BaseModel):
    email: Optional[str]
    slug: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    is_active: Optional[bool]
    is_student: Optional[bool]
    is_editor: Optional[bool]

    class Config:
        orm_mode = True
