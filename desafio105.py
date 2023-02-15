"""
Faça um programa que tenha uma função notas() que
pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:

— quantidade de notas
— a maior nota
— a menor nota
— a média da turma
— a situação (opcional)
"""


def notas(*n, sit=False):
    informacoes = dict()
    informacoes['total'] = len(n)
    informacoes['maior'] = max(n)
    informacoes['menor'] = min(n)
    informacoes['media'] = sum(n) / len(n)
    if sit:
        if informacoes['media'] >= 7:
            informacoes['situacao'] = 'BOA'
        elif 5 < informacoes['media'] < 7:
            informacoes['situacao'] = 'RAZOÁVEL'
        else:
            informacoes['situacao'] = 'MELHORAR'
    return informacoes


aluno = notas(9, 6, 7, 8, sit=True)
print(aluno)
