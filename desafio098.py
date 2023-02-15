"""
Faça um programa que tenha uma função chamada contador(), que receba
três parâmetros: início, fim e passo e realiza a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep


def contagem(inicio, fim, passo):
    passo = 1 if passo == 0 else passo
    if inicio < fim:
        for i in range(inicio, (fim + 1), passo):
            print(i, end=' ')
            sleep(0.25)
        print('FIM')
    elif inicio > fim:
        for g in range(inicio, (fim - 1), (passo if passo < 0 else passo * -1)):
            print(g, end=' ')
            sleep(0.25)
        print('FIM')
    else:
        print('Argumentos digitados são inválidos')


print('-=' * 30)
contagem(1, 10, 1)
print('-=' * 30)
contagem(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio_usuario = int(input(f'{"Início: ":<10}'))
fim_usuario = int(input(f'{"Fim: ":<10}'))
passo_usuario = int(input(f'{"Passo: ":<10}'))
contagem(inicio_usuario, fim_usuario, passo_usuario)

