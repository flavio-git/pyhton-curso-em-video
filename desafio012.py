"""
No pacote utilidades que criamos no desafio111,
temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que consiga funcionar como a função
input(), mas com uma validação de dados para aceitar
apenas valores que sejam monetários.
"""
from utilidades.dado import leia_dinheiro
from utilidades.moeda import resumo

p = leia_dinheiro('Digite o preço: R$ ')
resumo(p, 10, 30)
