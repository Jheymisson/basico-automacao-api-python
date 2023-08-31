import requests

from unicred.config import gerar_token, AMBIENTE_URL


class Boletos:

    def __init__(self):
        self.token = gerar_token()

    def gerar_boleto_normal(self, uuidBeneficiario, carteira, boleto_body):
        url = f'{AMBIENTE_URL}/titulo-usf/cobranca/v3/beneficiarios/{uuidBeneficiario}/titulos'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}',
            'cooperativa': '515'
        }
        response = requests.post(url, headers=headers, json=boleto_body)
        uuid_titulo = response.text
        print(uuid_titulo)
        return uuid_titulo