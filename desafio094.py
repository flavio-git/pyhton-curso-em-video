"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:

a) quantas pessoas cadastradas
b) a média de idade
c) uma lista com mulheres
d) uma lista com idade acima da média
"""

pessoas_list = list()

controle = True
while controle:
    pessoa = dict()
    pessoa['nome'] = input('Nome: ')

    while True:
        sexo_pessoa = input('Sexo: [M/F] ')
        if sexo_pessoa in 'MmFf':
            pessoa['sexo'] = sexo_pessoa
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')

    while True:
        idade_pessoa = int(input('Idade: '))
        if idade_pessoa in range(1, 130):
            pessoa['idade'] = idade_pessoa
            break
        else:
            print('ERRO! Por favor, digite um valor entre 1 e 130.')

    while True:
        opcao_adicionar_mais_pessoa = input('Quer continuar? [S/N] ')
        if opcao_adicionar_mais_pessoa in 'Nn':
            controle = False
            break
        elif opcao_adicionar_mais_pessoa in 'Ss':
            break
        else:
            print('ERRO! Responda apenas S ou N.')

    pessoas_list.append(pessoa.copy())
    pessoa.clear()


quantidade_de_pessoas = len(pessoas_list)

soma_idades = 0
for pessoa in pessoas_list:
    soma_idades += pessoa['idade']
media_idades = soma_idades / quantidade_de_pessoas

pessoas_idade_acima_media = list()
for pessoa in pessoas_list:
    if pessoa['idade'] > media_idades:
        pessoas_idade_acima_media.append(pessoa)

mulheres = list()
for pessoa in pessoas_list:
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa['nome'])

print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas_list)} cadastradas.')
print(f'B) A média de idade é de {media_idades:.2f} anos.')
print(f'C) As mulheres cadastradas: {mulheres}')
print(f'D) Lista das pessoas que estão acima da média: ')
for pessoa in pessoas_idade_acima_media:
    for k, v in pessoa.items():
        print(f'    {str(k).capitalize()} = {v}', end='; ')
    print()
print('<< ENCERRADO >>')


