"""
Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e menor valores
lidos. O programa deve perguntar ao usuário se ele
quer continuar ou não a digitar valores.
"""

print('Para começar a execução do programa digite 5 números: ')

soma_numeros_digitados = 0
quantidade_numeros_digitados = 0
maior_numero_digitado = 0
menor_numero_digitado = 0
numeros_digitados = []

i = 0
while i < 5:
    numero = int(input('Digite um número: '))
    soma_numeros_digitados += numero
    quantidade_numeros_digitados += 1
    numeros_digitados.append(numero)

    if i == 0:
        maior_numero_digitado = numero
        menor_numero_digitado = numero
    else:
        if numero > maior_numero_digitado:
            maior_numero_digitado = numero

        if numero < menor_numero_digitado:
            menor_numero_digitado = numero

    i += 1

    if i == 5:
        controle_novo_laco = True
        while controle_novo_laco:
            numero = int(input('Digite mais um número ou digite 0 para finalizar o programa: '))

            if numero != 0:
                quantidade_numeros_digitados += 1
                soma_numeros_digitados += numero
                numeros_digitados.append(numero)

                if numero > maior_numero_digitado:
                    maior_numero_digitado = numero

                if numero < menor_numero_digitado:
                    menor_numero_digitado = numero
            else:
                controle_novo_laco = False

print(f'\nNúmeros digitados: {numeros_digitados}')
print(f'Soma dos valores digitados: {soma_numeros_digitados}')
print(f'Média dos valores digitados: {soma_numeros_digitados / quantidade_numeros_digitados}')
print(f'Menor número digitado: {menor_numero_digitado}')
print(f'Maior número digitado: {maior_numero_digitado}')
