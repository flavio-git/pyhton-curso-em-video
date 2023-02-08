"""
Faça um programa que leia um três números
e mostre qual é o maior e qual é o menor.
"""

menor_numero = 0
maior_numero = 0

for i in range(3):
    numero_usuario = int(input('Digite um número: '))

    if i == 0:
        menor_numero = numero_usuario
        maior_numero = numero_usuario

    if numero_usuario < menor_numero:
        menor_numero = numero_usuario
    if numero_usuario > maior_numero:
        maior_numero = numero_usuario

print(f'Menor número: {menor_numero}')
print(f'Maior número: {maior_numero}')
