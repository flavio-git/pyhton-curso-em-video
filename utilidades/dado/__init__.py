
def leia_dinheiro(msg=''):
    while True:
        valor = input(msg)
        if valor.count(',') == 1 and valor.replace(',', '').isdigit():
            valor = valor.replace(',', '.')
        if valor.count('.') == 1 and valor.replace('.', '').isdigit() or valor.isdigit():
            return float(valor)
        else:
            print('Você digitou um valor inválido. Digite apenas números.')


if __name__ == '__main__':
    leia_dinheiro('Digite um valor: ')
    # print(valor_usuario)
