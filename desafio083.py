"""
Crie um programa onde o usuário digite uma expressão
qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os os parênteses
abertos e fechados na ordem correta.
"""

expressao = input('Digite sua fórmula: ')

caracteres_expressao = []

for caractere in expressao:
    caracteres_expressao.insert(0, caractere)

if caracteres_expressao.count('(') == caracteres_expressao.count(')'):
    print('Números de parênteses está correto.')
elif caracteres_expressao.count('(') > caracteres_expressao.count(')'):
    print('Número de parênteses está incorreto. Está faltando um ")"')
else:
    print('Número de parênteses está incorreto. Está faltando um "("')


if expressao.count('(') == expressao.count(')'):
    print('Números de parênteses está correto.')
elif expressao.count('(') > expressao.count(')'):
    print('Número de parênteses está incorreto. Está faltando um ")"')
else:
    print('Número de parênteses está incorreto. Está faltando um "("')
