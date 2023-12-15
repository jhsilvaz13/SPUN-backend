from sqlalchemy.orm import Session

from core.apps.v1.exam_question import schemas
from core.apps.v1.exam_question import services


def create_random_exam(exam:schemas.ExamCreate, db: Session) -> schemas.ExamQuestionBlocksRead:
    """"""
    data=services.create_random(exam=exam,db=db)
    return data

def create_random_simulacrum(exam:schemas.ExamCreate, db: Session) -> schemas.ExamQuestionBlocksRead:
    """"""
    data=services.create_random_simulacrum(exam=exam,db=db)
    return data
