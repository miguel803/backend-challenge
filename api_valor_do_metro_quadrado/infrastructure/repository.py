import databases

from app.infrastructure.database import get_database_url


database_url = get_database_url()
database = databases.Database(database_url)
