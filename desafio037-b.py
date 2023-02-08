"""
Arquivo desafio037.py contém os algoritmos desenvolvidos sem estudo.
Nesse arquivo estão as soluções através de pesquisas e estudos.
"""


# algoritmo para binario usando recursão
def converter_binario(numero):
    if numero >= 1:
        converter_binario(numero // 2)
    print(numero % 2, end='')


# função com in-built do Python para binário
def conversor_binario_in_built(numero):
    print(bin(numero))
    print(bin(numero).replace('0b', ''))
    print(bin(numero)[2:])


# função in-built do Python para octal
def conversor_octal_in_built(numero):
    print(oct(numero))
    print(oct(numero).replace('0o', ''))
    print(oct(numero)[2:])


# função in-built do Python para octal
def conversor_hexadecimal_in_built(numero):
    print(hex(numero))
    print(hex(numero).replace('0x', ''))
    print(hex(numero)[2:])


print('{0:10} | {1:10} | {2:10} | {3:10}'.format('Decimal', 'Binário', 'Octal', 'Hexadecimal'))
for i in range(256):
    print('{0:10}'.format(str(i)), end=' | ')
    print('{0:10}'.format(bin(i)[2:]), end=' | ')
    print('{0:10}'.format(oct(i)[2:]), end=' | ')
    print('{0:10}'.format(hex(i)[2:]))
