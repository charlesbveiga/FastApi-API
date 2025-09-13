from fastapi import APIRouter, Depends, HTTPException
from models import Users
from dependencies import create_session
from main import bcrypt_context
from schemas import UsersSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def home():
    """
    Rota Padrão para autenticação de usuários.
    """
    return {"mensagem": "Você acessou a rota auth"}


@auth_router.post("/create_account")
async def create_account(users_schema: UsersSchema,
                         session: Session = Depends(create_session)):
    user = session.query(Users).filter(
        Users.email == users_schema.email).first()
    if user:
        raise HTTPException(status_code=400,
                            detail="Email do usuário já cadastrado!")
    else:
        encrypted_password = bcrypt_context.hash(users_schema.password)
        new_user = Users(users_schema.name,
                         users_schema.email,
                         encrypted_password,
                         users_schema.active,
                         users_schema.admin)
        session.add(new_user)
        session.commit()
        return {"mensage":
                f"Usuário {users_schema.email} cadastrado com sucesso!"}

# Criamos um roteador e especificamos o caminho dominio/auth
# para as rotas de autenticação.
