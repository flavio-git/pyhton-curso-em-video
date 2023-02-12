"""
Crie um programa que vai gerar cinco números aleatórios
e colocar em um tupla.

Depois disso, mostre a listagem de números gerados e
também indique o menor e o maior valor que estão ma tupla.
"""

from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(f'Números gerados: {numeros}')
print(f'Classificando os números: {sorted(numeros)}')
print(f'Maior número: {max(numeros)}')
print(f'Menor número: {min(numeros)}')

# implementação dos algoritmos
maior_numero = 0
menor_numero = 0

for pos, numero in enumerate(numeros):
    if pos == 0:
        maior_numero = numero
        menor_numero = numero
    else:
        if numero > maior_numero:
            maior_numero = numero
        elif numero < menor_numero:
            menor_numero = numero

# print(f'Maior número: {maior_numero}')
# print(f'Menor número: {menor_numero}')
