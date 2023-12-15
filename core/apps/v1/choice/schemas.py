from pydantic import BaseModel, validator
from typing import Literal, Optional

class Choice(BaseModel):
    id: int
    question_id: int
    text: str
    is_correct: bool
    class Config:
        orm_mode = True

class ChoiceRead(Choice):
    pass

class ChoiceCreate(BaseModel):
    question_id: int
    text: str
    is_correct: bool
    class Config:
        orm_mode = True

class ChoiceCreateI(BaseModel):
    text: str
    is_correct: bool
    class Config:
        orm_mode = True

class ChoiceUpdate(BaseModel):
    text: str
    is_correct: bool
    class Config:
        orm_mode = True 