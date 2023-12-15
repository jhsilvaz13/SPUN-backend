from sqlalchemy.orm import Session
from core.exceptions import ObjectDoesNotExist

from core.models import User
from core.apps.v1.user import schemas

def get_all(db: Session) -> list[schemas.UserRead]:
    return db.query(User).all()

def get(id:int, db: Session) -> schemas.UserRead:
    user_db=db.query(User).filter(User.id==id).first()
    if user_db is None:
        raise ObjectDoesNotExist()
    return user_db

def get_by_email(email:str, db: Session) -> schemas.UserRead:
    user_db=db.query(User).filter(User.email==email).first()
    if user_db is None:
        raise ObjectDoesNotExist()
    return user_db

def update(id:int, user:schemas.UserUpdate, db: Session) -> schemas.UserRead:
    user_db=get(id=id,db=db)
    if user_db is None:
        raise ObjectDoesNotExist()
    user_data=user.dict(exclude_unset=True)
    for key,value in user_data.items():
        setattr(user_db,key,value)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def delete(id:int, db: Session) -> schemas.UserRead:
    user_db=get(id=id,db=db)
    if user_db is None:
        raise ObjectDoesNotExist()
    db.delete(user_db)
    db.commit()
    return user_db