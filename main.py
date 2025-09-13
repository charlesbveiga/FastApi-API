from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from order_router import order_router  # noqa
from auth_routes import auth_router  # noqa

app.include_router(auth_router)
app.include_router(order_router)

# Arquivo responsável por criar o Fast API e definir configurações de
# criptografia, acessos e roteamento.
# Para rodar o código, executaro o comando: uvicorn main:app --reload
