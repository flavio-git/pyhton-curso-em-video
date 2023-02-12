"""
Crie uma tupla preenchida com os 20 primeiros colocados
da tabela do Campeonato Brasileiro, na ordem de colocação.
Depois mostre:

a) apenas os 5 primeiros colocados.
b) os últimos 4 colocados na tabels.
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time do Vasco
"""

colocacao_campeonato = (
    'Flamengo',
    'Santos',
    'Palmeiras',
    'Grêmio',
    'Athletico-PR',
    'São Paulo',
    'Internacional',
    'Corinthians',
    'Fortaleza',
    'Goiás',
    'Bahia',
    'Vasco',
    'Atlético-MG',
    'Fluminense',
    'Botafogo',
    'Ceará',
    'Cruzeiro',
    'CSA',
    'Chapecoense',
    'Avaí',
)

print('CLASSIFICAÇÃO CAMPEONATO BRASILEIRO 2019')
print(f'Os 5 primeiros colocados: {colocacao_campeonato[:5]}')
print(f'Os 4 últimos colocados: {colocacao_campeonato[-4:]}')
print(f'O time do Vasco terminou na colocação: {(colocacao_campeonato.index("Vasco")) + 1}')

print('\nTimes por ordem alfabética: ')
for time in sorted(colocacao_campeonato):
    print(time)

print('\nTimes por posição na tabela: ')
for pos, time in enumerate(colocacao_campeonato):
    print(f'{pos + 1 }. {time}')
