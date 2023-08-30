import requests

token = 'Bearer -'

response = requests.post(f'{url_path_aqui}/limite-transacao-us/canais/limite-transacao/v2/contas/27/usuarios/19541/transacoes/PAGAMENTO_TITULO/limites',
                        headers={'Content-Type': 'application/json;charset=UTF-8', 'Authorization': token, 'cooperativa': '0000'},
                        json={"dataHoraFim":"2023-09-29T20:00:56.035Z", "dataHoraInicio": "2023-09-29T10:00:00.035Z",
                            "numeroCooperativa": "4022", "valorMaximo": "100000000","valorTotalDiario": "100000000"}
                        )

assert response.status_code == 201

