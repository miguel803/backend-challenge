import os


def get_database_url():
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    host = os.environ["DB_HOST"]
    db_name = os.environ["DB_NAME"]

    return f"postgresql://{user}:{password}@{host}/{db_name}"