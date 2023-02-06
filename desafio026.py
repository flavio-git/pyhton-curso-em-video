"""
Faça um programa que leia uma frase
pelo teclado e mostre:

- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez
"""

frase = input('Digite uma frase: ').upper()

contagem_a = frase.count('A')
primeiro_a = frase.find('A')
ultimo_a = frase.find('A', -1)

print(f'A letra "A" aparece: {contagem_a} vezes.')
print(f'Posição da primeira letra "A": {primeiro_a}')
print(f'Última posição da letra "A": {ultimo_a}')
