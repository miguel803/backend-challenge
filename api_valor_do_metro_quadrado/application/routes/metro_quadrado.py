from fastapi import APIRouter

router = APIRouter()


@router.get("/metro_quadrado/", tags=["metro_quadrado"])
async def get_metro_quadrado():
    return None
