# Dados de faturamento mensal por estado
faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcular o valor total mensal de faturamento
valor_total_mensal = sum(faturamento_mensal.values())

# Função para calcular o percentual de representação de cada estado
def calcular_percentual_representacao(estado_faturamento, valor_total):
    percentual = (estado_faturamento / valor_total) * 100
    return round(percentual, 2)

# Calcular o percentual de representação de cada estado
percentuais = {}
for estado, faturamento in faturamento_mensal.items():
    percentual = calcular_percentual_representacao(faturamento, valor_total_mensal)
    percentuais[estado] = percentual

# Exibir os resultados
print("Percentual de representação do faturamento mensal por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual}%")