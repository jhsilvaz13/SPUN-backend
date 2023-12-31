from dotenv import load_dotenv
import os

load_dotenv()
POSTGRESS_HOST=os.getenv('POSTGRESS_HOST')
POSTGRESS_DB=os.getenv('POSTGRESS_DB')
POSTGRESS_USER=os.getenv('POSTGRESS_USER')
POSTGRESS_PASSWORD=os.getenv('POSTGRESS_PASSWORD')
POSTGRESS_URL=f"postgresql://{POSTGRESS_USER}:{POSTGRESS_PASSWORD}@{POSTGRESS_HOST}/{POSTGRESS_DB}"

HOST=os.getenv('HOST')
PORT=int(os.getenv('PORT'))

SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM=os.getenv('ALGORITHM')
TOKEN_EXPIRE_MINUTES=int(os.getenv('TOKEN_EXPIRE_MINUTES'))