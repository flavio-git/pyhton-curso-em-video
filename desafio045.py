"""
Crie um programa que o faça o computador
jogar Jokenpô com você.
"""

from random import randint

possibilidades = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
jogada_computador = possibilidades.get(randint(1, 3))

print("""Escolha um jogada:
[1] Pedra
[2] Papel
[3] Tesoura""")
jogada_usuario = int(input('Digite sua opção: '))
jogada = possibilidades.get(jogada_usuario)

if jogada == 'Pedra' and jogada_computador == 'Tesoura':
    print(f'Sua jogada {jogada} e do computador {jogada_computador}. VOCÊ GANHOU!')
elif jogada == 'Papel' and jogada_computador == 'Pedra':
    print(f'Sua jogada {jogada} e do computador {jogada_computador}. VOCÊ GANHOU!')
elif jogada == 'Tesoura' and jogada_computador == 'Papel':
    print(f'Sua jogada {jogada} e do computador {jogada_computador}. VOCÊ GANHOU!')
elif jogada == jogada_computador:
    print(f'Sua jogada {jogada} e do computador {jogada_computador}. EMPATE!')
else:
    print(f'Sua jogada {jogada} e do computador {jogada_computador}. VOCÊ PERDEU!')
