from pydantic import BaseModel, validator
from typing import Literal, Optional

from core.utils import Components
class ExamCreate(BaseModel):
    component: Components
    is_simulacrum: bool=False

class Exam(BaseModel):
    id: int
    is_simulacrum: bool
    component: Components

    class Config:
        orm_mode = True

class ExamRead(Exam):
    pass

class ExamUpdate(BaseModel):
    is_simulacrum: Optional[bool]
    component: Optional[str]
    class Config:
            orm_mode = True

