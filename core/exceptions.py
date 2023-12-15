
from fastapi.responses import JSONResponse
from fastapi import Request, status
from fastapi.exceptions import HTTPException
class ObjectDoesNotExist(HTTPException):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status.HTTP_404_NOT_FOUND
        self.message = "Object does not exist"
    def __str__(self):
        return self.message
        
async def ObjectDoesNotExistHandler(request: Request, exc: ObjectDoesNotExist):
    return JSONResponse(status_code=exc.status_code, 
    content={"message": exc.message})

class UserAlreadyExists(HTTPException):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status.HTTP_409_CONFLICT
        self.message = "User already exists"
    def __str__(self):
        return self.message
    
async def UserAlreadyExistsHandler(request: Request, exc: UserAlreadyExists):
    return JSONResponse(status_code=exc.status_code, 
    content={"message": exc.message})

class IncorrectPassword(HTTPException):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.message = "Incorrect Pasword"
    def __str__(self):
        return self.message
    
async def IncorrectPasswordHandler(request: Request, exc: IncorrectPassword):
    return JSONResponse(status_code=exc.status_code, 
    content={"message": exc.message})

class CredentialsNotValid(HTTPException):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.message = "Credentials not valid"
        self.headers={"WWW-Authenticate": "Bearer"}

    def __str__(self):
        return self.message
    
async def CredentialsNotValidHandler(request: Request, exc: CredentialsNotValid):
    return JSONResponse(status_code=exc.status_code, 
    content={"message": exc.message})

class TokenExpired(HTTPException):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.message = "Token expired"
        self.headers={"WWW-Authenticate": "Bearer"}

    def __str__(self):
        return self.message

async def TokenExpiredHandler(request: Request, exc: TokenExpired):
    return JSONResponse(status_code=exc.status_code, 
    content={"message": exc.message})

class DontHavePermissions(HTTPException):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.message = "You don't have permissions"
    def __str__(self):
        return self.message
    
async def DontHavePermissionsHandler(request: Request, exc: DontHavePermissions):
    return JSONResponse(status_code=exc.status_code, 
    content={"message": exc.message})

