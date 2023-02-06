"""
Crie um programa que leia o nome de
uma pessoa e diga se ela tem "Silva"
no nome
"""

nome_pessoa = input('Digite seu nome: ')

if 'SILVA' in nome_pessoa.upper():
    print('Seu nome tem Silva.')
else:
    print('Seu nome não tem Silva.')
