import requests

def test_get_limites(token):
    response = requests.get(f'{url_path_aqui}/limite-transacao-us/canais/limite-transacao/v2/contas/27/usuarios/19541/limites',
                        headers={'Content-Type': 'application/json;charset=UTF-8', 'Authorization': token, 'cooperativa': '0000'})

    assert response.json()[0]['id'] is not None
    assert response.status_code == 200
    assert response.json()[0]['codigoTransacao'] == 21
    id_do_limite = response.json()[0]['id']
    return id_do_limite