"""
Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valore 'M' ou 'F'. Caso esteja
errado, peça a digitação novamente até estar correto
"""

controle = False
while not controle:
    sexo_escolhido = input('Digite o seu sexo: ')
    if sexo_escolhido in 'MmFf':
        controle = True
    else:
        print('Opção inválida. Tente novamente.')
