'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''
import json

with open ("dados.json") as file:
    dados = json.load(file)


# Função pra tirar os valores 0
def tirandoZero(dados):
    return [ item for item in dados if item['valor'] != 0]

semZero = tirandoZero(dados)





# Função mostrar o menor valor
def menorvalor(semZero):
    return min(semZero, key=lambda d : d['valor'])

menor_valor = menorvalor(semZero)
print(f"O menor valor de faturamento ocorrido em um dia do mês: {menor_valor}")






# Função mostrar o maior valor:
def maiorvalor(semZero):
    return max(semZero, key=lambda d : d['valor'])

maior_valor = maiorvalor(semZero)
print(f"O maior valor de faturamento ocorrido em um dia do mês: {maior_valor}")





# Média dos valores: 
soma_dados = 0
dias_com_faturamento = 0
for dia in dados:
    if dia['valor'] != 0:
        soma_dados += dia['valor']
        dias_com_faturamento += 1
media = soma_dados / dias_com_faturamento
print(f"A média é: {media}")
