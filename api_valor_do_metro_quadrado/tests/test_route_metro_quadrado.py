from unittest import mock
from datetime import datetime

from api_valor_do_metro_quadrado.tests.helpers import get_client, mock_database_env_vars


def test_get_metro_quadrado_success_content(mock_database_env_vars):
    client = get_client()
    with mock.patch("api_valor_do_metro_quadrado.infrastructure.repositories.metro_quadrado.MetroQuadradoRepository.get") as mock_repo_get:
        mock_repo_get.return_value = {'id': '1', 'valor': 100.0, 'data_de_cadastro': datetime.now()}
        response = client.get('/metro_quadrado/')

        assert response.status_code == 200
        assert response.json() == {'valor': 100.0}
        mock_repo_get.assert_called_once()