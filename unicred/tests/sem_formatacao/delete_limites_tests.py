import requests

token = 'Bearer -6J52Dml0UDVCkjvpyBobVuzxStmDEVHA8LH9xs_5w'
id_limite = '1547485'
tipo_pagamento = 'PAGAMENTO_TITULO'

response = requests.delete(f'{url_path_aqui}/limite-transacao-us/canais/limite-transacao/v2/contas/27/usuarios/19541/transacoes/{tipo_pagamento}/limites/{id_limite}',
                        headers={'Content-Type': 'application/json;charset=UTF-8', 'Authorization': token, 'cooperativa': '0000'})

# assert response.status_code == 204
assert response.json()['message'] == 'Não foi encontrado limite temporário cadastrado com os dados informados'
assert response.status_code == 422
