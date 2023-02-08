"""
Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com sua idade:

— se ele ainda vai se alistar ao serviço militar
— se é a hora de se alistar
— se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que
falta ou que passou do prazo.
"""

from datetime import date

ano_nascimento = int(input('Informe o ano de seu nascimento: '))
idade = date.today().year - ano_nascimento

if idade == 18:
    print('Você completará 18 anos neste ano. Favor fazer o alistamento militar.')
elif idade < 18:
    print(f'Você irá completar {idade} neste ano. Ainda faltam {18 - idade} para fazer o alistamento militar.')
else:
    print(f'Você irá completar {idade} neste ano. Você tinha que fazer alistamento militar há {idade - 18} anos.')
