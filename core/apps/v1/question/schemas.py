import datetime
from pydantic import BaseModel, validator
from typing import Literal, Optional

from core.apps.v1.choice.schemas import ChoiceRead, ChoiceCreateI

class Question(BaseModel):
    id: int
    question_block_id: int
    text: str
    choices: list[ChoiceRead]
    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    question_block_id: int
    text: str
    choices: list[ChoiceCreateI]

    class Config:
        orm_mode = True    

class QuestionRead(Question):
    pass

class QuestionUpdate(BaseModel):
    text: str
    class Config:
        orm_mode = True

