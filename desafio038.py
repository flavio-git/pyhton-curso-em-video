"""
Escreva um programa que leia dois números inteiros e
compare-os, mostrando uma mensagem na tela informando
qual é o maior número ou se há igualdade entre eles.
"""

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

if numero_1 > numero_2:
    print('O primeiro valor é maior: {} > {}'.format(numero_1, numero_2))
elif numero_2 > numero_1:
    print('O segundo valor é maior: {} > {}'.format(numero_2, numero_1))
else:
    print('Os dois números são iguais')

