"""
Crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta
"""

lista = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# solução utilizando o While

# linha = 0
# while linha < len(lista):
#     coluna = 0
#     while coluna < len(lista[linha]):
#         numero = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
#         lista[linha][coluna] = numero
#         coluna += 1
#     linha += 1


# solução utilizando o For

for linha, i in enumerate(lista):
    for coluna, g in enumerate(lista[linha]):
        numero = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        lista[linha][coluna] = numero

for linha, i in enumerate(lista):
    for coluna, g in enumerate(lista[linha]):
        print(f'[ {g} ]', end=' ')
    print()
