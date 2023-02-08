"""
Crie um programa que receba três valores
e verifique se esses valores obedecem às
condições para formar um triângulo.
"""

primeiro = int(input('Primeiro segmento: '))
segundo = int(input('Segundo segmento: '))
terceiro = int(input('Terceiro segmento: '))

# solução 1
if abs(segundo - terceiro) < primeiro < (segundo + terceiro):
    print('Pode-se formar um triângulo com os valores digitados.')
else:
    print('Não pode-se formar um triângulos com os valores digitados')

# solução 2
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Pode-se formar um triângulo com os valores digitados.')
else:
    print('Não pode-se formar um triângulos com os valores digitados')
