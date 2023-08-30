import requests
from unicred.common.utils.bodies import dados_limite

token = 'Bearer -6J52Dml0UDVCkjvpyBobVuzxStmDEVHA8LH9xs_5w'

def tests_put_limites(token, id_limite):
    response = requests.put(f'{url_path_aqui}/limite-transacao-us/canais/limite-transacao/v2/contas/27/usuarios/19541/transacoes/PAGAMENTO_TITULO/limites/{id_limite}',
                        headers={'Content-Type': 'application/json;charset=UTF-8',
                                 'Authorization': token,
                                 'cooperativa': '0000'},
                        json=dados_limite
                        )

    assert response.status_code == 204
