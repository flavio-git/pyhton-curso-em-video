"""
Crie um pequeno sistema modularizado que permita cadastrar
pessoas pelo seu nome e idade em um arquivo de texto simples.

O sistema só vai ter 2 opções: cadastrar uma nova pessoa e
listar todas as pessoas cadastradas.
"""

from utilidades import dado


def cria_pessoa():
    nome_pessoa = input('Digite o nome da pessoa: ')
    while True:
        try:
            idade_pessoa = int(input('Digite a idade da pessoas: '))
            break
        except ValueError:
            print('Favor digitar uma idade válida.')
    return nome_pessoa, idade_pessoa


def ler_arquivo(arquivo):
    try:
        leitura = open(arquivo)
    except FileNotFoundError:
        print(f'Não encontrei o arquivo "{arquivo}".')
    else:
        print(f'Lendo arquivo {arquivo}: ')
        print(leitura.read())
        leitura.close()


def gravar_dados_pessoa(arquivo, nome_pessoa, idade_pessoa):
    try:
        leitura = open(arquivo, mode='a')
    except FileNotFoundError:
        print(f'Não encontrei o arquivo "{arquivo}".')
    else:
        leitura.write(f'{nome_pessoa}, {idade_pessoa}\n')
        leitura.close()


def mostrar_pessoas(arquivo):
    try:
        leitura = open(arquivo, mode='r')
    except FileNotFoundError:
        print(f'Não encontrei o arquivo "{arquivo}".')
    else:
        for linha in leitura:
            nome, idade = linha.strip().replace(',', '').split()
            print(f'{str(nome).capitalize():<20}{idade:>15} anos')
        leitura.close()


def gera_header(msg, n):
    print('—' * n)
    print(f'{msg}'.center(n))
    print('—' * n)


def apaga_arquivo(arquivo):
    try:
        leitura = open(arquivo, 'w')
    except FileNotFoundError:
        print(f'Não encontrei o arquivo "{arquivo}".')
    else:
        leitura.write('')
        leitura.close()


def menu():
    while True:
        gera_header('MENU PRINCIPAL', 40)
        print('\033[93m1 —\033[00m \033[96mVer pessoas cadastradas\033[00m ')
        print('\033[93m2 —\033[00m \033[96mCadastrar nova pessoa\033[00m ')
        print('\033[93m3 —\033[00m \033[96mSair do sistema\033[00m ')
        print('—' * 40)
        opcao = dado.leia_int_exception('\033[92mSua opção: \033[00m')
        if opcao == 1:
            gera_header('PESSOAS CADASTRADAS', 40)
            mostrar_pessoas(arquivo_1)
        elif opcao == 2:
            gera_header('NOVO CADASTRO', 40)
            nome = input('Nome pessoa: ')
            idade = dado.leia_int_exception('Idade pessoa: ')
            gravar_dados_pessoa(arquivo_1, nome, idade)
        elif opcao == 3:
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')


arquivo_1 = 'pessoas-cadastradas.txt'

menu()
