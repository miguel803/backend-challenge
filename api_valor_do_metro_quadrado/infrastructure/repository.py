import databases

from api_valor_do_metro_quadrado.infrastructure.database import get_database_url


database_url = get_database_url()
database = databases.Database(database_url)
