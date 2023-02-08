"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
"""

velocidade_medida = int(input('Digite a velocidade que você estava: '))

if velocidade_medida > 80:
    velocidade_ultrapassada = velocidade_medida - 80
    valor_multa = velocidade_ultrapassada * 7
    print(f'Você ultrapassou o limite de velocidade em {velocidade_ultrapassada} Km/h.')
    print(f'O valor da multa é de R$ {valor_multa}.')
else:
    print('Você não ultrapassou o limite de velocidade.')
