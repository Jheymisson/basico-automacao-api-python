import requests

token = 'Bearer -ieOn5bQWm9_hT7LTijN9jmHMEWroyMN275fvi-6J52Dml0UDVCkjvpyBobVuzxStmDEVHA8LH9xs_5w'

response = requests.put(f'{url_path_aqui}/limite-transacao-us/canais/limite-transacao/v2/contas/27/usuarios/19541/transacoes/PAGAMENTO_TITULO/limites/1547485',
                        headers={'Content-Type': 'application/json;charset=UTF-8', 'Authorization': token, 'cooperativa': '000'},
                        json={"dataHoraFim":"2023-09-29T20:00:56.035Z", "dataHoraInicio": "2023-09-29T10:00:00.035Z",
                            "numeroCooperativa": "4022", "valorMaximo": "90000000","valorTotalDiario": "90000000"}
                        )

assert response.status_code == 204
