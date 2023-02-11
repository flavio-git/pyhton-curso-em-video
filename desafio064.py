"""
Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de
parada. No final mostre quantos números foram
digitados e qual foi a soma entre eles.
"""

print('Enquanto você não digitar 999 o programa irá ler um número...')

numero = 0
quantidade_de_numeros = 0
soma_dos_numeros_digitados = 0
numeros_digitados = []

while numero != 999:
    numero = int(input('Digite um número: '))

    if numero != 999:
        quantidade_de_numeros += 1
        soma_dos_numeros_digitados += numero
        numeros_digitados.append(numero)

print(f'Quantidade de números digitados: {quantidade_de_numeros}')
print(f'Soma dos numeros digitados: {soma_dos_numeros_digitados}')
print(f'Números digitados: {numeros_digitados}')
