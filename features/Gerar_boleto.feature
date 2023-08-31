Feature: Geracão de boletos

  Background:
    Given que informo o uuidBeneficiario "00FB8823A6F645D2B788D128356F82C6" e a variacao carteira "84256"

  Scenario: Gerar boleto com sucesso
    When que realizo a requisicão de gerar boleto
    Then é criado o uuidTitulo com sucesso
