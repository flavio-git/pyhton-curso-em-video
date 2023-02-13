"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
"""

valores = []
quantidade_valores_digitados = 5  # quantidade mínima que o usuário deve digitar

menor_valor = 0
maior_valor = 0

for i in range(0, quantidade_valores_digitados):
    numero_usuario = int(input('Digite um valor: '))

    if i == 0:
        menor_valor = maior_valor = numero_usuario
    else:
        if numero_usuario > maior_valor:
            maior_valor = numero_usuario
        elif numero_usuario < menor_valor:
            menor_valor = numero_usuario

    valores.append(numero_usuario)


# procurando posição do menor valor
print(f'Menor valor digitado {menor_valor} está nas seguintes posições: ', end='')
for posicao, valor in enumerate(valores):
    if valor == menor_valor:
        print(f'{posicao}... ', end='')

print()

# procurando posição do maior valor
print(f'Maior valor digitado {maior_valor} está nas seguintes posições: ', end='')
for posicao, valor in enumerate(valores):
    if valor == maior_valor:
        print(f'{posicao}... ', end='')

print()


# print(f'Maior valor digitado {max(valores)} e sua posição na lista é {valores.index(max(valores))}.')
# print(f'Menor valor digitado {min(valores)} e sua posição na lista é {valores.index(min(valores))}.')

