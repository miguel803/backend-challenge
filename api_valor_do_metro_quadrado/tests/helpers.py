import os
from unittest import mock

import pytest
from dotenv import dotenv_values


@pytest.fixture
def mock_env_vars():
    config = dotenv_values("./api_valor_do_metro_quadrado/.dev-env")
    with mock.patch.dict(os.environ, config):
        yield
