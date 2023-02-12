"""
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você de mostrar, para
cada palavra, quais são as suas vogais.
"""

palavras = ('Casa', 'Games', 'Escola', 'Carro', 'Predio', 'Praia', 'Bola', 'Computador', 'Futebol')
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
    print(f'{palavra} --> Vogais: ', end='')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end=' ')
    print()
