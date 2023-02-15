"""
Crie um programa que tenha a função leia_int(),
que vai funcionar de forma semelhante à função
input() do Python, só que fazendo a validação
para aceitar apenas um valor numérico.
"""


def leia_int(msg=''):
    """
    read an input from user and checks if the input it's an integer number
    :param msg: a message to the user
    :return: return an integer number
    """
    while True:
        leitura_usuario = input(msg)
        if leitura_usuario.isdigit():
            return int(leitura_usuario)
        else:
            print('Você deve digitar um número. Tente novamente.')


n = leia_int('Digite um número: ')
print(n)
