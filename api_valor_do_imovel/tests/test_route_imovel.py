from fastapi.testclient import TestClient

from api_valor_do_imovel.main import app


def test_route_get_imovel():
    client = TestClient(app)
    response = client.get('/imovel/')

    assert response.status_code == 200
