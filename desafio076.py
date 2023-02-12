"""
Crie um programa que tenha uma tupla única com
de produtos e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando
os dados em forma tabular.
"""

produtos = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidos', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

i = 0
while i < len(produtos):
    print(f'{produtos[i]:.<30} R${produtos[i + 1]:>7.2f}')
    i += 2

print('-' * 40)
