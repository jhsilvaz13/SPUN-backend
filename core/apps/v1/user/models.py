from sqlalchemy import DateTime, Boolean, Column, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship
from starlette_admin.contrib.sqla import admin, ModelView

from core.database import Base, engine   

class User(Base):
    """"""
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index = True)
    email = Column(String, unique=True, index=True)
    slug = Column(String, unique=True, index=True)
    first_name = Column(String, unique=False, index=True)
    last_name = Column(String, unique=False, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_student = Column(Boolean, default=True)
    is_editor = Column(Boolean, default=False)

class Exam(Base):
    """Represents an exam and its information"""
    __tablename__ = "exam"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    is_simulacrum = Column(Boolean, nullable=False)
    component = Column(String, nullable=False, default="Simulacro")

class ExamTake(Base):
    """Represents the presentation of an exam"""
    __tablename__ = "exam_take"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    exam_id = Column(Integer, ForeignKey('exam.id'))
    created_at = Column(DateTime, default=func.current_timestamp())
    finished_at = Column(DateTime)
    score = Column(Integer, nullable=False)
    title = Column(String, index=True)
    description = Column(String, index=True)
    answers = Column(Text, nullable=False)

class ExamQuestion(Base):
    """Represents the questions related to an exam"""
    __tablename__ = "exam_question"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey("exam.id"))
    question_block_id = Column(Integer, ForeignKey("question_block.id"))


class QuestionBlock(Base):
    """Represent a block where the context for one or more questions is stored"""
    __tablename__ = "question_block"
    id = Column(Integer, primary_key=True, index = True, autoincrement=True)
    content = Column(Text, nullable=True,)
    component = Column(String, nullable=False)
    image = Column(String, nullable=True)

    questions=relationship("Question", back_populates="question_block",cascade="all, delete")

class Question(Base):
    """Represent a question, the question is always related to a question block with id question_block_id"""
    __tablename__ = "question"
    id = Column(Integer, primary_key=True, index = True, autoincrement=True)
    question_block_id = Column(Integer, ForeignKey("question_block.id",ondelete='CASCADE'),nullable=False)
    text = Column(Text, nullable=False)

    question_block=relationship("QuestionBlock", back_populates="questions")
    choices=relationship("Choice", back_populates="question",cascade="all, delete")

class Choice(Base):
    """Represent a choice for a question, the choice is always related to a question with id quest_id"""
    __tablename__ = "choice"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey("question.id",ondelete='CASCADE'))
    text = Column(String, nullable=False)   
    is_correct = Column(Boolean, nullable=False,default=False)

    question=relationship("Question", back_populates="choices")

# Create admin interface with starlette
PANEL= admin.Admin(engine) 

PANEL.add_view(ModelView(User))
PANEL.add_view(ModelView(Exam))
PANEL.add_view(ModelView(ExamTake))
PANEL.add_view(ModelView(ExamQuestion))
PANEL.add_view(ModelView(QuestionBlock))
PANEL.add_view(ModelView(Question))
PANEL.add_view(ModelView(Choice))