"""
Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de
parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles.
"""

numeros_digitados = []

while True:
    numero = int(input('Digite um número ou digite 999 para parar o programa: '))

    if numero != 999:
        numeros_digitados.append(numero)
    else:
        break

print(f'Números digitados: {numeros_digitados}')
print(f'Quantidade de números digitados: {len(numeros_digitados)}')
print(f'Soma dos números digitados: {sum(numeros_digitados)}')

