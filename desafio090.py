"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No
final, mostre o conteúdo da estrutura na tela.
"""

aluno = dict()
aluno['Nome'] = input('Digite o nome do aluno: ')
aluno['Nota'] = float(input('Digite a nota final do aluno: '))

if aluno['Nota'] >= 6:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

print('\nInformações do dicionário: ')

print('\nKeys: ')
for i in aluno.keys():
    print(i)

print('\nValues: ')
for i in aluno.values():
    print(i)

