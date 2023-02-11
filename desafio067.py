"""
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando um número solicitado
for negativo
"""

while True:
    numero = int(input("""Digite um número para ver a tabuada dele ou
digite um número negativo para parar o programa: """))

    if numero > 0:
        for i in range(1, 11):
            print(f'{i} x {numero}: {i * numero}')
    else:
        break
