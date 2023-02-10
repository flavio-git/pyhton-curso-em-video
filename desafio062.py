"""
Melhore o desafio061, perguntando para o usuário se
ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos.
"""

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

resultado = primeiro_termo
numero_de_termos = 10
controle = 1
controle_laco = True
while controle_laco:
    while controle < numero_de_termos:
        print(f'{resultado} ', end='')
        controle += 1
        resultado += razao

    resultado = primeiro_termo
    controle = 1

    opcao = int(input('\nDeseja ver mais termos? Se sim digite a quantidade, caso negativo digite 0: '))

    if 0 < opcao < 0:
        numero_de_termos += opcao
    elif opcao == 0:
        print('Saindo do programa...')
        controle_laco = False
    else:
        print('Você digitou uma opção inválida.')