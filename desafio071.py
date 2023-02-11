"""
Crie um programa que simule o funcionamento de um
caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada
valor serão entregues
"""

print('=' * 30)
print('{:^30}'.format('BANCO PORTO ALEGRE'))
print('=' * 30)

valor_saque = int(input('Digite o valor a ser sacado: '))
valor_restante = valor_saque

quantidade_cedulas_50 = 0
quantidade_cedulas_20 = 0
quantidade_cedulas_10 = 0
quantidade_cedulas_1 = 0

while True:
    if valor_restante >= 50:
        quantidade_cedulas_50 += 1
        valor_restante -= 50
    elif valor_restante >= 20:
        quantidade_cedulas_20 += 1
        valor_restante -= 20
    elif valor_restante >= 10:
        quantidade_cedulas_10 += 1
        valor_restante -= 10
    elif valor_restante >= 1:
        quantidade_cedulas_1 += 1
        valor_restante -= 1

    if valor_restante == 0:
        break

print(f'Cédulas de 50: {quantidade_cedulas_50}')
print(f'Cédulas de 20: {quantidade_cedulas_20}')
print(f'Cédulas de 10: {quantidade_cedulas_10}')
print(f'Cédulas de 1: {quantidade_cedulas_1}')
