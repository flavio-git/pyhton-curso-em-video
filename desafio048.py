"""
Faça um programa que calcule a soma entre todos
os números ímpares que são múltiplos de três e
que se encontram no intervalo de 1 até 500
"""

somatorio = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        somatorio += i
        print(f'i = {i} -> {somatorio}')
        