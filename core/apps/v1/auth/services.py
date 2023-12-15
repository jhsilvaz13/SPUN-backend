from sqlalchemy.orm import Session

from core.exceptions import ObjectDoesNotExist, UserAlreadyExists, IncorrectPassword
from core.models import User
from core.utils import Hash
from core.apps.v1.auth import schemas
from core.apps.v1.auth import jwt

def login(user:schemas.UserLogin, db: Session):
    user_db=db.query(User).filter(User.email==user.email).first()
    if user_db is None:
        raise ObjectDoesNotExist()
    if not Hash.check_password(user.password, user_db.hashed_password):
        raise IncorrectPassword()
    userDataToken=schemas.DataToken(email=user_db.email,slug=user_db.slug,first_name=user_db.first_name,last_name=user_db.last_name, is_active=user_db.is_active, is_student=user_db.is_student, is_editor=user_db.is_editor)
    token= jwt.create_token(data=userDataToken.dict())
    return token

def signup(user:schemas.UserSignUp, db: Session):
    user_db=db.query(User).filter(User.email==user.email).first()
    if user_db is not None:
        raise UserAlreadyExists()
    hashed_password=Hash.hash_password(user.password)
    user.password=hashed_password
    user_db=User(email=user.email,slug=user.slug,first_name=user.first_name,last_name=user.last_name,hashed_password=user.password,is_active=user.is_active,is_student=user.is_student,is_editor=user.is_editor)
    token=jwt.create_token(data=schemas.DataToken(email=user_db.email,slug=user_db.slug,first_name=user_db.first_name,last_name=user_db.last_name, is_active=user_db.is_active, is_student=user_db.is_student, is_editor=user_db.is_editor).dict())
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return token