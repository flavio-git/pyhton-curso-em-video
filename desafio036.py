"""
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será
negado.
"""

valor_casa = float(input('Valor da casa: '))
salario = float(input('Salário mensal: '))
anos_pagamento = int(input('Em quantos anos será paga: '))

quantidade_meses = anos_pagamento * 12
parcela_mensal_casa = valor_casa / quantidade_meses

percentual_parcela_em_relacao_salario = (parcela_mensal_casa / salario) * 100

print('=' * 30)
print('Informações sobre a negociação')
print('=' * 30)

print(f'Quantidade de meses para pagamento: {quantidade_meses}')
print(f'Valor da parcela mensal: R$ {parcela_mensal_casa:.2f}')
print(f'Percentual da parcela em relação ao salário: {percentual_parcela_em_relacao_salario:.2f}%')

if percentual_parcela_em_relacao_salario <= 30:
    print('O empréstimo foi concedido.')
else:
    print('O empréstimo não foi concedido.')
