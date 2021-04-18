from api_valor_do_metro_quadrado.tests.helpers import get_client, mock_database_env_vars


def test_get_metro_quadrado_status_200(mock_database_env_vars):
    client = get_client()
    response = client.get('/metro_quadrado/')

    assert response.status_code == 200
