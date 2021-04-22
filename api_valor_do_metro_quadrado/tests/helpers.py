import os
from unittest import mock
import asyncio

from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def mock_database_env_vars():
    env_vars = {
        "DB_NAME": "test_db",
        "DB_USER": "user",
        "DB_PASSWORD": "pass",
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
    }
    with mock.patch.dict(os.environ, env_vars):
        yield


def get_client():
    from api_valor_do_metro_quadrado.main import app
    return TestClient(app)


def mock_async_function_result(result):
    import sys
    if sys.version_info[0] >= 3.8:
        return_value = asyncio.Future()
        return_value.set_result(result)
    else:
        return_value = result

    return return_value
