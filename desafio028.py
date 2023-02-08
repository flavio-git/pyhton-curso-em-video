"""
Escreva um programa que faça o computador
"pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual
foi o número escolhido pelo computador

O programa deverá escrever na tela se o
usuário venceu ou perdeu
"""

from random import randint

numero_secreto = randint(0, 5)

numero_usuario = int(input('Digite um número entre 0 e 5: '))

print(f'Número secreto: {numero_secreto}')

if numero_secreto == numero_usuario:
    print('Você acertou o número secreto.')
else:
    print('Você errou o número secreto.')
