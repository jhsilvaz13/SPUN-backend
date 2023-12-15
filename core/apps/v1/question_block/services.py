from sqlalchemy.orm import Session
import random 
from core.exceptions import ObjectDoesNotExist

from core.models import QuestionBlock
from core.apps.v1.question_block import schemas
from core.utils import Alghoritms


def create(question_block:schemas.QuestionBlockCreate, db: Session) -> schemas.QuestionBlockRead    :
    question_bl_db=QuestionBlock(content=question_block.content,component=question_block.component,image=question_block.image)
    db.add(question_bl_db)
    db.commit()
    db.refresh(question_bl_db)
    return question_bl_db

def get_all(db: Session) -> list[schemas.QuestionBlockRead]:
    return db.query(QuestionBlock).all()

def get(id:int, db: Session) -> schemas.QuestionBlockRead:
    question_bl_db=db.query(QuestionBlock).filter(QuestionBlock.id==id).first()
    if question_bl_db is None:
        raise ObjectDoesNotExist()
    return question_bl_db

def get_all_by_component(component:str, db: Session) -> list[schemas.QuestionBlockRead]:
    return db.query(QuestionBlock).filter(QuestionBlock.component==component).all()

def get_all_by_component_random(component:str, db: Session, n:int) -> list[schemas.QuestionBlockRead]:
    question_blocks=random.sample(get_all_by_component(component=component,db=db),n) #select 20 random question blocks
    weights=[len(qb.questions) for qb in question_blocks]#get the number of questions of each question block
    return Alghoritms.knapsack(list=question_blocks, weights=weights, goal=n)

def update(id:int, question_block:schemas.QuestionBlockUpdate, db: Session) -> schemas.QuestionBlockRead | None:
    question_bl_db=get(id=id,db=db)
    if question_bl_db is None:
        raise ObjectDoesNotExist()
    question_block_data=question_block.dict(exclude_unset=True)
    for key,value in question_block_data.items():
        setattr(question_bl_db,key,value)
    db.add(question_bl_db)
    db.commit()
    db.refresh(question_bl_db)
    return question_bl_db

def delete(id:int, db: Session) -> schemas.QuestionBlockRead | None:
    question_bl_db=get(id=id,db=db)
    if question_bl_db is None:
        raise ObjectDoesNotExist()
    db.delete(question_bl_db)
    db.commit()
    return question_bl_db

