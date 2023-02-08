"""
Desenvolva um programa que leia seis números
inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar,
desconsidere-o
"""

somatorio = 0
for i in range(1, 7):
    numero = int(input(f'Digite o {i}: '))
    if numero % 2 == 0:
        somatorio += numero

print('Soma dos números pares digitados: {}'.format(somatorio))
