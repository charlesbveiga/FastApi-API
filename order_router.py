from fastapi import APIRouter

order_router = APIRouter(prefix="/list", tags=["list"])


@order_router.get("/")
async def list():
    """
    Rota Padrão para listagem de automóveis.
    """
    return {"mensagem": "Você acessou a rota list"}

# Criamos um roteador e especificamos o caminho dominio/list para
# rotas de listagem.
