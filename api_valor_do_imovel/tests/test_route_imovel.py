from unittest import mock

from fastapi.testclient import TestClient

from api_valor_do_imovel.main import app
from api_valor_do_imovel.tests.helpers import mock_database_env_vars, MockRequestsResponse


def test_route_get_imovel():
    client = TestClient(app)
    response = client.get('/imovel/')

    assert response.status_code == 200


def test_route_get_imovel_metragem_invalida():
    client = TestClient(app)
    response = client.get('/imovel/?metragem=8')

    assert response.status_code == 400


def test_route_get_imovel_metragem_valida(mock_database_env_vars):
    client = TestClient(app)
    with mock.patch("api_valor_do_imovel.infrastructure.external_apis.api_metro_quadrado.requests.get") as mock_get:
        mock_get.return_value = MockRequestsResponse(content={"valor": 10.0}, status_code=200)
        response = client.get('/imovel/?metragem=100')

        assert response.status_code == 200
        assert response.json() == {'metragem': 100, 'valor': 1000}
