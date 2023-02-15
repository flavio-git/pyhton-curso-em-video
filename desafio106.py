"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
"""

from os import system as console


def clear_console():
    console('clear')


def mostra_manual():
    while True:
        clear_console()
        opcao = input('Função ou Biblioteca: ')

        if opcao.upper() == 'FIM':
            print('Saindo do manual...')
            break

        help(opcao)


mostra_manual()
