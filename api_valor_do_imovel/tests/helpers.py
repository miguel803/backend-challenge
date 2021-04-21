import os
from unittest import mock

import pytest


@pytest.fixture
def mock_database_env_vars():
    env_vars = {
        "API_METRO_QUADRADO_URL": "http://localhost:8080/metro_quadrado/",
    }
    with mock.patch.dict(os.environ, env_vars):
        yield


class MockRequestsResponse:

    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code
    
    def json(self):
        return self.content
