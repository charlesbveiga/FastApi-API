from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def authenticate():
    """
    Rota Padrão para autenticação de usuários.
    """
    return {"mensagem": "Você acessou a rota auth"}

# Criamos um roteador e especificamos o caminho dominio/auth para as rotas de autenticação.
