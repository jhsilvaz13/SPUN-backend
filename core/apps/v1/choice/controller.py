from sqlalchemy.orm import Session
from core.apps.v1.choice import services
from core.apps.v1.choice import schemas


def get_all_choice(db:Session):
    """"""
    data=services.get_all(db=db)
    return data

def get_choice(id:int, db:Session):
    """"""
    data=services.get(id=id, db=db)
    return data
    
def update_choice(id:int, choice: schemas.ChoiceUpdate,db: Session):
    """"""
    data=services.update(id=id, choice=choice, db=db)
    return data

def delete_choice(id:int, db:Session):
    """"""
    data=services.delete(id=id, db=db)
    return data