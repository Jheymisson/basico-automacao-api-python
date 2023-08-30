import requests

from unicred.common.utils.bodies import gerar_boleto_body
from unicred.config import gerar_token, AMBIENTE_URL


class Boletos:

    def __init__(self):
        self.token = gerar_token()

    def gerar_boleto_normal(self):
        url = f'{AMBIENTE_URL}/titulo-usf/cobranca/v3/beneficiarios/00FB8823A6F645D2B788D128356F82C6/titulos'
        print(url, 'URL completa')
        headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {self.token}',
                    'cooperativa': '515'
                }
        response = requests.post(url, headers=headers, json=gerar_boleto_body)
        uuid_titulo = response.text
        print(uuid_titulo)
        return uuid_titulo