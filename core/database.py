from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from core.config.config import POSTGRESS_DB, POSTGRESS_PASSWORD, POSTGRESS_HOST, POSTGRESS_USER

# Descomentar para usar SQLite
"""SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  
)
"""

# Descomentar para usar PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://"+POSTGRESS_USER+":"+POSTGRESS_PASSWORD+"@"+POSTGRESS_HOST+"/"+POSTGRESS_DB

engine = create_engine(
    SQLALCHEMY_DATABASE_URL  
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass