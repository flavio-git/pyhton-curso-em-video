"""
Crie um programa que leia dois valores e
mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação
solicitada em cada caso.
"""

numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite outro número: '))

print("""
O que você deseja fazer:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")

programa_ativo = True
while programa_ativo:
    soma = numero_1 + numero_2
    multiplicacao = numero_1 * numero_2
    maior = numero_1 if numero_1 > numero_2 else numero_2

    opcao_usuario = int(input('\nQual a sua opção: '))

    if opcao_usuario == 1:
        print(f'Soma: {soma}')
    elif opcao_usuario == 2:
        print(f'Multiplicação: {multiplicacao}')
    elif opcao_usuario == 3:
        print(f'Maior número: {maior}')
    elif opcao_usuario == 4:
        numero_1 = float(input('Digite o novo valor do primeiro número: '))
        numero_2 = float(input('Digite o novo valor do segundo número: '))
    elif opcao_usuario == 5:
        print('Saindo do programa...')
        programa_ativo = False
    else:
        print('Opção inválida. Tente novamente')

