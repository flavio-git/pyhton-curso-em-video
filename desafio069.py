"""
Crie um programa que leia a idade e o sexo de várias.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:

a) quantas pessoas tem mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres tem menos de 20 anos
"""

numero_pessoas_cadastradas = 0
quantidade_homens = 0
quantidade_mulheres_menor_20 = 0

while True:
    print('Cadastrando nova pessoa.')
    sexo = input('Sexo (M - masculino) (F - feminino): ')
    idade = int(input('Idade da pessoa: '))

    if sexo in 'Mm':
        quantidade_homens += 1
    elif sexo in 'Ff' and idade < 20:
        quantidade_mulheres_menor_20 += 1

    numero_pessoas_cadastradas += 1

    print('Deseja adicionar mais um pessoa?')
    continuar = int(input('1 - Sim | 2 - Sair do programa: '))

    if continuar == 2:
        break


print(f'Quantidade de pessoas cadastradas: {numero_pessoas_cadastradas}')
print(f'Quantidade de homens: {quantidade_homens}')
print(f'Quantidade mulheres menor de 20 anos: {quantidade_mulheres_menor_20}')
