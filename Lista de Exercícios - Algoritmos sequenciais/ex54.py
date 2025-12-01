# ENTRADA
TAXA_SERVICO = 0.10 # Gorjeta de 10%
valor_gasto = float(input("Digite o valor gasto pelo cliente: "))

# PROCESSAMENTO
valor_taxa_servico_sobre_gasto = valor_gasto * TAXA_SERVICO
valor_total_com_taxa_servico = valor_gasto + valor_taxa_servico_sobre_gasto

# SAÍDA
print(f"O valor total com a taxa de serviço é de: R${valor_total_com_taxa_servico}")