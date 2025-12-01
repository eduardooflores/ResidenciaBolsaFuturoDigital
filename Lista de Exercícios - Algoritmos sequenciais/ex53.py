# ENTRADA
salario_bruto = float(input("Digite seu salário bruto mensal: "))
percentual_reajuste = float(input("Digite o percentual de reajuste: "))

# PROCESSAMENTO
valor_rajuste = salario_bruto * (percentual_reajuste / 100)
salario_liquido = salario_bruto + valor_rajuste

# SAÍDA
print(f"{salario_liquido} (salário reajustado)")