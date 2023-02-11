"""
Refatorando o desafio065
"""
minimo_de_numeros = 5

print(f'Para começar a execução do programa digite {minimo_de_numeros} números: ')

numeros_digitados = []

i = 0
while i < minimo_de_numeros:
    numero = int(input('Digite um número: '))
    numeros_digitados.append(numero)

    i += 1

    if i == 5:
        controle_novo_laco = True
        while controle_novo_laco:
            numero = int(input('Digite mais um número ou digite 0 para finalizar o programa: '))

            if numero != 0:
                numeros_digitados.append(numero)
            else:
                controle_novo_laco = False

print(f'\nNúmeros digitados: {sorted(numeros_digitados)}')
print(f'Quantidade de números digitados: {len(numeros_digitados)}')
print(f'Soma dos valores digitados: {sum(numeros_digitados)}')
print(f'Média dos valores digitados: {sum(numeros_digitados) / len(numeros_digitados)}')
print(f'Menor número digitado: {min(numeros_digitados)}')
print(f'Maior número digitado: {max(numeros_digitados)}')
