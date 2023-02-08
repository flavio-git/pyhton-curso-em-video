"""
Faça um programa que leia o peso de cinco
pessoas. No final, mostre qual foi o maior
e o menor peso
"""

maior_peso = 0
menor_peso = 0

for i in range(1, 6):
    peso = float(input(f'{i}. Peso = '))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso

print(f'Maior peso: {maior_peso}')
print(f'Menor peso: {menor_peso}')
