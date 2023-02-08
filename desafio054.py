"""
Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são
"""

from datetime import date

maiores_de_idade = 0

for i in range(1, 8):
    idade = date.today().year - int(input(f'{i} - Ano de nascimento: '))
    if idade >= 18:
        maiores_de_idade += 1

print(f'Total de pessoas maiores de 18 anos: {maiores_de_idade}')
print(f'Total de pessoas menores de 18 anos: {7 - maiores_de_idade}')
