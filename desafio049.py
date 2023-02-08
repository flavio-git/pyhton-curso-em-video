"""
Refaça o desafio009, mostrando a tabuada de
um número que o usuário escolher, só que agora
utilizando um laço for
"""

numero = int(input('Tabuada de qual número você quer: '))
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')
