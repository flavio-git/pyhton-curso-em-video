"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e
dizer qual deles é o maior.
"""

from time import sleep


def maior(*args):
    print('-=' * 30)
    numeros = list(args)
    print('Analisando os valores passados...')
    for i in numeros:
        print(i, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    if len(numeros) > 0:
        print(f'O maior número informado foi {max(numeros)}.')
    else:
        print(f'O maior número informado foi 0.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
