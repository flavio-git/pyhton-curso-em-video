"""
Faça um programa que tenha uma função chamada area(),
que receba as dimensões de um terrano retangular
(largura e comprimento) e mostre a área do terreno.
"""


def area(comprimento, largura):
    valor_area = largura * comprimento
    print(f'A área de um terreno {comprimento}x{largura} é de {valor_area:.2f} metros quadrado.')


print('Controle de Terrenos')
print('-' * 20)
comprimento = float(input('LARGURA (m): '))
largura = float(input('COMPRIMENTO (m): '))
area(comprimento, largura)
