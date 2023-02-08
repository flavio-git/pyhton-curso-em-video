"""
Desenvolva um programa que pergunte a distância em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km
para viagens de até 200km e R$ 0,45 para viagens mais longas.
"""

distancia_viagem = float(input('Quantos Km será a viagem: '))

if distancia_viagem <= 200:
    print(f'Passagem custará: {distancia_viagem * 0.50}')
else:
    print(f'Passagem custará: {distancia_viagem * 0.45}')