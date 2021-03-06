from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from api_valor_do_imovel.domain.entities.imovel import Imovel
from api_valor_do_imovel.infrastructure.external_apis.api_metro_quadrado import get_valor_do_metro_quadrado


router = APIRouter()


@router.get("/imovel/", response_model=Imovel)
async def get_imovel(metragem: int = None):
    if metragem:
        try:
            imovel = Imovel(metragem=metragem)
            valor_do_metro_quadrado = get_valor_do_metro_quadrado()
            imovel.valor = imovel.metragem * valor_do_metro_quadrado
            return imovel
        except ValidationError as validation_exc:
            raise HTTPException(
                status_code=400, 
                detail={'error': 'A metragem precisa estar entre 10 e 10.000 metros quadrados'}
            )
    return None
