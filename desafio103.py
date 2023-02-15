"""
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um
jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do
jogador, mesmo que algum dado não tenha sido informado
incorretamente.
"""


def ficha(n, g):
    """
    Função que irá imprimir no console o nome e a quantidade de gols de jogador.
    Caso nenhum parâmetro seja passado n irá receber "<desconhecido>" e g receberá 0.
    :param n: Nome de um determinado jogador
    :param g: Quantidade de gols marcado por esse jogodar
    :return: Imprime no console as informações do jogador
    """

    if n != '':
        print(f'O jogador {n.capitalize()} fez {g} gol(s) no campeonato.')
    else:
        print(f'O jogador <desconhecido> fez {g} gol(s) no campeonato.')


nome = input('Nome do Jogador: ')
gols = input('Número de Gols: ')
gols = int(gols) if gols.isdigit() else 0

ficha(nome, gols)
