"""
Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário
incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()
numero_de_gols = list()

jogador['nome'] = input('Nome do Jogador: ')

numero_de_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

for i in range(0, numero_de_partidas):
    quantidade_gols_partida = int(input(f'  Quantos gols na partida {i + 1}? '))
    numero_de_gols.append(quantidade_gols_partida)

jogador['gols'] = numero_de_gols
jogador['total'] = sum(numero_de_gols)

print('-=' * 30)

print(jogador)

print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {str(k).capitalize()} tem o valor {v}')

print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {numero_de_partidas} partidas:')

for pos, i in enumerate(jogador['gols']):
    print(f'    => Na partida {pos + 1}, fez {i} gols.')

print(f'Foi um total de {jogador["total"]} gols.')



