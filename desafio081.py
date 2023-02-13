"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

a) quantos números foram digitados
b) a lista de valores ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista
"""

numeros = []

while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)

    opcao_mais_numero = input('Deseja adicionar mais um número: [S/N] ')

    if opcao_mais_numero in 'Nn':
        break

print(f'Números digitados: {numeros}')
print(f'Quantidade de números digitados: {len(numeros)}')

numeros.sort(reverse=True)
print(f'Lista em ordem decrescente: {numeros}')

if 5 in numeros:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')

