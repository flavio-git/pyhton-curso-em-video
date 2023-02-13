"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vair sortear
6 números entre 1 e 60 para jogo, cadastrando tudo em uma lista composta
"""

from random import randint
from time import sleep

print('=' * 30)
print('{:^30}'.format('MEGA SENA'))
print('=' * 30)

quantidade_de_jogos = int(input('Quantos jogos você quer sortear? '))

jogos_gerados = list()

for i in range(0, quantidade_de_jogos):
    jogo = list()

    for g in range(0, 6):
        numero_gerado = randint(1, 60)

        if numero_gerado not in jogo:
            jogo.append(numero_gerado)

    jogos_gerados.append(jogo.copy())
    jogo.clear()

print('=' * 30)
print('{:^30}'.format(f'NUMEROS GERADOS PARA {quantidade_de_jogos} JOGOS'))
print('=' * 30)
for pos, jogo in enumerate(jogos_gerados):
    print(f'Jogo {pos + 1}: {sorted(jogo)}')
    sleep(0.5)
