# ENTRADA
custo_fabrica_carro = float(input("Digite o custo de fábrica do carro: "))

# PROCESSAMENTO
# Primeiro aplicar os impostos
valor_com_imposto = custo_fabrica_carro * (1 + IMPOSTOS)

# Depois aplicar a margem do distribuidor
custo_ao_consumidor = valor_com_imposto * (1 + PORCENTAGEM_DISTRIBUIDOR)

# SAÍDA
print(f"O custo ao consumidor é: R$ {custo_ao_consumidor:.2f}")