"""
Desenvolva um programa que leia o
nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

— a média de idade do grupo
— qual é o nome do homem mais velho
— quantas mulheres têm menos de 20 anos
"""

quantidade_pessoas = int(input('Digite a quantidade de pessoas: '))

soma_idades = 0

nome_homem_mais_velho = ''
idade_homem_mais_velho = 0

quantidade_mulheres_menos_20_anos = 0

for i in range(1, quantidade_pessoas + 1):
    print(f'Dados pessoa {i}:')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M) ou (F): ').upper()
    print()

    soma_idades += idade

    if i == 1 and sexo == 'M':
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
    elif sexo == 'M':
        if idade > idade_homem_mais_velho:
            nome_homem_mais_velho = nome
            idade_homem_mais_velho = idade

    if sexo == 'F' and idade < 20:
        quantidade_mulheres_menos_20_anos += 1


print(f'Idade média da pessoas: {soma_idades / quantidade_pessoas}')
print(f'Nome do homem mais velho: {nome_homem_mais_velho}')
print(f'Quantidade de mulheres menores de 20 anos: {quantidade_mulheres_menos_20_anos}')