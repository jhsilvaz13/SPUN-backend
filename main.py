import uvicorn

from fastapi import FastAPI
from core.models import Base
from core.database import engine
from core.api import router as api
from core.config.config import HOST, PORT
from core import exceptions

from fastapi import HTTPException

description = """
SPUN API backend: API REST that is consumed by SPUN, data is stored in a database in POSTGRESQL.
"""
app = FastAPI(
    title="SPUN API",
    version="1.0.0",
    description=description,
)

#Create tables
Base.metadata.create_all(bind=engine)

#Aplication
app.include_router(api, prefix="/api")

#Handling errors
app.add_exception_handler(exceptions.ObjectDoesNotExist, exceptions.ObjectDoesNotExistHandler)
app.add_exception_handler(exceptions.UserAlreadyExists, exceptions.UserAlreadyExistsHandler)
app.add_exception_handler(exceptions.CredentialsNotValid, exceptions.CredentialsNotValidHandler)
app.add_exception_handler(exceptions.TokenExpired, exceptions.TokenExpiredHandler)
app.add_exception_handler(exceptions.DontHavePermissions, exceptions.DontHavePermissionsHandler)



#default route
@app.get("/")
async def home():
    return {"message": "Server is running"}

#models.PANEL.mount_to(app)

