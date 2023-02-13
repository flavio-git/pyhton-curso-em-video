"""
Aprimore o desafio anterior, mostrando no final:

a) a soma de todos os valores pares digitados
b) a soma dos valores da terceira coluna
c) o maior valor da segund linha
"""

lista = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

soma_pares = 0

for linha, i in enumerate(lista):
    for coluna, g in enumerate(lista[linha]):
        numero = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        lista[linha][coluna] = numero

        if numero % 2 == 0:
            soma_pares += numero

for linha, i in enumerate(lista):
    for coluna, g in enumerate(lista[linha]):
        print(f'[ {g} ]', end=' ')
    print()

print(f'A soma dos valores pares = {soma_pares}')
print(f'A soma dos valores da terceira coluna = {lista[0][2] + lista[1][2] + lista[2][2]}')
print(f'O maior valor da segunda linha = {max(lista[1])}')
