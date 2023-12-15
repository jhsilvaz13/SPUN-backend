from sqlalchemy.orm import Session

from core.exceptions import ObjectDoesNotExist
from core. models import Exam, ExamQuestion
from core.apps.v1.exam import schemas

from core.apps.v1.question_block import services as question_block_services


def create(exam: schemas.ExamCreate, db: Session)->schemas.ExamRead:
    """"""
    exam_db = Exam(component=exam.component, is_simulacrum=exam.is_simulacrum)
    db.add(exam_db)
    db.commit()
    db.refresh(exam_db)
    return exam_db

def get_all(db: Session) -> list[schemas.ExamRead]:
    """"""
    return db.query(Exam).all()

def get(id: int, db: Session):
    """"""
    db_exam = db.query(Exam).filter(Exam.id == id).first()
    if db_exam is None:
        raise ObjectDoesNotExist()
    return db_exam

def update(id: int, exam: schemas.ExamUpdate, db: Session):
    """"""
    db_exam = get(id=id, db=db)
    if db_exam is None:
        raise ObjectDoesNotExist()
    exam_data = exam.dict(exclude_unset=True)
    for key, value in exam_data.items():
        setattr(db_exam, key, value)
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam

def delete(id: int, db: Session):
    """"""
    db_exam = get(id=id, db=db)
    if db_exam is None:
        raise ObjectDoesNotExist()
    db.delete(db_exam)
    db.commit()
    return db_exam