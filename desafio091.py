"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios. Guarde esses resultados
em um dicionário. No final, coloque esse dicionário em
ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint

numero_jogadores = 4

jogadores = dict()

for i in range(0, numero_jogadores):
    jogadores[i + 1] = randint(1, 6)

print(f'Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{" ":<3} O jogador {k} tirou {v}')

print(f'Ranking dos jogadores: ')
ranking_jogadores = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

for pos, jogador in enumerate(ranking_jogadores):
    print(f'{" ":<3} {pos + 1}. lugar: jogador {jogador[0]} com {jogador[1]}')
