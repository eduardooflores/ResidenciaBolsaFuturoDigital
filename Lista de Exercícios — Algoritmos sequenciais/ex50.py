# Questão 50. Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faca
# um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre
# a comissão e o salário final do funcionário.

# ENTRADA
SALARIO_FIXO = 1200
COMISSAO = 0.04
valor_vendas = float(input("Digite o valor total de vendas: "))

# PROCESSAMENTO
comissaos_vendas = valor_vendas * COMISSAO
salario_liquido = comissaos_vendas + SALARIO_FIXO

# SAÍDA
print(f"O valor da comissão é de: R${comissaos_vendas:.2f}")
print(f"O salário final do funcionário é de: R${salario_liquido:.2f}")
