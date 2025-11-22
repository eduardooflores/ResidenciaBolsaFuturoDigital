#  Questão 55. Para vários tributos, a base de cálculo é o salário mínimo. Faça um programa que leia
# o valor do salário mínimo e o valor do salário de uma pessoa. Calcule e mostre quantos salários
# mínimos a pessoa ganha.

# ENTRADA
salario_minimo = float(input("Digite o valor do salário mínimo: "))
salario = float(input("Digite o valor do seu salário: "))

# PROCESSAMENTO
qntd_salarios_minimos = salario / salario_minimo

# SAÍDA
print(f"O seu salário é equivalente a {qntd_salarios_minimos} salários mínimos.")