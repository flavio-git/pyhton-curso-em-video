"""
Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-os (com idade) em
um dicionário se por acaso o CTPS for diferente de
Zero, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente além da idadem com
quantos anos a pessoa vai se aposentar.
"""

from datetime import date

pessoa = dict()
pessoa['nome'] = input('Nome: ')
pessoa['idade'] = date.today().year - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratacao'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (35 - (date.today().year - pessoa['contratacao'])) + pessoa['idade']

for k, v in pessoa.items():
    print(f'{str(k).capitalize()} tem o valor {v}')

