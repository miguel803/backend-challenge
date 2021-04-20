import pytest

from pydantic import ValidationError
from api_valor_do_imovel.domain.entities.imovel import Imovel


@pytest.mark.parametrize("test_input", [9, 10001])
def test_entity_imovel_validacao_metragem(test_input):
    with pytest.raises(ValidationError) as exc:
        Imovel(metragem=test_input)

        assert str(exc.value) == 'A quantidade de metros quadrados deve estar entre 10 e 10.000'
