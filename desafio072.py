"""
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.
"""

numero_por_extenso = (
    'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'desoito', 'dezenove', 'vinte'
)

print('Seu número por extenso')
numero_usuario = int(input('Digite um número entre 1 e 20: '))

while numero_usuario not in range(1, 21):
    print('Você digitou um número fora do limite.')
    numero_usuario = int(input('Digite um número entre 1 e 20: '))
else:
    print(f'Seu número {numero_usuario} por extenso é {numero_por_extenso[numero_usuario - 1]}.')

