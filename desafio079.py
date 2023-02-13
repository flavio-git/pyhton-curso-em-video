"""
Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.
"""

valores = []

while True:
    numero_usuario = int(input('Digite um número: '))

    if len(valores) == 0:
        valores.append(numero_usuario)
    else:
        tem_numero_igual = False

        # i = 0
        # while i < len(valores):
        #     if valores[i] == numero_usuario:
        #         print(f'Valor {numero_usuario} não será adicionado, pois já consta na lista.')
        #         tem_numero_igual = True
        #         break
        #     i += 1

        for numero in valores:
            if numero == numero_usuario:
                print(f'Valor {numero_usuario} não será adicionado, pois já consta na lista.')
                tem_numero_igual = True
                break

        if not tem_numero_igual:
            print(f'Valor {numero_usuario} foi adicionado com sucesso.')
            valores.append(numero_usuario)

    opcao_mais_numero = input('Deseja adicionar mais um número? [S/N]: ')

    if opcao_mais_numero in 'Nn':
        break

print(f'Números digitados em ordem crescente: {sorted(valores)}')
