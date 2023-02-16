"""
Modifique as funções criadas no desafio107 para aceitem um
parâmetro a mais, informando se o valor retornado por elas
vai ser ou não formatado pela função moeda(), do desafio108
"""


import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}.')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}.')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(preco, 10, True)}.')
print(f'Reduzindo 13%, temos R$ {moeda.diminuir(preco, 13, True)}.')

moeda.moeda(preco)
