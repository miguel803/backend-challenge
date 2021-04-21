from unittest import mock

from api_valor_do_imovel.infrastructure.external_apis.api_metro_quadrado import get_valor_do_metro_quadrado
from api_valor_do_imovel.tests.helpers import MockRequestsResponse


@mock.patch("api_valor_do_imovel.infrastructure.external_apis.api_metro_quadrado.requests.get")
def test_external_api_metro_quadrado(mock_requests_get):
    mock_requests_get.return_value = MockRequestsResponse(content={"valor": 50.0}, status_code=200)
    valor_do_metro_quadrado = get_valor_do_metro_quadrado()

    assert valor_do_metro_quadrado == 50.0
