from pydantic import BaseModel, validator, ValidationError


MIN_METRAGEM = 10
MAX_METRAGEM = 10000


class Imovel(BaseModel):
    metragem: int
    valor: float = 0.0

    @validator('metragem')
    def validate_metragem(cls, v):
        metragem = v
        if metragem < MIN_METRAGEM or metragem > MAX_METRAGEM:
            raise ValidationError('A quantidade de metros quadrados deve estar entre 10 e 10.000')
        
        return metragem