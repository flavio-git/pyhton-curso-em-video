"""
Crie um programa que leia o nome
completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras sem considerar espaços
- Quantas letras tem o primeiro nome
"""

nome = input('Digite o seu nome: ')

quantidade_letras_sem_espacos = len(nome) - nome.count(' ')

lista_palavras = nome.split()
quantidade_letras_primeiro_nome = len(lista_palavras[0])

print(f'Todo maiúsculo: {nome.upper()}')
print(f'Todo minúsculo: {nome.lower()}')
print(f'Quantidade de caracteres: {len(nome)}')
print(f'Quantidade de letras (sem espaços em branco): {quantidade_letras_sem_espacos}')
print(f'Quantidade de letras do primeiro nome: {quantidade_letras_primeiro_nome}')



