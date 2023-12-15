from sqlalchemy.orm import Session

from core.exceptions import ObjectDoesNotExist

from core. models import Choice
from core.apps.v1.choice import schemas

def create(choice:schemas.ChoiceCreate, db: Session) -> schemas.ChoiceRead:
    choice_db=Choice(question_id=choice.question_id, text=choice.text, is_correct=choice.is_correct)
    db.add(choice_db)
    db.commit()
    db.refresh(choice_db)
    return choice_db

def get_all(db: Session) -> list[schemas.ChoiceRead]:
    return db.query(Choice).all()

def get(id:int, db: Session) -> schemas.ChoiceRead | None:
    choice_db=db.query(Choice).filter(Choice.id==id).first()
    if choice_db is None:
        raise ObjectDoesNotExist()
    return choice_db

def update(id:int, choice:schemas.ChoiceUpdate, db: Session) -> schemas.ChoiceRead | None:
    choice_db=get(id=id,db=db)
    if choice_db is None:
        raise ObjectDoesNotExist()
    choice_data=choice.dict(exclude_unset=True)
    for key,value in choice_data.items():
        setattr(choice_db,key,value)
    db.add(choice_db)
    db.commit()
    db.refresh(choice_db)
    return choice_db

def delete(id:int, db: Session) -> schemas.ChoiceRead | None:
    choice_db=get(id=id,db=db)
    if choice_db is None:
        raise ObjectDoesNotExist()
    db.delete(choice_db)
    db.commit()
    return choice_db
    