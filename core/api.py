from fastapi import APIRouter

from core.apps.v1.question_block.router import router as question_block
from core.apps.v1.question.router import router as question
from core.apps.v1.choice.router import router as choice
from core.apps.v1.exam.router import router as exam
from core.apps.v1.exam_question.router import router as exam_question
from core.apps.v1.user.router import router as user
from core.apps.v1.auth.router import router as auth 

router = APIRouter()


router.include_router(exam, prefix="/v1/exam", tags=["exam"])
router.include_router(exam_question, prefix="/v1/exam_question", tags=["exam_question"])
router.include_router(question_block, prefix="/v1/question_block", tags=["question_block"])
router.include_router(question, prefix="/v1/question", tags=["question"])
router.include_router(choice, prefix="/v1/choice", tags=["choice"])
router.include_router(user, prefix="/v1/user", tags=["user"])
router.include_router(auth, prefix="/v1/auth", tags=["auth"])