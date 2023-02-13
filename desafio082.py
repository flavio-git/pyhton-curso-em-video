"""
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
"""

numeros = []
pares = []
impares = []

while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    opcao_mais_numero = input('Deseja adicionar mais um número: [S/N] ')

    if opcao_mais_numero in 'Nn':
        break

print(f'Números digitados: {numeros}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')
