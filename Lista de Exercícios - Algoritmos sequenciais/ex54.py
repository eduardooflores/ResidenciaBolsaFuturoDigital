# Questão 54. Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% para
# o garçom. Faça um programa que leia o valor gasto com as despesas realizadas em um restaurante
# e mostre o valor total com a gorjeta.

# ENTRADA
TAXA_SERVICO = 0.10 # Gorjeta de 10%
valor_gasto = float(input("Digite o valor gasto pelo cliente: "))

# PROCESSAMENTO
valor_taxa_servico_sobre_gasto = valor_gasto * TAXA_SERVICO
valor_total_com_taxa_servico = valor_gasto + valor_taxa_servico_sobre_gasto

# SAÍDA
print(f"O valor total com a taxa de serviço é de: R${valor_total_com_taxa_servico}")