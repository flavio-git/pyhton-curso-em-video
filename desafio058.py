"""
Melhore o jogo do DESAFIO028 onde o computador vai
"pensar" um em número entre 0 e 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer
"""

from random import randint

numero_computador = randint(0, 10)
tentativas = 0

print('Tente adivinhar o número escolhido pelo computador.')
controle = False
while not controle:
    numero_usuario = int(input('Digite um número: '))
    tentativas += 1
    if numero_usuario == numero_computador:
        print(f'Parabéns você acertou em {tentativas} tentativas. '
              f'O número escolhido pelo computador era {numero_computador}.')
        controle = True
    else:
        print('Você errou. Tente novamente.')
