"""
A confederação nacional de natação precisa de um
programa que leia o ano de nascimento de um atleta
e mostre a sua categoria, de acordo com a idade:

— até 9 anos: MIRIM
— até 14 anos: INFANTIL
— até 19 anos: JUNIOR
— até 20 anos: SÊNIOR
— acima: MASTER
"""

from datetime import date

ano_nascimento_atleta = int(input('Digite o ano de nascimento do atleta: '))
idade_atleta = date.today().year - ano_nascimento_atleta

if idade_atleta <= 9:
    print(f'Idade do atleta: {idade_atleta}, categoria: MIRIM')
elif 9 < idade_atleta <= 14:
    print(f'Idade do atleta: {idade_atleta}, categoria: INFANTIL')
elif 14 < idade_atleta <= 19:
    print(f'Idade do atleta: {idade_atleta}, categoria: JUNIOR')
elif 19 < idade_atleta <= 20:
    print(f'Idade do atleta: {idade_atleta}, categoria: SÊNIOR')
else:
    print(f'Idade do atleta: {idade_atleta}, categoria: MASTER')
