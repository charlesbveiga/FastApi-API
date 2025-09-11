from auth_routes import auth_router
from order_router import order_router
from fastapi import FastAPI

app = FastAPI()


app.include_router(auth_router)
app.include_router(order_router)

# Arquivo responsável por criar o Fast API e definir configurações de criptografia, acessos e roteamento.
# Para rodar o código, executaro o comando: uvicorn main:app --reload
