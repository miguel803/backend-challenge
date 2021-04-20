from datetime import datetime

from api_valor_do_metro_quadrado.domain.entities.metro_quadrado import MetroQuadrado


def test_entity_metro_quadrado():
    metro_quadrado_dict = {"id": 1, "valor": 100.0, "data_de_cadastro": datetime.now()}
    entity_fields = MetroQuadrado(**metro_quadrado_dict).dict().keys()
    
    assert list(entity_fields) == ["id", "valor", "data_de_cadastro"]
