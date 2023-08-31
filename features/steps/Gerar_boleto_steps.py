import uuid

from behave import given, when , then

from unicred.common.actions.boleto import Boletos
from unicred.common.utils.bodies import gerar_boleto_body


@given('que informo o uuidBeneficiario "{uuid}" e a variacao carteira "{carteira}"')
def step_impl(context, uuid, carteira):
    context.uuid = uuid
    context.carteira = carteira
    context.boleto_body = gerar_boleto_body(carteira)
    print(type(context.boleto_body))

@when('que realizo a requisicão de gerar boleto')
def step_impl(context):
    boleto_instancia = Boletos()
    context.uuid_titulo = boleto_instancia.gerar_boleto_normal(context.uuid, context.carteira, context.boleto_body)

@then('é criado o uuidTitulo com sucesso')
def step_impl(context):
    uuid_titulo = context.uuid_titulo.strip()
    try:
        uuid.UUID(uuid_titulo, version=4)
        assert True, f"UUIDTitulo gerado com sucesso: {uuid_titulo}"
    except ValueError:
        assert False, f"Resposta não é um UUID válido: {uuid_titulo}"