"""
Crie um pacote chamado utilidades que tenha dois módulos
internos chamados moeda e dado.

Transfira todas as funções utilizadas nos desafios 107,
108, e 109 para o primeiro pacote e mantenha tudo funcionando.
"""

from utilidades.moeda import resumo

numero = float(input('Digite um número: '))
resumo(numero)
