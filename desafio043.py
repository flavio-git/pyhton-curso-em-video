"""
Desenvolva uma lógica que leia o peso e a altura de
uma pessoa, calcule seu IMC e mostre seu status, de
acordo com a tabela abaixo:

— abaixo de 18,5: ABAIXO DO PESO
— entre 18,5 e 25: PESO IDEAL
— 25 até 30: SOBREPESO
— 30 até 40: OBESIDADE
— acima de 40: OBESIDADE MÓRBIDA
"""

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC: {imc:.1} | Situação: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print(f'Seu IMC: {imc:.1} | Situação: PESO IDEAL')
elif 25 <= imc < 30:
    print(f'Seu IMC: {imc:.1} | Situação: SOBREPESO')
elif 30 <= imc < 40:
    print(f'Seu IMC: {imc:.1} | Situação: OBESIDADE')
else:
    print(f'Seu IMC: {imc:.1} | Situação: OBESIDADE MÓRBIDA')


