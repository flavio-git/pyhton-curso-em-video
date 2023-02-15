"""
Aprimore o desafio 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
"""

jogadores_list = list()

while True:
    jogador = dict()
    gols_por_partida = list()

    jogador['nome'] = input('Nome do Jogador: ').capitalize()

    numero_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, numero_partidas):
        quantidade_gols = int(input(f'   Quantos gols na partida {i + 1}? '))
        gols_por_partida.append(quantidade_gols)

    jogador['gols'] = gols_por_partida
    jogador['total'] = sum(gols_por_partida)

    jogadores_list.append(jogador.copy())
    jogador.clear()

    while True:
        opcao_mais_jogador = input('Quer continuar? [S/N] ')
        if opcao_mais_jogador in 'SsNn':
            break
        else:
            print('ERRO! Responda apenas S ou N.')

    if opcao_mais_jogador in 'Nn':
        break

print('-=' * 30)
print(f'{"cod":<4} {"nome":<15} {"gols":<20} {"total":<3}')
print('-=' * 30)
for pos, i in enumerate(jogadores_list):
    print('{:<4}'.format(pos), end=' ')
    for k, v in i.items():
        if k == 'nome':
            print('{:<15}'.format(v), end=' ')
        elif k == 'gols':
            print('{:<20}'.format(str(v)), end=' ')
        elif k == 'total':
            print('{:<3}'.format(v))
print('-=' * 30)

while True:
    detalhes_jogador_numero = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    if detalhes_jogador_numero == 999:
        break
    elif detalhes_jogador_numero in range(0, len(jogadores_list)):
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores_list[detalhes_jogador_numero]["nome"].upper()}')
        for pos, gols in enumerate(jogadores_list[detalhes_jogador_numero]['gols']):
            print(f'        No jogo {pos + 1} fez {gols} gols.')
    else:
        print('Você digitou uma opção inválida. Tente novamente.')

print('Encerrando...')
