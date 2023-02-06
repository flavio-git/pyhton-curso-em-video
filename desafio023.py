"""
Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados

Ex:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

numero = input('Digite um número entre 0 e 9999: ')

if numero in range(10000):
    if len(numero) == 1:
        print(f'Unidade: {numero}')
        print(f'Dezena : {0}')
        print(f'Centena: {0}')
        print(f'Milhar : {0}')
    elif len(numero) == 2:
        print(f'Unidade: {numero[1]}')
        print(f'Dezena : {numero[0]}')
        print(f'Centena: {0}')
        print(f'Milhar : {0}')
    elif len(numero) == 3:
        print(f'Unidade: {numero[2]}')
        print(f'Dezena : {numero[1]}')
        print(f'Centena: {numero[0]}')
        print(f'Milhar : {0}')
    elif len(numero) == 4:
        print(f'Unidade: {numero[3]}')
        print(f'Dezena : {numero[2]}')
        print(f'Centena: {numero[1]}')
        print(f'Milhar : {numero[0]}')
else:
    print('Número inválido')
