"""
Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no
final.

— abaixo de 5,0: REPROVADO
— entre 5,0 e 6,9: RECUPERAÇÃO
— 7,0 ou superior: APROVADO
"""

nota_grau_a = float(input('Digite a nota do grau A: '))
nota_grau_b = float(input('Digite a nota do grau B: '))
media_final = (nota_grau_a + nota_grau_b) / 2

if media_final < 5:
    print(f'Sua média final foi: {media_final:.2f} --> REPROVADO')
elif 5 <= media_final < 7:
    print(f"Sua média final foi: {media_final:.2f} --> RECUPERAÇÃO")
else:
    print(f'Sua média final foi: {media_final:.2f} --> APROVADO')
