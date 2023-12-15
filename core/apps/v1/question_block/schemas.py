from pydantic import BaseModel, validator
from typing import Literal, Optional
from core.apps.v1.question.schemas import QuestionRead
from core.utils import Components


class QuestionBlock(BaseModel):
    id: int
    content: Optional[str]
    component: Components
    image: Optional[str]
    questions : list[QuestionRead]
    class Config:
        orm_mode = True

class QuestionBlockRead(QuestionBlock):
    pass

class QuestionBlockCreate(BaseModel):
    content: Optional[str]
    component: Components
    image: Optional[str]
    class Config:
        orm_mode = True

class QuestionBlockUpdate(BaseModel):
    content: Optional[str]
    component: Components
    image: Optional[str]

        