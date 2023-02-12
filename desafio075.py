"""
Desenvolva um programa que leia quatro valores pelo
teclado e guarde-os em uma tupla. No final, mostre:

a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
c) quais foram os números pares
"""

valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))
valor_3 = int(input('Digite o terceiro valor: '))
valor_4 = int(input('Digite o quarto valor: '))

valores = (valor_1, valor_2, valor_3, valor_4)

print(f'Numéros digitados: {valores}')
print(f'Quantidade de 9: {valores.count(9)}')

if 3 in valores:
    print(f'Primeira posição do 3: {valores.index(3)}')
else:
    print(f'O número 3 não foi digitado')

print('Números pares: ', end='')
for numero in valores:
    if numero % 2 == 0:
        print(f'{numero} ', end=" ")
