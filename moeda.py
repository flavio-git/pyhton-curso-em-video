"""
Módulo com funções básicas e úteis para soluções de pequenos problemas
"""

import locale


def aumentar(valor, percentual, formatado=False):
    resultado = valor + (valor * (percentual / 100))
    if formatado:
        return moeda(resultado, True)
    return resultado


def diminuir(valor, percentual, formatado=False):
    resultado = valor - (valor * (percentual / 100))
    if formatado:
        return moeda(resultado, True)
    return resultado


def dobro(valor, formatado=False):
    if formatado:
        return moeda(valor * 2, True)
    return valor * 2


def metade(valor, formatado=False):
    if formatado:
        return moeda(valor / 2, True)
    return valor / 2


def moeda(valor, symbol=False):
    valor_ajuste = f'{valor:,.2f}'.replace(',', 'v').replace('.', ',').replace('v', '.')
    if symbol:
        return f'R$ {valor_ajuste}'
    return valor_ajuste


def moeda_import(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, grouping=True, symbol=False)


def resumo(valor):
    print('*' * 50)
    print('RESUMO DO VALOR'.center(50))
    print('*' * 50)
    print(f"""{'Preço analisado:':<20}{moeda(valor, True):>30}
{'Dobro do preço: ':<20}{dobro(valor, True):>30}
{'Metade do preço: ':<20}{metade(valor, True):>30}
{'80% de aumento: ':<20}{aumentar(valor, 80, True):>30}
{'35% de redução: ':<20}{diminuir(valor, 35, True):>30}""")


if __name__ == '__main__':
    valor_teste_1 = 5000000000
    valor_teste_2 = 500.5
    valor_teste_3 = 500.50
    valor_teste_4 = 1500.50

    print(moeda(valor_teste_1, symbol=True))
    print(moeda(valor_teste_2))
    print(moeda(valor_teste_3))
    print(moeda(valor_teste_4))

    print(moeda_import(valor_teste_1))
    print(moeda_import(valor_teste_2))
    print(moeda_import(valor_teste_3))
    print(moeda_import(valor_teste_4))

    resumo(valor_teste_1)
