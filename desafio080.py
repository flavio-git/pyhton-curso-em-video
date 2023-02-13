"""
Crie um programa onde o usuário possa digitar cinco valores
numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""

valores = []

for i in range(0, 5):
    numero = int(input('Digite um número: '))

    if i == 0 or numero > valores[-1]:
        valores.append(numero)
    else:
        for posicao, valor in enumerate(valores):
            if numero < valor:
                valores.insert(posicao, numero)
                break

print(f'Números digitados: {valores}')
