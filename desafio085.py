"""
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e ímpares em
ordem crescente.
"""

numeros = [[], []]

for i in range(0, 7):
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print(f'Pares em ordem crescente: {sorted(numeros[0])}')
print(f'Ímpares em ordem crescente: {sorted(numeros[1])}')
