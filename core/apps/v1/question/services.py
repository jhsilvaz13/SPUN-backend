from sqlalchemy.orm import Session

from core.exceptions import ObjectDoesNotExist
from core. models import Question
from core.apps.v1.question import schemas
from core.apps.v1.choice import services as choice_services
from core.apps.v1.choice import schemas as choice_schemas


def create(question:schemas.QuestionCreate, db: Session) -> schemas.QuestionRead:
    question_db=Question(question_block_id=question.question_block_id,text=question.text)
    db.add(question_db)
    db.commit()
    db.refresh(question_db)
    for choice in question.choices:
        choice_services.create(
            choice=choice_schemas.ChoiceCreate(
                question_id=question_db.id,
                text=choice.text,
                is_correct=choice.is_correct
            ),
            db=db
        )
    return question_db

def get_all(db: Session) -> list[schemas.QuestionRead]:
    return db.query(Question).all()

def get(id:int, db: Session) -> schemas.QuestionRead:
    question_db=db.query(Question).filter(Question.id==id).first()
    if question_db is None:
        raise ObjectDoesNotExist()
    return question_db

def update(id:int, question:schemas.QuestionUpdate, db: Session) -> schemas.QuestionRead:
    question_db=get(id=id,db=db)
    if question_db is None:
        raise ObjectDoesNotExist()
    question_data=question.dict(exclude_unset=True)
    for key,value in question_data.items():
        setattr(question_db,key,value)
    db.add(question_db)
    db.commit()
    db.refresh(question_db)
    return question_db

def delete(id:int, db: Session) -> schemas.QuestionRead:
    question_db=get(id=id,db=db)
    if question_db is None:
        raise ObjectDoesNotExist()
    db.delete(question_db)
    db.commit()
    return question_db
