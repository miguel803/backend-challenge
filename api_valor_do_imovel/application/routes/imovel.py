from fastapi import APIRouter


router = APIRouter()


@router.get("/imovel/")
async def get_imovel():
    return None
