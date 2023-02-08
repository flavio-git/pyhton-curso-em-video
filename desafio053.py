"""
Crie um programa que leia uma frase
qualquer e diga se ela é um palíndromo,
desconsiderando os espaços
"""

frase = input('Digite uma frase: ')
ajuste_frase = frase.replace(' ', '').strip().upper()

ultima_letra_posicao = len(ajuste_frase) - 1
check_palindromo = True

for i in range(0, len(ajuste_frase)):
    if ajuste_frase[i] != ajuste_frase[ultima_letra_posicao - i]:
        check_palindromo = False

if check_palindromo:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')


def test_palindromo_(palavra):
    palavra_ajuste = str(palavra).upper().strip().replace(' ', '')
    if palavra_ajuste == palavra_ajuste[::-1]:
        print('Test palavra 2: é palíndromo')
    else:
        print('Test palavra 2: não é palíndromo')


test_palindromo_(ajuste_frase)
