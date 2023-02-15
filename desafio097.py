"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
"""


def escreva(mensagem):
    tamanho_mensagem = len(mensagem)
    print('~' * (tamanho_mensagem + 2))
    print(f'{" ":<1}{mensagem:^}{" ":>1}')
    print('~' * (tamanho_mensagem + 2))


escreva('Flavio Vicentini')
escreva('Curso de Python no Youtube')
escreva('POA')
