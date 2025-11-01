# Questão 53. Escreva um algoritmo para ler o salário mensal e o percentual de reajuste. Calcular e
# escrever o valor do novo salário.
# [Exemplo de dados de entrada]
# 500 (salário mensal)
# 15 (percentual de reajuste)
# [Saída para os dados de entrada acima]
# 575 (salário reajustado)

# ENTRADA
salario_bruto = float(input("Digite seu salário bruto mensal: "))
percentual_reajuste = float(input("Digite o percentual de reajuste: "))

# PROCESSAMENTO
valor_rajuste = salario_bruto * (percentual_reajuste / 100)
salario_liquido = salario_bruto + valor_rajuste

# SAÍDA
print(f"{salario_liquido} (salário reajustado)")