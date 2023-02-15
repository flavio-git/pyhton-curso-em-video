"""
Crie um programa que tenha uma função fatorial() que receba
dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o cáculo.
"""

import math


def fatorial(n, show=False):
    res = 1
    if show:
        for i in range(n, 0, -1):
            res *= i
            if i != 1:
                print(f'{i} x ', end='')
            else:
                print(f'{i} = {res}')
    else:
        for i in range(n, 0, -1):
            res *= i
        return res


fatorial(20, show=True)
