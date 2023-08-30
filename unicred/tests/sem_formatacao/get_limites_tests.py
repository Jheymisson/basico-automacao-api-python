import requests

token = 'Bearer .-6J52Dml0UDVCkjvpyBobVuzxStmDEVHA8LH9xs_5w'

response = requests.get(f'{url_path_aqui}/limite-transacao-us/canais/limite-transacao/v2/contas/27/usuarios/19541/limites',
                        headers={'Content-Type': 'application/json;charset=UTF-8', 'Authorization': token, 'cooperativa': '0000'})

print(response.text)
print(response.headers)
assert response.json()[0]['id'] is not None
assert response.status_code == 200
assert response.json()[0]['codigoTransacao'] == 21
assert response.json()[0]['dataHoraInicio'] == '2023-08-29T10:00:00'