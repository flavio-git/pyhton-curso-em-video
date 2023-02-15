"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de
uma pessoa, retornando um valor literal indicando se
uma pessoa tem voto, NEGADO, OPCIONAL ou OBRIGATÓRIO
nas eleições.
"""

from datetime import date


def voto(nascimento):
    idade = date.today().year - nascimento
    if 18 <= idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO NEGADO'


ano_nascimento = int(input('Digite seu ano de nascimento: '))
print(voto(ano_nascimento))
