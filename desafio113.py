"""
Reescreva a função leia_int() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leia_float()
com a mesma funcionalidade.
"""

from utilidades import dado

try:
    valor_inteiro = dado.leia_int_exception('Digite um número inteiro: ')
    valor_real = dado.leia_float_exception('Digite um número real: ')
except KeyboardInterrupt:
    print('\nUsuário interrompendo a execusão do programa.')
else:
    print(f'O valor inteiro digitado foi {valor_inteiro} e o real foi {valor_real:.2f}.')
