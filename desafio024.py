"""
Crie um programa que leia o nome de
uma cidade e diga se ela começa com
o nome "Santo"
"""

nome_cidade = input('Digite o nome de sua cidade: ').split()

if 'SANTO' in nome_cidade[0].upper():
    print("Sua cidade começa com Santo no nome.")
else:
    print('Sua cidade não começa com Santo no nome.')
