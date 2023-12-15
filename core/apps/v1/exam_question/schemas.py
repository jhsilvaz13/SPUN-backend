from pydantic import BaseModel, validator
from typing import Literal, Optional

from core.apps.v1.question_block.schemas import QuestionBlockRead
from core.apps.v1.exam.schemas import ExamRead, ExamCreate


class ExamQuestionBlocksRead(ExamRead):
    questions_blocks: list[QuestionBlockRead]
    class Config:
        orm_mode = True