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
