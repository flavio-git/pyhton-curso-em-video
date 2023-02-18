
def leia_dinheiro(msg=''):
    while True:
        valor = input(msg)
        if valor.count(',') == 1 and valor.replace(',', '').isdigit():
            valor = valor.replace(',', '.')
        if valor.count('.') == 1 and valor.replace('.', '').isdigit() or valor.isdigit():
            return float(valor)
        else:
            print('Você digitou um valor inválido. Digite apenas números.')


def leia_int_exception(msg=''):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError as err:
            print('Você digitou uma expressão inválida. Por favor tente novamente.')


def leia_float_exception(msg=''):
    while True:
        try:
            valor = input(msg)
            if valor.count(',') == 1 and valor.replace(',', '').isdigit():
                valor = valor.replace(',', '.')
            return float(valor)
        except ValueError:
            print('Você digitou uma expressão inválida. Por favor tente novamente.')


if __name__ == '__main__':
    leia_dinheiro('Digite um valor: ')
    # print(valor_usuario)
