import os

import requests


def get_valor_do_metro_quadrado():
    api_url = os.getenv("API_METRO_QUADRADO_URL")
    response = requests.get(api_url)

    return response.json()["valor"]
