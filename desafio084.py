"""
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista, mostre:

a) quantas pessoas foram cadastradas
b) uma listagem com as pessoas mais pessadas
c) uma listagem com as pessoas mais leves
"""

pessoas = []
pessoas_mais_pesadas = []
pessoas_mais_leves = []

i = 0
while True:
    pessoa = list()
    nome = input('Digite o nome da pessoa: ')
    peso = int(input('Digite o peso da pessoas: '))
    pessoa.append(nome)
    pessoa.append(peso)
    pessoas.append(pessoa.copy())

    if i == 0:
        pessoas_mais_pesadas.append(pessoa.copy())
        pessoas_mais_leves.append(pessoa.copy())
    else:
        if peso > pessoas_mais_pesadas[0][1]:
            pessoas_mais_pesadas.clear()
            pessoas_mais_pesadas.append(pessoa.copy())
        elif peso == pessoas_mais_pesadas[0][1]:
            pessoas_mais_pesadas.append(pessoa.copy())

        if peso < pessoas_mais_leves[0][1]:
            pessoas_mais_leves.clear()
            pessoas_mais_leves.append(pessoa.copy())
        elif peso == pessoas_mais_leves[0][1]:
            pessoas_mais_leves.append(pessoa.copy())

    pessoa.clear()

    opcao_mais_pessoas = input('Deseja inserir mais uma pessoa? [S/N]: ')

    if opcao_mais_pessoas in 'Nn':
        break

    i += 1

print()
print(f'Quantidade de pessoas cadastradas {len(pessoas)}')

print(f'As pessoas mais pesadas são: ')
for pessoa in pessoas_mais_pesadas:
    print(f'Nome: {pessoa[0]} | Peso: {pessoa[1]}Kg.')

print()
print(f'As pessoas mais leves são: ')
for pessoa in pessoas_mais_leves:
    print(f'Nome: {pessoa[0]} | Peso: {pessoa[1]}Kg.')
