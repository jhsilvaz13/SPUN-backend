from sqlalchemy.orm import Session

from core.models import ExamQuestion, Exam

from core.apps.v1.exam_question import schemas
from core.apps.v1.question_block import services as question_block_services
from core.apps.v1.exam import services as exam_services
from core.utils import Components


def create_random(exam: schemas.ExamCreate, db: Session)->schemas.ExamQuestionBlocksRead:
    question_blocks=question_block_services.get_all_by_component_random(component=exam.component,db=db,n=25)
    exam_db=exam_services.create(exam=exam,db=db)
    for question_block in question_blocks:
        exam_question_db=ExamQuestion(exam_id=exam_db.id, question_block_id=question_block.id)
        db.add(exam_question_db)
        db.commit()
        db.refresh(exam_question_db)

    for question_block in question_blocks:
        print(question_block.id)
    return schemas.ExamQuestionBlocksRead(id=exam_db.id,component=exam_db.component,is_simulacrum=exam_db.is_simulacrum,questions_blocks=question_blocks)

def create_random_simulacrum(exam: schemas.ExamCreate, db: Session)->schemas.ExamQuestionBlocksRead:
    final_question_blocks=[]
    for i,component in Components:
        if component==exam.component:
            break
        question_blocks=question_block_services.get_all_by_component_random(component=component,db=db,n=25)
        final_question_blocks+=question_blocks
    exam_db=exam_services.create(exam=exam,db=db)
    for question_block in final_question_blocks:
        exam_question_db=ExamQuestion(exam_id=exam_db.id, question_block_id=question_block.id)
        db.add(exam_question_db)
        db.commit()
        db.refresh(exam_question_db)

def get(exam_id: int, db: Session):
    """"""
    id_question_blocks=db.query(ExamQuestion).filter(ExamQuestion.exam_id == exam_id).all()
    question_blocks=[
        question_block_services.get(id=id_question_block.question_block_id,db=db)
        for id_question_block in id_question_blocks
    ]
    return question_blocks

