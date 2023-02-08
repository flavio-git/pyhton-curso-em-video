"""
Crie um programa que mostre na tela todos
os números pares no intervalo
de 1 e 50
"""

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')

print()

# menos iterações
for i in range(2, 51, 2):
    print(i, end=' ')
