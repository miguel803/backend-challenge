import os
from unittest import mock

import databases

from api_valor_do_metro_quadrado.tests.helpers import mock_database_env_vars
from api_valor_do_metro_quadrado.infrastructure.database import get_database_url, create_database_connection


def test_get_database_url(mock_database_env_vars):
    database_url = get_database_url()

    assert database_url == f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"


def test_create_database_connection(mock_database_env_vars):
    database = create_database_connection()

    assert type(database) == databases.Database
