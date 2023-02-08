"""
Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
"""

numero = int(input('Digite um número: '))
tem_divisor = False
for i in range(2, numero):
    if numero % i == 0:
        tem_divisor = True

if tem_divisor:
    print(f'O número {numero} não é primo.')
else:
    print(f'O número {numero} é primo.')

