"""
Faça um programa que leia um ano
qualquer e mostre se ele é BISSEXTO.

Condições para ano bissexto:
1) divisível por 4
2) não ser divisível por 100
"""

ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    if ano % 100 != 0:
        print(f'{ano} é um ano bissexto.')
    else:
        print(f'{ano} não é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')


