"""
Escreva um programa que leia um número n inteiro
qualquer e mostre na tela os n primeiros elementos
de uma sequência fibonacci
"""

numero = int(input('Digite um número: '))

penultimo = 0
ultimo = 1

controle = 0
while controle < numero:
    if controle <= 1:
        print(f'{controle} ', end='')
    else:
        atual = ultimo + penultimo
        print(f'{atual} ', end='')
        penultimo = ultimo
        ultimo = atual

    controle += 1
