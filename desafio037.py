"""
Escreve um programa que leia um número inteiro
qualquer e peça para o utilizador escolher qual
será a base de conversão:

1. binária
2. octal
3. hexadecimal
"""


def decimal_para_binario(numero):
    binario = []
    quociente = numero // 2
    binario.insert(0, str(numero % 2))
    while quociente > 0:
        binario.insert(0, str(quociente % 2))
        quociente = quociente // 2
    return ''.join(binario)


def decimal_para_octal(numero):
    octal = []
    quociente = numero // 8
    octal.insert(0, str(numero % 8))
    while quociente > 0:
        octal.insert(0, str(quociente % 8))
        quociente = quociente // 8
    return ''.join(octal)


def decimal_para_hexadecimal(numero):
    hexadecimal = []
    quociente = numero // 16
    hexadecimal.insert(0, str(representacao_hexadecimal(numero % 16)))
    while quociente > 0:
        hexadecimal.insert(0, str(representacao_hexadecimal(quociente % 16)))
        quociente = quociente // 16
    return ''.join(hexadecimal)


def representacao_hexadecimal(numero):
    if numero < 10:
        return numero
    elif numero == 10:
        return 'A'
    elif numero == 11:
        return 'B'
    elif numero == 12:
        return 'C'
    elif numero == 13:
        return 'D'
    elif numero == 14:
        return 'E'
    elif numero == 15:
        return 'F'


numero = int(input('Digite um número: '))
print(f'''Você quer converter o número {numero} para qual base:
[1] Base Binária
[2] Base Octal
[3] Base Hexadecimal''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'Número em Decimal: {numero} | Número em Binário: {decimal_para_binario(numero)}')
elif opcao == 2:
    print(f'Número em Decimal: {numero} | Número em Octal: {decimal_para_octal(numero)}')
elif opcao == 3:
    print(f'Número em Decimal: {numero} | Número em Hexadecimal: {decimal_para_hexadecimal(numero)}')
else:
    print('Opção inválida. Tente novamente.')
