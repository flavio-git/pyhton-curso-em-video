"""
Refaça o desafio035, acrescentando o recurso de
mostrar que tipo de triângulo será formado:

— equilátero: todos os lados iguais
— isósceles: dois lados iguais
— escaleno: todos os lados diferentes
"""

primeiro = int(input('Primeiro segmento: '))
segundo = int(input('Segundo segmento: '))
terceiro = int(input('Terceiro segmento: '))

if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    if primeiro == segundo == terceiro:
        print('Triângulo Equilátero')
    elif primeiro == segundo or primeiro == terceiro or segundo == terceiro:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Não pode-se formar um triângulos com os valores digitados')
