from fastapi import APIRouter

from api_valor_do_metro_quadrado.domain.entities.metro_quadrado import MetroQuadrado
from api_valor_do_metro_quadrado.infrastructure.repositories.metro_quadrado import MetroQuadradoRepository


router = APIRouter()


@router.get("/metro_quadrado/", tags=["metro_quadrado"], response_model=MetroQuadrado, response_model_exclude=["id", "data_de_cadastro"])
async def get_metro_quadrado():
    obj = await MetroQuadradoRepository.get()
    return dict(obj)
