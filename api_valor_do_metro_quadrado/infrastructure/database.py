import os


def get_database_url():
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    host = os.environ["DB_HOST"]
    port = os.environ["DB_PORT"]
    db_name = os.environ["DB_NAME"]

    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"