"""
Refaça o desafio051, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando o while
"""

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

resultado = primeiro_termo
controle = 1
while controle < 10:
    print(f'{resultado} ', end='')
    controle += 1
    resultado += razao

