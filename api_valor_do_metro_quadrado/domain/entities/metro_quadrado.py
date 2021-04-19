from datetime import datetime

from pydantic import BaseModel


class MetroQuadrado(BaseModel):
    id: int
    valor: float
    data_de_atualizacao: datetime
