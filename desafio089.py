"""
Crie um programa que leia nome e duas de vários alunos
e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que
o usuário possa mostrar as notas de cada aluno individualmente.
"""

lista_alunos = list()

while True:
    aluno = list()
    aluno_notas = list()

    nome = input('Digite nome do aluno: ')
    nota_1 = float(input('Digite a nota 1: '))
    nota_2 = float(input('Digite a nota 2: '))

    aluno_notas.append(nota_1)
    aluno_notas.append(nota_2)

    aluno.append(nome)
    aluno.append(aluno_notas.copy())

    lista_alunos.append(aluno.copy())

    aluno_notas.clear()
    aluno.clear()

    opcao_adicionar_mais_aluno = input(f'Deseja adicionar mais um aluno? [S/N]: ')

    if opcao_adicionar_mais_aluno in 'Nn':
        break

print('-' * 40)
print(f'{"No.":<4} {"NOME":<15} {"MÉDIA":<5}')
print('-' * 40)
for pos, aluno in enumerate(lista_alunos):
    print(f'{pos:<4} {aluno[0]:<15} {(sum(aluno[1]) / len(aluno[1])):>5.2}')

while True:
    print('-' * 40)
    opcao_ver_detalhe = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if opcao_ver_detalhe == 999:
        print('Saindo do programa...')
        break
    if opcao_ver_detalhe < 0 or opcao_ver_detalhe > (len(lista_alunos) - 1):
        print('Você digitou uma opção inválida. Tente novamente.')
    else:
        print(f'Notas de {lista_alunos[opcao_ver_detalhe][0]} são {lista_alunos[opcao_ver_detalhe][1]}')
