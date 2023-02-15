"""
Faça um progama que tenha uma lista chamada números e duas
funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro de uma lista
e a segundo função vai mostrar a soma entre todos os valores
PARES sorteados pela função anterior.
"""

from random import randint
from time import sleep


def sortea_numeros(quantidade_numeros):
    numeros_sorteados = list()
    print(f'Sorteando {quantidade_numeros} valores: ', end='')
    for i in range(0, quantidade_numeros):
        numero = randint(1, 100)
        print(numero, end=' ')
        numeros_sorteados.append(numero)
        sleep(0.4)
    print('PRONTO!')
    return numeros_sorteados


def soma_pares(arg):
    pares = list()
    for i in arg:
        if i % 2 == 0:
            pares.append(i)
    print(f'Somando os valores pares de {arg}, temos {sum(pares)}.')


print('-=' * 30)
soma_pares(sortea_numeros(5))
print('-=' * 30)
soma_pares(sortea_numeros(10))
