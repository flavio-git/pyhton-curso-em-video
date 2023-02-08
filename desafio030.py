"""
Crie um programa que leia um número inteiro
e mostra na tela se ele é PAR ou ÍMPAR.
"""

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'{numero} é um número par.')
else:
    print(f'{numero} é um número ímpar.')
