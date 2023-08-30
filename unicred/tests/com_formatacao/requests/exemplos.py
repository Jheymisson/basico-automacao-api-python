from unicred.common.actions.boleto import Boletos
from unicred.tests.com_formatacao.delete_limites_tests import tests_delete_limite_sucesso
from unicred.tests.com_formatacao.get_limites_tests import test_get_limites
from unicred.tests.com_formatacao.post_limites_tests import test_post_limites
from unicred.tests.com_formatacao.put_limites_tests import tests_put_limites

token = 'Bearer --ieOn5bQWm9_hT7LTijN9jmHMEWroyMN275fvi-6J52Dml0UDVCkjvpyBobVuzxStmDEVHA8LH9xs_5w'

# Testes basicos

# # Busca
# id_retornado1 = test_get_limites(token)
# print(id_retornado1)
# # Deleta
# tests_delete_limite_sucesso(token, id_retornado1)
# # Cria
# test_post_limites(token)
# # Busca
# id_retornado2 = test_get_limites(token)
# print(id_retornado2)
# # Atualiza
# tests_put_limites(token, id_retornado2)


# Testes com dois ambientes e o token dinamico
boleto_normal = Boletos()
uuid_titulo = boleto_normal.gerar_boleto_normal()