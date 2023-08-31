import requests
import yaml

with open('/Volumes/trabalho/pocs/automacao/treinamento_basico_automacao_zallpy/unicred/common/utils/env.yaml', 'r') as file:
    config = yaml.safe_load(file)

AMBIENTE = config['ambiente']

if AMBIENTE == 'tst':
    AMBIENTE_URL = '{url_path}'
    OAUTH_URL = '{url_path}/auth/realms/UnicredRealm/protocol/openid-connect/token'
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    PASSWORD = ''
elif AMBIENTE == 'hlg':
    AMBIENTE_URL = '{url_path_hlg_aqui}'
    OAUTH_URL = '{url_path}/auth/realms/UnicredRealm/protocol/openid-connect/token'
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    PASSWORD = ''
else:
    raise ValueError("Ambiente desconhecido")

def gerar_token():
    bodies_uni = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'username': 'sys.cheque_legal',
        'password': PASSWORD,
        'grant_type': 'password'
    }
    headers_uni = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.post(OAUTH_URL, headers=headers_uni, data=bodies_uni)
    if response.status_code == 200:
        token_unicred = response.json()
        return token_unicred['access_token']
    else:
        print('error')