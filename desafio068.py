"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo.
"""

from random import randint

quantidade_vitorias = 0

while True:
    numero_computador = randint(1, 10)
    numero_usuario = int(input('\nDigite um número: '))
    soma = numero_usuario + numero_computador
    opcao_usuario = input('Par [P] ou Ímpar [I]: ')

    if (numero_usuario + numero_computador) % 2 == 0 and opcao_usuario in 'Pp':
        quantidade_vitorias += 1
        print(f'GANHOU DEU PAR --> Você {numero_usuario} + Computador {numero_computador} = {soma}')
    elif (numero_usuario + numero_computador) % 2 == 1 and opcao_usuario in 'Ii':
        quantidade_vitorias += 1
        print(f'GANHOU DEU ÍMPAR --> Você {numero_usuario} + Computador {numero_computador} = {soma}')
    elif (numero_usuario + numero_computador) % 2 == 0 and opcao_usuario in 'Ii':
        print(f'PERDEU DEU PAR --> Você {numero_usuario} + Computador {numero_computador} = {soma}')
        break
    else:
        print(f'PERDEU DEU ÍMPAR --> Você {numero_usuario} + Computador {numero_computador} = {soma}')
        break


print(f'\nQuantidade de vitórias: {quantidade_vitorias}')
