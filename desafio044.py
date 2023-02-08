"""
Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço atual e a
condição de pagamento:

— à vista dinheiro/cheque: 10% de desconto
— à vista no cartão: 5% de desconto
— em até 2x no cartão: preço normal
— 3x ou mais no cartão: 20% de juros
"""

preco_produto = float(input('Digite o preço do produto: '))
print("""Escolha uma das opções de pagamento abaixo:
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros""")
opcao = int(input('Qual a forma de pagamento escolhida: '))

if opcao == 1:
    desconto = preco_produto * 0.10
    print(f'Preço do produto: {preco_produto}, '
          f'valor do desconto: {desconto}, '
          f'total a pagar: {preco_produto - desconto}')
elif opcao == 2:
    desconto = preco_produto * 0.05
    print(f'Preço do produto: {preco_produto}, '
          f'valor do desconto: {desconto}, '
          f'total a pagar: {preco_produto - desconto}')
elif opcao == 3:
    print(f'Não há juros ou desconto nessa forma de pagamento. Total a pagar: {preco_produto}')
elif opcao == 4:
    juros = preco_produto * 0.20
    print(f'Preço do produto: {preco_produto}, '
          f'valor do juros: {juros}, '
          f'total a pagar: {preco_produto + juros}')
else:
    print('Opção inválida.')
