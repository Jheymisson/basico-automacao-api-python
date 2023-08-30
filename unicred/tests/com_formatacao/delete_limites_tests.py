import requests

tipo_pagamento = 'PAGAMENTO_TITULO'


def tests_delete_limite_sucesso(token, id_limite):
    response = requests.delete(f'{url_path_aqui}/limite-transacao-us/canais/limite-transacao/v2/contas/27/usuarios/19541/transacoes/{tipo_pagamento}/limites/{id_limite}',
                        headers={'Content-Type': 'application/json;charset=UTF-8', 'Authorization': token, 'cooperativa': '0000'})
    assert response.status_code == 204


def tests_delete_limite_erro(token, id_limite):
    response = requests.delete(f'{url_path_aqui}/limite-transacao-us/canais/limite-transacao/v2/contas/27/usuarios/19541/transacoes/{tipo_pagamento}/limites/{id_limite}',
                        headers={'Content-Type': 'application/json;charset=UTF-8', 'Authorization': token, 'cooperativa': '0000'})

    assert response.json()['message'] == 'Não foi encontrado limite temporário cadastrado com os dados informados'
    assert response.status_code == 422