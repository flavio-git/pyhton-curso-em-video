"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá se o usuário vai continuar. No final, mostre

a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
"""

total_gasto = 0
quantidade_produtos_mais_100 = 0
produto_mais_barato_nome = 0
produto_mais_barato_valor = 0

print('CADASTRANDO COMPRAS')

i = 0
while True:
    nome_produto = input('Nome do produto: ')
    preco_produto = float(input('Preço do produto: '))

    total_gasto += preco_produto

    if preco_produto > 1000:
        quantidade_produtos_mais_100 += 1

    if i == 0:
        produto_mais_barato_nome = nome_produto
        produto_mais_barato_valor = preco_produto
    else:
        if preco_produto < produto_mais_barato_valor:
            produto_mais_barato_nome = nome_produto
            produto_mais_barato_valor = preco_produto

    i += 1

    print('Deseja adicionar mais um produto?')
    continuar = int(input('1 - Sim | 2 - Sair do programa: '))

    if continuar == 2:
        break


print(f'\nValor total compra: {total_gasto}')
print(f'Quantidade produtos com valor superior R$ 1.000,00: {quantidade_produtos_mais_100}')
print(f'Produto mais barato: {produto_mais_barato_nome} R$ {produto_mais_barato_valor}')
