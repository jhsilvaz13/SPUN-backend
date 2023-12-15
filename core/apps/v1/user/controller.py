from sqlalchemy.orm import Session
from core.apps.v1.user import services
from core.apps.v1.user import schemas

def get_all_user(db: Session):
    data=services.get_all(db=db)
    return data

def get_user(id:int, db: Session):
    data=services.get(id=id, db=db)
    return data

def get_user_by_email(email:str, db: Session):
    data=services.get_by_email(email=email, db=db)
    return data

def update_user(id:int, user:schemas.UserUpdate, db: Session):
    data=services.update(id=id,user=user, db=db)
    return data

def delete_user(id:int, db: Session):
    data=services.delete(id=id, db=db)
    return data
