"""
Escreva um programa que pergunte o salário
de um funcionário e calcule o valor do seu
aumento.

Para salários superiores a R$ 1.250,00,
calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é
de 15%
"""

salario_funcionario = float(input('Digite o salário do funcionário: '))
novo_salario = 0

if salario_funcionario > 1250:
    novo_salario = salario_funcionario * 1.10
else:
    novo_salario = salario_funcionario * 1.15

print(f'Novo salário após o aumento: {novo_salario}')
