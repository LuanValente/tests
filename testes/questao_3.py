import json

# Dados de faturamento em formato JSON
dados_faturamento = [
    {
        "dia": 1,
        "valor": 22174.1664
    },
    {
        "dia": 2,
        "valor": 24537.6698
    },
    {
        "dia": 3,
        "valor": 26139.6134
    },
    {
        "dia": 4,
        "valor": 0.0
    },
    {
        "dia": 5,
        "valor": 0.0
    },
    {
        "dia": 6,
        "valor": 26742.6612
    },
    {
        "dia": 7,
        "valor": 0.0
    },
    {
        "dia": 8,
        "valor": 42889.2258
    },
    {
        "dia": 9,
        "valor": 46251.174
    },
    {
        "dia": 10,
        "valor": 11191.4722
    },
    {
        "dia": 11,
        "valor": 0.0
    },
    {
        "dia": 12,
        "valor": 0.0
    },
    {
        "dia": 13,
        "valor": 3847.4823
    },
    {
        "dia": 14,
        "valor": 373.7838
    },
    {
        "dia": 15,
        "valor": 2659.7563
    },
    {
        "dia": 16,
        "valor": 48924.2448
    },
    {
        "dia": 17,
        "valor": 18419.2614
    },
    {
        "dia": 18,
        "valor": 0.0
    },
    {
        "dia": 19,
        "valor": 0.0
    },
    {
        "dia": 20,
        "valor": 35240.1826
    },
    {
        "dia": 21,
        "valor": 43829.1667
    },
    {
        "dia": 22,
        "valor": 18235.6852
    },
    {
        "dia": 23,
        "valor": 4355.0662
    },
    {
        "dia": 24,
        "valor": 13327.1025
    },
    {
        "dia": 25,
        "valor": 0.0
    },
    {
        "dia": 26,
        "valor": 0.0
    },
    {
        "dia": 27,
        "valor": 25681.8318
    },
    {
        "dia": 28,
        "valor": 1718.1221
    },
    {
        "dia": 29,
        "valor": 13220.495
    },
    {
        "dia": 30,
        "valor": 8414.61
    }
]

# Função para calcular o menor valor de faturamento
def calcular_menor_faturamento(dados):
    menor_valor = float('inf')
    for item in dados:
        if item['valor'] < menor_valor:
            menor_valor = item['valor']
    return menor_valor

# Função para calcular o maior valor de faturamento
def calcular_maior_faturamento(dados):
    maior_valor = float('-inf')
    for item in dados:
        if item['valor'] > maior_valor:
            maior_valor = item['valor']
    return maior_valor

# Função para calcular o número de dias com faturamento acima da média mensal
def calcular_dias_acima_media(dados):
    soma_valores = 0
    for item in dados:
        soma_valores += item['valor']
    media_mensal = soma_valores / len(dados)
    count_dias_acima_media = 0
    for item in dados:
        if item['valor'] > media_mensal:
            count_dias_acima_media += 1
    return count_dias_acima_media

# Chamar as funções e exibir os resultados
print("Menor valor de faturamento: R$", calcular_menor_faturamento(dados_faturamento))
print("Maior valor de faturamento: R$", calcular_maior_faturamento(dados_faturamento))
print("Número de dias com faturamento acima da média mensal:", calcular_dias_acima_media(dados_faturamento))