"""
Faça um programa que leia um número qualquer
e mostre o seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120
"""

numero = int(input('Digite um número: '))
fatorial = numero

print(f'{numero}! = {numero}', end='')

controle = 1
while numero > controle:
    fatorial *= (numero - controle)

    if controle < numero:
        print(f' x {numero - controle}', end='')

    controle += 1

print(f' = {fatorial}')
