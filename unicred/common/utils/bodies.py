
dados_limite = {
    "dataHoraFim":"2023-09-29T20:00:56.035Z",
    "dataHoraInicio": "2023-09-29T10:00:00.035Z",
    "numeroCooperativa": "4022",
    "valorMaximo": "40000000",
    "valorTotalDiario": "40000000"
}

gerar_boleto_body = {
    "seuNumero": "5014715",
    "pagador": {
        "tipoPessoa": "F",
        "nomeFantasia": "Grafica GeraTitulo",
        "endereco": {
            "uf": "RS",
            "cidade": "Porto Alegre",
            "logradouro": "Rua IV",
            "bairro": "Centro",
            "cep": "91720160"
        },
        "numeroDocumento": "05625316104",
        "nomeRazaoSocial": "Grafica Unicred LTDA",
        "email": "tst.gera.titulo@hotmail.com"
    },
    "juros": {
        "codigo": 1,
        "valor": "15",
        "dataInicio": "2023-09-07"
    },
    "multa": {
        "codigo": 1,
        "valor": "20",
        "dataInicio": "2023-09-10"
    },
    "valor": "100",
    "nossoNumero": "0",
    "beneficiarioVariacaoCarteira": "84256",
    "vencimento": "2023-09-02"
}